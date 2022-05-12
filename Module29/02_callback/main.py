import functools


def callback(path):
    def application(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
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