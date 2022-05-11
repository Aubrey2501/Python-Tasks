import functools
from typing import Callable
from functools import wraps

user_permissions = ['admin']


def check_permission(func):
    @functools.wraps
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('wrapping')
        return result
    return wrapper

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
