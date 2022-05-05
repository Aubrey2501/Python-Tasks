from typing import Any, SupportsInt
from abc import ABC
import math


class Figure(ABC):
    """Абстрактный базовый класс для плоских фигур"""
    def __init__(self) -> None:
        self.figure = None
        self._length = None
        self._height = None
        self.__square = None
        self.__perimeter = None


class Foursquare(Figure):
    """ Класс Квадрат. Родительский класс Figure """
    def __init__(self, length: int) -> None:
        super().__init__()
        self.figure = 'Квадрат'
        self._length = length
        self.__square = self.set_4square()
        self.__perimeter = self.set_4perimeter()
        self.__str__()

    def __str__(self):
        return f'{self.figure} с длинной стороны {self._length}, периметром {self.__perimeter} ' \
               f'и площадью {self.__square}'

    @property
    def square(self):
        return self.__square

    @property
    def perimeter(self):
        return self.__perimeter

    def set_4square(self):
        self.__square = self._length ** 2
        return self.__square

    def set_4perimeter(self):
        self.__perimeter = self._length * 4
        return self.__perimeter


class Triangle(Figure):
    """ Класс Треугольник. Родительский класс Figure """
    def __init__(self, length: int, height: int) -> None:
        super().__init__()
        self.figure = 'Треугольник'
        self._length = length
        self._height = height
        self.__square = self.set_3square()
        self.__perimeter = self.set_3perimeter()

    def __str__(self):
        return f'{self.figure} с длиной основания {self._length}, высотой {self._height}, ' \
               f'периметром {self.__perimeter:.3f} и площадью {self.__square}'

    @property
    def square(self):
        return self.__square

    @property
    def perimeter(self):
        return self.__perimeter

    def set_3square(self):
        self.__square = (self._length / 2) * self._height
        return self.__square

    def set_3perimeter(self):
        self.__perimeter = self._length + 2 * (math.sqrt((self._length / 2) ** 2 + self._height ** 2))
        return self.__perimeter


class Mixin3D(Triangle, Foursquare):
    """Класс-примесь для инициации вычисления площади плоских фигур"""
    def figure_square(self, i_figure):
            if i_figure == 'Foursquare':
                return Foursquare.set_4square(self)
            else:
                return Triangle.set_3square(self)


class Pyramid(Mixin3D):
    """
    Класс Пирамида. Родительский класс Mixin3D
    Parameters:
        length (int): длина стороны основания
        height (int): высота боковой поверхности
    Attributes:
        self.figure (str): название фигуры
        self.__sum_square (float): суммарная площадь поверхностей
        self.figures (list): список плоских фигур, из которых состоит поверхность фигуры
      """
    def __init__(self, length: int, height: int) -> None:
        self.figure = 'Пирамида'
        self._length = length
        self._height = height
        self.__sum_square = 0
        self.__perimeter = None
        self.figures = ['Foursquare', 'Triangle', 'Triangle', 'Triangle', 'Triangle']
        for i_figure in self.figures:
            self.__sum_square += super().figure_square(i_figure)
        self.__square = self.__sum_square

    def __str__(self):
        return f'{self.figure} с длиной основания {self._length}, высотой боковой поверхности {self._height}, ' \
               f' и площадью поверхности {self.__square}'


class Cube(Mixin3D):
    """
    Класс Куб. Родительский класс Mixin3D
        Parameters:
        length (int): длина стороны грани
    Attributes:
        self.figure (str): название фигуры
        self.__sum_square (float): суммарная площадь поверхностей
        self.figures (list): список плоских фигур, из которых состоит поверхность фигуры
      """
    def __init__(self, length: int) -> None:
        self.figure = 'Куб'
        self._length = length
        # self._height = height
        self.__sum_square = 0
        self.__perimeter = None
        self.figures = ['Foursquare', 'Foursquare', 'Foursquare', 'Foursquare', 'Foursquare', 'Foursquare']
        for i_figure in self.figures:
            self.__sum_square += super().figure_square(i_figure)
        self.__square = self.__sum_square

    def __str__(self):
        return f'{self.figure} с длиной основания {self._length}, ' \
               f' и площадью поверхности {self.__square}'

my_square = Foursquare(length=5)
print(my_square)
print(my_square.square)

my_triangle = Triangle(length=5, height=3)
print(my_triangle)
print(my_triangle.square * 4)

my_pyramid = Pyramid(length=5, height=3)
print(my_pyramid)
print()
my_pyramid = Cube(length=5)
print(my_pyramid)