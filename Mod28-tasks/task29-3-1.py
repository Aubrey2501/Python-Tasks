from typing import Callable, Any
from typing import Optional
import functools


def do_some_times(_func: Optional[Callable] = None, *, repeats: int = 2) -> Callable:
    def do_repeats(func: Callable) -> Any:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            for _ in range(repeats):
                func(*args, **kwargs)
        return wrapped_func
    if _func is None:
        return do_repeats
    return do_repeats(_func)


@do_some_times(repeats=4)
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')