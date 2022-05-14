import functools
import time
from datetime import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Функция:\t {func.__name__}, аргументы:\t {args}, именованные аргументы:\t {kwargs}')
        return result
    return wrapper


def for_all_methods_timer(decorator):
    @functools.wraps(decorator)
    def wrapper(cls):
        for i_method_name in dir(cls):
            if not i_method_name.startswith('__'):
                i_method = getattr(cls, i_method_name)
                cur_method = decorator(i_method)
                setattr(cls, i_method_name, cur_method)
        return cls
    return wrapper


@for_all_methods_timer(logging)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        result = 0
        number = 100
        for _ in range(number + 1):
            result += sum(i_num ** 2 for i_num in range(1, self.max_num + 1))
        return result

    def cubes_sum(self, number) -> int:
        result = 0
        for _ in range(number):
            result += sum(i_num ** 3 for i_num in range(1, self.max_num + 1))
        return result


my_func = Functions(max_num=1000)
print(my_func.squares_sum())
print(my_func.cubes_sum(number=100))