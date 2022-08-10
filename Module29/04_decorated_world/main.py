import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор, передающий в функцию аргументы"""

    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """Декоратор - шаблон"""
    functools.wraps(func)

    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор:', func_args, func_kwargs)

        # меняем параметр, передаваемый в функцию decorated_function
        func_kwargs1 = dict()
        for i_key, i_val in func_kwargs.items():
            if isinstance(i_val, int):
                i_val += 100
            func_kwargs1[i_key] = i_val

        return func(*func_args, **func_kwargs1)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text=None, num=None) -> None:
    print("Привет", text, num)


decorated_function("Юзер", num=101)

# зачет!

