import random

class House:
    """
    Базовый класс Дом
    Attributes:
        money (int): количество денег
        food (int): количество еды в холодильнике
        cat_food (int): количество единиц кошачьего корма
        dirt (int): степень загрязненности
    """
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

    def get_dirty(self):
        """ Метод накапливать грязь, описывает увеличение числа единиц мусора каждый день"""
        self.dirt += 5

    def __str__(self):
        self.get_dirty()
        return 'Дом: Еда: {}, Деньги: {}, Кошачий корм: {}, Степень загрязнения: {}'.format(
            self.food, self.money, self.cat_food, self.dirt
        )


class Man:
    """
    Базовый класс Человек
    Attributes:
        satiety (int): уровень сытости
        happy (int): уровень счастья
        alive (bool): аттрибут жив/мертв
        house (type): ссылка на элемент класса Дом

    """
    def __init__(self):
        self.satiety = 30
        self.happy = 100
        self.alive = True
        self.house = my_house

    def eat(self):
        """
        Метод Есть (принимать пищу)
        :param:
            food_amount (int) - количество единиц съеденной пищи
            house.food (int): количество оставшейся пищи в доме
        """
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
        """Метод Гладить кота"""
        self.happy += 5
        self.satiety -= 10

    def __str__(self):
        return 'сытость: {}, удовлетворенность: {}'.format(self.satiety, self.happy)

    def is_alive(self, satiety, happy):
        """Проверка, жив ли персонаж на начало каждого дня"""
        if self.satiety <= 0:
            self.alive = False
            return 'умер от голода!'
        elif self.happy <= 0:
            self.alive = False
            return 'умер от депрессии!'
        else:
            return ''

class Husband(Man):
    """
    Класс Муж, дочерний от класса Человек
    Attributes:
        name (str): имя
        house (type): ссылка на элемент класса Дом
    Аттрибуты базового класса:
        satiety (int): уровень сытости
        happy (int): уровень счастья
        alive (bool): аттрибут жив/мертв
    """
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    def action(self):
        """
        Основной метод Действие дня, проверяет жив ли персонаж и вызывает действия: еда, работа, гладить кота или играть
        """
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
        """Проверка, жив ли персонаж"""
        info = super().is_alive(self.satiety, self.happy)
        if not self.alive:
            info = ' '.join((self.name, info))
            print(info)
        return self.alive

    def eat(self):
        """Метод Принимать пищу"""
        info = super().eat()
        print(self.name, info)

    def work(self):
        """Метод Работать"""
        print('{} идет на работу'.format(self.name))
        self.house.money += 150
        self.satiety -= 10

    def play(self):
        """Метод Играть"""
        print('{} играет на компьютере'.format(self.name))
        self.happy += 20
        self.satiety -= 10

    def pet_the_cat(self):
        """Метод Гладить кота"""
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
    """
    Класс Жена, дочерний от класса Человек
    Attributes:
        name (str): имя
        house (type): ссылка на элемент класса Дом
    Аттрибуты базового класса:
        satiety (int): уровень сытости
        happy (int): уровень счастья
        alive (bool): аттрибут жив/мертв
    """
    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house
        self.fur = 0

    def action(self):
        """
        Основной метод Действие дня, проверяет жив ли персонаж и вызывает действия: еда, покупка продуктов, уборка и т.д.
        """
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
        """Метод Принимать пищу"""
        info = super().eat()
        print(self.name, info)

    def buy_food(self):
        """Метод Покупать продукты"""
        print('{} покупает продукты'.format(self.name))
        self.house.food += 30
        self.house.cat_food += 10
        self.house.money -= 40
        self.satiety -= 10

    def shopping(self):
        """Метод Покупать шубу"""
        print('{} идет в магазин за шубой'.format(self.name))
        self.happy += 60
        self.fur += 1
        self.house.money -= 350
        self.satiety -= 10

    def clean(self):
        """Метод Убирать Дом"""
        print('{} убирает дом'.format(self.name))
        if self.house.dirt <= 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100
        self.satiety -= 10

    def pet_the_cat(self):
        """ Метод Гладить кота"""
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
        """Проверка, жив ли персонаж?"""
        info = super().is_alive(self.satiety, self.happy)
        if not self.alive:
            info = ' '.join((self.name, info))
            print(info)
        return self.alive


class Cat:
    """
    Класс Кот
    Attributes:
        satiety (int): уровень сытости
        name (str): имя
        alive (bool): аттрибут жив/мертв
        house (type): ссылка на элемент класса Дом
    """
    def __init__(self, name, house):
        self.satiety = 30
        self.name = name
        self.house = house
        self.alive = True

    def action(self):
        """Метод выбора действия: есть, спать или драть обои"""
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
        """Метод Есть"""
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
        """Метод спать"""
        print('Кот {} спит'.format(self.name))
        self.satiety -= 10

    def tearing_wallpaper(self):
        """Метод драть обои"""
        print('Кот {} дерёт обои'.format(self.name))
        self.house.dirt += 5
        self.satiety -= 10

    def is_alive(self):
        """Проверка, жив ли персонаж"""
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