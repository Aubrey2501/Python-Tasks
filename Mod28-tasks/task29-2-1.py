import time
from contextlib import contextmanager
from collections.abc import Iterator

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as err:
        print(err)
    finally:
        print(time.time() - start)


with timer() as t1:
    val_1 = 100 * 100 ** 1000000
    print('Первая часть')

with timer() as t2:
    val_2 = 200 * 200 ** 1000000
    val_2 += 'abc'
    print('Вторая часть')

with timer() as t3:
    val_3 = 300 * 300 ** 1000000
    print('Третья часть')