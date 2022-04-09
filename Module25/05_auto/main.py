# coding: utf-8
import math
import random


class Car:
    def __init__(self, x, y, dir):
        self.coord_x = x
        self.coord_y = y
        self.direction = dir

    def turn(self, angle):
        if angle <= 180:
            self.direction += angle
        else:
            self.direction -= (360 - angle)
        if self.direction >= 360:
            self.direction -= 360
        print('Текущее направление: ', self.direction, 'градусов')

    def move(self, distance):
        self.coord_x += distance * math.cos(self.direction)
        self.coord_x = round(self.coord_x, 1)
        self.coord_y += distance * math.sin(self.direction)
        self.coord_y = round(self.coord_y, 1)

    def get_coord(self):
        return 'Текущие координаты: {} : {}\n'.format(self.coord_x, self.coord_y)


my_car = Car(0, 0, 15)
my_car.turn(25)
my_car.move(30)
print(my_car.get_coord())
