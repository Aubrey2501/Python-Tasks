import functools
from typing import Callable
from functools import wraps


def check_permission(user_permissions):
    def action(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            print('wrapping', args, kwargs)
            for i_permission in user_permissions:
                result = func(*args, **kwargs)
                print(result)
            return result
        return wrapped
    return action


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


user_permissions = ['admin']

delete_site()
add_comment()
