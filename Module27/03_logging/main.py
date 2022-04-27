import datetime
from typing import Callable
import functools

LOG_File = []


def logging(func: Callable) -> Callable:
    """Декоратор. Логирует функцию и заносит ошибки в файл"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            LOG_File.append('{time}: {func} {docs}'.format(
                time=datetime.datetime.now(), func=func.__name__, docs=func.__doc__))
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            with open('function_errors.log', 'a') as error_file:
                err_log = '{time}: {func} - {error}\n'.format(
                    time=datetime.datetime.now(), func=func.__name__, error=str(error))
                error_file.write(err_log)
    return wrapped_func


@logging
def say_hello(name: str, repeats: int) -> str:
    """
    Функция вывода на экран приветствия заданное количество раз
    Args:
        name (str): Имя в приветствии
        repeats (int): Количество повторений
    Returns:
        result (str): текст приветствия
    """
    result = ''
    for _ in range(repeats):
        result += 'Привет {}!\n'.format(name)
    return result


@logging
def say_goodbye(name: str, repeats: int) -> str:
    """
    Функция вывода на экран прощания заданное количество раз
    Args:
        name (str): Имя в прощании
        repeats (int): Количество повторений
    Returns:
        result (str): текст прощания
    """
    result = ''
    for _ in range(repeats):
        result += 'Пока, {}!\n'.format(name)
    return result


for _ in range(3):
    print(say_hello('Tom', repeats=1))
print(say_goodbye('Bob', repeats=3))

print(say_goodbye('Bob'))           # ошибка в позиционном аргументе

for i_elem in LOG_File:
    print(i_elem)


