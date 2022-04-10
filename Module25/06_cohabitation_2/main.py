import random

class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

    def get_dirty(self):
        self.dirt += 5

    def __str__(self):
        self.get_dirty()
        return 'Дом: Еда: {}, Деньги: {}, Кошачий корм: {}, Степень загрязнения: {}'.format(
            self.food, self.money, self.cat_food, self.dirt
        )


class Man:
    def __init__(self):
        super().__init__()
        self.satiety = 30
        self.happy = 100
        self.alive = True
        self.house = my_house

    def eat(self):
        if self.house.food >= 30:
            food_amount = random.randint(1, 30)
        elif self.house.food > 1:
            food_amount = random.randint(1, self.house.food // 2)
        else:
            food_amount = self.house.food
        self.satiety += food_amount
        self.house.food -= food_amount
        return 'ест {} пищи'.format(food_amount)

    def pet_the_cat(self):
        self.happy += 5
        self.satiety -= 10

    def __str__(self):
        return 'сытость: {}, удовлетворенность: {}'.format(self.satiety, self.happy)

    def is_alive(self, satiety, happy):
        if self.satiety <= 0:
            self.alive = False
            return 'умер от голода!'
        elif self.happy <= 0:
            self.alive = False
            return 'умер от депрессии!'
        else:
            return ''

class Husband(Man):
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    def action(self):
        self.alive = self.is_alive()
        if not self.alive:
            raise Exception('{} мертв!'.format(self.name))
        else:
            if self.house.dirt > 90:
                self.happy -= 10
            if self.satiety <= 10 and self.house.food > 0:
                self.eat()
            elif self.house.money < 100 and self.satiety >= 1:
                self.work()
            elif self.happy <= 10:
                self.pet_the_cat()
            else:
                self.play()

    def is_alive(self):
        info = super().is_alive(self.satiety, self.happy)
        if not self.alive:
            info = ' '.join((self.name, info))
            print(info)
        return self.alive

    def eat(self):
        info = super().eat()
        print(self.name, info)

    def work(self):
        print('{} идет на работу'.format(self.name))
        self.house.money += 150
        self.satiety -= 10

    def play(self):
        print('{} играет на компьютере'.format(self.name))
        self.happy += 20
        self.satiety -= 10

    def pet_the_cat(self):
        super().pet_the_cat()
        print('{} гладит кота'.format(self.name))


    def __str__(self):
        info = super().__str__()
        info = ' '.join(
            (
                'Имя: {}, Состояние:'.format(self.name),
                info)
        )
        return info


class Wife(Man):
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house
        self.fur = 0

    def action(self):
        self.alive = self.is_alive()
        if not self.alive:
            raise Exception('{} мертв!'.format(self.name))
        else:
            if self.house.dirt > 90:
                self.happy -= 10
            if self.satiety <= 10 and self.house.food > 0:
                self.eat()
            elif (self.house.food <= 30 or self.house.cat_food <= 10) and self.house.money >= 40:
                self.buy_food()
            elif self.house.dirt >= 50 and self.satiety >= 1:
                self.clean()
            elif self.happy <= 10 and self.house.money >= 350:
                self.shopping()
            else:
                self.pet_the_cat()
            self.__str__()

    def eat(self):
        info = super().eat()
        print(self.name, info)

    def buy_food(self):
        print('{} покупает продукты'.format(self.name))
        self.house.food += 30
        self.house.cat_food += 10
        self.house.money -= 40
        self.satiety -= 10

    def shopping(self):
        print('{} идет в магазин за шубой'.format(self.name))
        self.happy += 60
        self.fur += 1
        self.house.money -= 350
        self.satiety -= 10

    def clean(self):
        print('{} убирает дом'.format(self.name))
        if self.house.dirt <= 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100
        self.satiety -= 10

    def pet_the_cat(self):
        super().pet_the_cat()
        print('{} гладит кота'.format(self.name))

    def __str__(self):
        info = super().__str__()
        info = ' '.join(
            (
                'Имя: {}, Состояние:'.format(self.name),
                info)
        )
        return info

    def is_alive(self):
        info = super().is_alive(self.satiety, self.happy)
        if not self.alive:
            info = ' '.join((self.name, info))
            print(info)
        return self.alive


class Cat:
    def __init__(self, name, house):
        super().__init__()
        self.satiety = 30
        self.name = name
        self.house = house
        self.alive = True

    def action(self):
        self.alive = self.is_alive()
        if not self.alive:
            raise Exception('Кот {} мертв!'.format(self.name))
        else:
            if self.satiety <= 15 and self.house.cat_food > 0:
                self.eat()
            else:
                rand_action = random.choice(['wallpaper', 'sleep'])
                if rand_action == 'wallpaper':
                    self.tearing_wallpaper()
                else:
                    self.sleep()

    def __str__(self):
        return 'Кот: {}, Сытость: {}'.format(self.name, self.satiety)


    def eat(self):
        if self.house.cat_food >= 10:
            food_amount = random.randint(1, 10)
        elif self.house.cat_food > 1:
            food_amount = random.randint(1, self.house.cat_food)
        else:
            food_amount = self.house.cat_food
        print('Кот {} ест {} кошачьего корма'.format(self.name, food_amount))
        self.satiety += food_amount
        self.house.cat_food -= food_amount

    def sleep(self):
        print('Кот {} спит'.format(self.name))
        self.satiety -= 10

    def tearing_wallpaper(self):
        print('Кот {} дерёт обои'.format(self.name))
        self.house.dirt += 5
        self.satiety -= 10

    def is_alive(self):
        if self.satiety <= 0:
            self.alive = False
            print('Кот {} умер от голода!'.format(self.name))
        return self.alive


my_house = House()
husband = Husband('Виталик', my_house)
wife = Wife('Матильда', my_house)
cat = Cat('Барсик', my_house)

for i_day in range(366):
    try:
        print('\nДень:', i_day + 1)
        if husband.is_alive():
            husband.action()
        if wife.is_alive():
            wife.action()
        if cat.is_alive():
            cat.action()
        print(my_house)
        print(husband)
        print(wife)
        print(cat)
    except Exception as error:
        print(error)