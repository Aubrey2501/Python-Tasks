from abc import ABC
import math


class MyMath(ABC):
    """ Абстрактный класс MyMath для вычисления математических величин  """

    @classmethod
    def circle_len(cls, radius) -> float:
        cls.radius = radius
        return 2 * cls.radius * math.pi

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        cls.radius = radius
        return math.pi * cls.radius ** 2

    @classmethod
    def cube_volume(cls, length: float) -> float:
        cls.length = length
        return cls.length ** 3

    @classmethod
    def sphere_area(cls, radius):
        cls.radius = radius
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(length=12.5)
print(res_1)
print(res_2)
print(res_3)