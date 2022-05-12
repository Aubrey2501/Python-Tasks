import functools
import time
from typing import Callable
from datetime import datetime


def timer(func: Callable, time_frm: str, cls_name: str) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print('- Запускается {}.{} Дата и время запуска:'.
              format(cls_name, func.__name__, datetime.utcnow()), datetime.utcnow().__format__(time_frm))
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print('- Завершение {}.{}. Время работы функции: {:.3f}s'.format(cls_name, func.__name__, runtime))
        return result
    return wrapper


def log_methods(frm=None):
    @functools.wraps(frm)
    def wrapper(cls):
        for i_method_name in dir(cls):
            if not i_method_name.startswith('__'):
                if frm is not None:
                    time_frm = '%' + ' %'.join(frm.split(' '))
                    time_frm = ':%'.join(time_frm.split(':'))
                else:
                    time_frm = ''
                i_method = getattr(cls, i_method_name)
                cur_method = timer(i_method, time_frm, cls.__name__)
                setattr(cls, i_method_name, cur_method)
        return cls
    return wrapper


@log_methods("b d Y- H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y- H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
