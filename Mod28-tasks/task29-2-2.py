from contextlib import contextmanager
from collections.abc import Iterator
import os

@contextmanager
def in_dir(new_dir: str) -> Iterator:
    try:
        path = os.path.abspath(new_dir)
        os.chdir(path)
        print('Текущая директория: {}'.format(path))
    except FileNotFoundError as err:
        print(f'Указанной директории {path} не существует.\nТекущая директория: {os.path.abspath(os.path.curdir)}')
    finally:
        yield


with in_dir('C:\\intr'):
    print(os.listdir())
# Результат:
# <тут все папки из вашего диска C>