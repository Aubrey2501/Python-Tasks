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
        return 'Дом:\n Еда: {}, Деньги: {}, Кошачий корм: {}, Степень загрязнения: {}'.format(
            self.food, self.money, self.cat_food, self.dirt
        )

class Man:
    def __init__(self):
        super().__init__()
        self.satiety = 30
        self.happy = 100
        self.alive = True

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
        self.is_alive()
        if not self.alive:
            raise Exception('{} мертв!'.format(self.name))
        else:
            if self.house.dirt > 90:
                self.happy -= 10
            if self.satiety <= 5 and self.house.food > 0:
                if self.house.food >= 30:
                    food_amount = random.randint(1, 30)
                else:
                    food_amount = random.randint(1, self.house.food)
                self.eat(food_amount)
            elif self.house.money <= 50 and self.satiety >= 1:
                self.work()
            else:
                self.pet_the_cat()

    def is_alive(self):
        info = super().is_alive(self.satiety, self.happy)
        if not self.alive:
            info = ' '.join((self.name, info))
            print(info)

    def eat(self, amount):
        self.satiety += amount
        self.house.food -= amount

    def work(self):
        self.house.money += 150
        self.satiety -= 10

    def play(self):
        self.happy += 20
        self.satiety -= 10

    def pet_the_cat(self):
        self.happy += 5
        self.satiety -= 10

    def __str__(self):
        info = super().__str__()
        info = ' '.join(
            (
                'Имя: {}, Состояние:'.format(self.name),
                info)
        )


class Wife(Man):
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house
        self.fur = 0

    def action(self):
        if not self.alive:
            raise Exception('{} мертв!'.format(self.name))
        else:
            if self.house.dirt > 90:
                self.happy -= 10
            if self.satiety <= 5 and self.house.food > 0:
                if self.house.food >= 30:
                    food_amount = random.randint(1, 30)
                else:
                    food_amount = random.randint(1, self.house.food)
                self.eat(food_amount)
            elif (self.house.food <= 15 or self.house.cat_food <= 5) and self.house.money >= 15:
                self.buy_food()
            elif self.happy <= 15 and self.house.money >= 350:
                self.shopping()
            elif self.house.dirt >= 10 and self.satiety >= 1:
                self.clean()
            else:
                self.pet_the_cat()
            self.__str__()

    def eat(self, amount):
        self.satiety += amount
        self.house.food -= amount

    def buy_food(self):
        self.house.food += 10
        self.house.cat_food += 5
        self.house.money -= 15
        self.satiety -= 10

    def shopping(self):
        self.happy += 60
        self.fur += 1
        self.house.money -= 350
        self.satiety -= 10

    def clean(self):
        if self.house.dirt <= 100
            self.house.dirt = 0
        else:
            self.house.dirt -= 100
        self.satiety -= 10

    def pet_the_cat(self):
        self.happy += 5
        self.satiety -= 10

    def __str__(self):
        info = super().__str__()
        info = ' '.join(
            (
                'Имя: {}, Состояние:'.format(self.name),
                info)
        )

    def is_alive(self):
        info = super().is_alive(self.satiety, self.happy)
        if not self.alive:
            info = ' '.join((self.name, info))
            print(info)


class Cat:
    def __init__(self, name, house):
        super().__init__()
        self.satiety = 30
        self.name = name
        self.house = house
        self.alive = True

    def action(self):
        if not self.alive:
            raise Exception('Кот {} мертв!'.format(self.name))
        else:
            if self.satiety <= 3 and self.house.cat_food > 0:
                if self.house.food >= 10:
                    food_amount = random.randint(1, 10)
                else:
                    food_amount = random.randint(1, self.house.food)
                self.eat(food_amount)
            else:
                rand_action = random.choice(['wallpaper', 'sleep'])
                if rand_action == 'wallpaper':
                    self.tearing_wallpaper()
                else:
                    self.sleep()

    def __str__(self):
        return 'Кот {}, Сытость: {}'.format(self.name, self.satiety)


    def eat(self, amount):
        self.satiety += amount
        self.house.cat_food -= amount

    def sleep(self):
        self.satiety -= 10

    def tearing_wallpaper(self):
        self.house.dirt += 5
        self.satiety -= 10

