import functools
from typing import Callable


def callback(path: str) -> Callable:
    """Декоратор - функция обратного вызова
       Args: path: аргумент для проверки условия запуска передаваемой функции"""
    def application(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            print(path, args, kwargs)
            if path == args[0]:
                return func
            return False
        return wrapped
    return application


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {'//': example('//')}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')