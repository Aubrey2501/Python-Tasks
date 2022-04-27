from typing import Callable, Any
import functools

COUNTER = dict()


def counter(func: Callable) -> Callable:
    """Декоратор. Считает и выводит количество вызовов функции"""
    @functools.wraps(func)
    def wrapped_func(*args: Any, **kwargs: Any) -> Any:
        if func.__name__ not in COUNTER:
            COUNTER[func.__name__] = 1
        else:
            COUNTER[func.__name__] += 1
        print(f'Функция {func.__name__}. Вызовов: {COUNTER[func.__name__]}')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@counter
def test():
    print('<Тут что-то происходит...>')


test()
test()
test()

