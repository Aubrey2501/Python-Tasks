import functools
import time
from typing import Callable, List
import math


def timer(func: Callable) -> Callable:
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения функции {}: {}s'.format(func.__name__, round(end - start, 5)))
        return result
    return wrapper


@timer
def is_prime(max_num: int) -> List[int]:
    prime_list = [2]
    for i_num in range(3, max_num + 1, 2):
        flag = True
        for i_division in range(3, i_num - 1):
            if i_num % i_division == 0:
                flag = False
        if flag:
            prime_list.append(i_num)
    return prime_list


@timer
def prime_comprehantion(max_num: int):
    result = [i_num for i_num in range(2, max_num + 1) if all(i_num % i_div for i_div in range(2, i_num - 1)) != 0]
    yield result


@timer
def prime_filter(max_num):
    result = filter(lambda i_num: i_num in range(2, max_num + 1)
                if all(i_num % i_div for i_div in range(2, i_num - 1)) != 0 else None,
                list(i_num for i_num in range(2, max_num + 1)))
    return result


print(is_prime(1000))
print()
print(list(prime_comprehantion(1000)))
print()
print(list(prime_filter(1000)))