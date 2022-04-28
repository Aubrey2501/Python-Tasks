from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Any:
    """Декоратор, задающий вопрос и выводящий ответ"""
    @functools.wraps(func)
    def wrapped_func(*args: Any, **kwargs: Any) -> Callable:
        question = input('Как дела? ')
        print('А у меня не очень')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

# зачет!
