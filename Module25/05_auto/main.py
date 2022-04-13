# coding: utf-8
import math
import random


class Car:
    """
    Базовый Класс Автомобиль
    Attributes:
        type (str): тип транспортного средства
        coord_x (int): координата по оси Х
        coord_y (int): координата по оси Y
        direction (int): направление движения в градусах
    :param:
        x - начальная координата по оси Х
        y - начальная координата по оси Y
    """
    def __init__(self, car_type, x, y):
        self.type = car_type
        self.coord_x = x
        self.coord_y = y
        self.direction = 0

    def turn_right(self, angle):
        """
        Метод: поворот направо
        :param angle: (int): угол поворота в градусах
        """
        self.direction += angle
        if self.direction >= 360:
            self.direction -= 360
        print('Поворачиваем на {} градусов вправо. Текущее направление: {} градусов'.format(angle, self.direction))

    def turn_left(self, angle):
        """
        Метод: поворот налево
        :param angle: (int): угол поворота в градусах
        """
        self.direction -= angle
        if self.direction < 0:
            self.direction += 360
        print('Поворачиваем на {} градусов влево. Текущее направление: {} градусов'.format(angle, self.direction))

    def move(self, distance):
        """
        Метод: движение прямо
        :param distance (int): расстояние в км.
        """
        print('Едем {}км вперед'.format(distance))
        self.coord_x += distance * math.sin(math.radians(self.direction))
        self.coord_x = round(self.coord_x, 1)
        self.coord_y += distance * math.cos(math.radians(self.direction))
        self.coord_y = round(self.coord_y, 1)

    def __str__(self):
        return '{}: текущие координаты: ({} : {})\n'.format(self.type, self.coord_x, self.coord_y)


class Bus(Car):
    """
    Класс Автобус, дочерний от класса Автомобиль
    Attributes:
        bus_type (str): тип транспортного средства
        coord_x (int): координата по оси Х
        coord_y (int): координата по оси Y
        direction (int): направление движения в градусах
        passengers (int): количество пассажиров
        money (int): количество денег, собранных за проезд
        capasity (int): вместимость автобуса (пассажиров)
        ticket_price (int): цена билета
    :param:
        x - начальная координата по оси Х
        y - начальная координата по оси Y
    """
    def __init__(self, bus_type, x, y):
        super().__init__(bus_type, x, y)
        self.passengers = 0
        self.money = 0
        self.capacity = 120
        self.ticket_price = 50

    def turn_left(self, angle):
        """
        Метод: поворот налево
        :param angle: (int): угол поворота в градусах
        """
        super(Bus, self).turn_left(angle=angle)


    def turn_right(self, angle):
        """
        Метод: поворот направо
        :param angle: (int): угол поворота в градусах
        """
        super(Bus, self).turn_right(angle=angle)

    def move(self, distance):
        """
        Метод: движение прямо
        :param distance (int): расстояние в км.
        """
        super(Bus, self).move(distance=distance)


    def bus_stop(self, get_in, get_out):
        """
        Метод: остановка автобуса
        :param get_in: количество вошедших пассажиров
        :param get_out: количество пассажиров, вышедших из автобуса
        """
        print('Остановка. Выходят {} человек, входят {} человек.'.format(get_out, get_in))
        self.passengers -= get_out
        if get_in > self.capacity - self.passengers:
            get_in = self.capacity - self.passengers
            print('Все пассажиры не влезли. Вошло {} человек'.format(get_in))
        self.passengers += get_in
        self.money += get_in * self.ticket_price

    def __str__(self):
        info = super().__str__()
        info = ''.join((info, 'В автобусе {} пассажиров. Денег в кассе: {}\n'.format(self.passengers, self.money)))
        return info


my_car = Car('Автомобиль', 0, 0)
print(my_car)
my_car.turn_right(90)
my_car.move(20)
print(my_car)
my_car.turn_left(55)
my_car.move(30)
print(my_car)
my_car.turn_left(35)
my_car.move(30)
print(my_car)
my_car.turn_left(180)
my_car.move(20)
print(my_car)

my_bus = Bus('Автобус', 0, 0)
print(my_bus)
my_bus.bus_stop(25, 0)
print(my_bus)
my_bus.turn_left(30)
my_bus.move(3)
my_bus.bus_stop(15, 8)
print(my_bus)
my_bus.turn_right(40)
my_bus.move(2)
my_bus.bus_stop(12, 8)
print(my_bus)

# зачет!
