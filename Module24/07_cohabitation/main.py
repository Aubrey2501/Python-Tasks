import random

class Human:
    satiety = 50
    def __init__(self, name):
        self.name = name
        self.home = Home()
    def eat(self):
        print('Надо поесть!')
        if self.home.meal >= 1:
            self.satiety += 1
            self.home.meal -= 1
        else:
            print('Холодильник пуст. Ходи голодный!')
            self.shopping()
    def work(self):
        print('Нужно поработать!')
        if self.satiety >= 1:
            self.satiety -= 1
            self.home.money += 1
        else:
            print('Умираю от голода, работать не могу!')
            self.eat()
    def play(self):
        if self.satiety >= 1:
            print('Можно поиграть')
            self.satiety -= 1
        else:
            print('Очень хочется есть! Не до игр!')
            self.eat()
    def shopping(self):
        print('Нужно идти в магазин')
        if self.home.money >= 1:
            self.home.meal += 1
            self.home.money -= 1
        else:
            print('Денег нет, шопинг отменяется!')
            self.work()
    def human_info(self, day):
        print('\nДень {}. Текущее состояние:\nИмя: {}\nСытость: {}\nЕды в холодильнике: {}\nДенег: {}\n'.format
              (day, self.name, self.satiety, self.home.meal, self.home.money))
        if self.satiety > 0:
            return True
        return False

    def action(self, dice):
        if self.satiety < 20:
            self.eat()
        elif self.home.meal < 10:
            self.shopping()
        elif self.home.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


class Home:
    def __init__(self):
        self.meal = 50
        self.money = 0

test_subj = ['Иван', 'Михаил']
alive = True
for i_name in test_subj:
    person = Human(i_name)
    for day in range(366):

        alive = person.human_info(day)
        if alive:
            dice = random.randint(1, 6)
            print('Бросаем кубик! На кубике выпало: ', dice)
            person.action(dice)
            # person.satiety -= 1
        else:
            print('Увы, клиент помер с голоду :(')
            break
    print(40 * '_')
    if alive:
        print('Поздравляем! Клиент выжил')
