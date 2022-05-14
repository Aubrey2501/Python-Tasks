import functools
from typing import Callable


def check_permission(user: str = '') -> Callable:
    """Декоратор для установления прав пользователя на вызываемые функции"""
    def action(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user not in user_permissions:
                    raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
                result = func(*args, **kwargs)
                return result
            except PermissionError as err:
                print(err)
                return None
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


# зачет!
