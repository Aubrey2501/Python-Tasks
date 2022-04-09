import random

class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0


class Man:
    def __init__(self):
        super().__init__()
        self.satiety = 30
        self.happy = 100
        self.alive = True


class Husband(Man):
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    def action(self):
        if not self.alive:
            raise Exception('{} мертв!'.format(self.name))
        else:
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

    def eat(self, amount):
        self.satiety += amount
        self.house.food -= amount

    def work(self):
        self.house.money += 150

    def play(self):
        self.happy += 20

    def pet_the_cat(self):
        self.happy += 5


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

    def eat(self, amount):
        self.satiety += amount
        self.house.food -= amount

    def buy_food(self):
        self.house.food += 10
        self.house.cat_food += 5
        self.house.money -= 15

    def shopping(self):
        self.happy += 60
        self.fur += 1
        self.house.money -= 350

    def clean(self):
        if self.house.dirt <= 100
            self.house.dirt = 0
        else:
            self.house.dirt -= 100

    def pet_the_cat(self):
        self.happy += 5


class Cat:
    def __init__(self, name, house):
        super().__init__()
        self.satiety = 30
        self.name = name
        self.house = house
        self.alive = True

    def action(self):
        if not self.alive:
            raise Exception('{} мертв!'.format(self.name))
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

    def eat(self, amount):
        self.satiety += amount
        self.house.cat_food -= amount

    def sleep(self):
        pass

    def tearing_wallpaper(self):
        self.house.dirt += 5

