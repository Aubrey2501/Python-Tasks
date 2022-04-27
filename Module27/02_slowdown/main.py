from typing import Callable, Any, Tuple
import time


def slower(func: Callable) -> Any:
    """Декоратор, замедляющий функцию на 2 секунды"""
    def wrapped_func(*args: Any, **kwargs: Any) -> Any:
        time.sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@slower
def sqrt_gen(num: int) -> str:
    """Функция, возвращающая квадрат и куб числа"""
    sqrt_num = num ** 2
    cube_num = num ** 3
    result = f'{num} ** 2 = {sqrt_num:>2};  {num} ** 3 = {cube_num}'
    return result


for i_num in range(1, 11):
    print(sqrt_gen(i_num))


