import datetime
from typing import Callable
import functools

LOG_File = []


def debug(func: Callable) -> Callable:
    """Декоратор. При каждом вызове декорируемой функции выводит её имя (вместе со всеми передаваемыми аргументами),
     а затем — какое значение она возвращает."""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> str:
        print('\nВызывается: {func}'.format(
            func=func.__name__), end='(')

        if args:
            print(repr(args).strip("()"), end='')
        if kwargs:
            print(f' {repr(kwargs).strip("{}").replace(":", "=")}', end='')

        print(')')

        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула значение '{result}'")
        print(result)
        return result
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачет!
