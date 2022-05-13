import functools
from typing import Callable, Optional


class Singleton:
    """Класс декоратор - синглтон"""
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
        self.id = 0

    def __call__(self, *args, **kwargs) -> Optional[Callable]:
        if self.num_calls == 0:
            self.num_calls = 1
            self.id = id(self.func)
        return self.func


@Singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)