from typing import Callable, Any


def do_twice(func: Callable) -> Any:
    def wrapped_func(*args, **kwargs) -> Any:
        for _ in range(2):
            func(*args, **kwargs)
    return wrapped_func


@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')