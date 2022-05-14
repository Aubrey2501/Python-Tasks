from typing import Callable, Any, Optional
import time
import functools


def slower_for_secs(_func: Optional[Callable] = None, *, num_seconds: int = 1) -> Callable:
    def slower(func: Callable) -> Any:
        """Декоратор, замедляющий функцию на 2 секунды"""
        @functools.wraps(func)
        def wrapped_func(*args: Any, **kwargs: Any) -> Any:
            time.sleep(num_seconds)
            result = func(*args, **kwargs)
            return result
        return wrapped_func
    if _func is None:
        return slower
    return slower(_func)


@slower_for_secs(num_seconds=2)
def sqrt_gen(num: int) -> str:
    """
    Функция, возвращающая квадрат и куб числа
    Args:
        num: число
    Returns:
        result(str): текстовая строка для вывода квадрата и куба числа num
    """
    sqrt_num = num ** 2
    cube_num = num ** 3
    result = f'{num} ** 2 = {sqrt_num:>2};  {num} ** 3 = {cube_num}'
    return result


for i_num in range(1, 11):
    print(sqrt_gen(i_num))


