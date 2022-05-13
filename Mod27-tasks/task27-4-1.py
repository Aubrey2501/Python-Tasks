from typing import Callable


def ingredients(func):
    def wrapped_func(*args, upper_ingr, lower_ingr, **kwargs):
        result = f'##{upper_ingr}##\n'
        result += func(*args, **kwargs)
        result += f'~~{lower_ingr}~~\n'
        return result
    return wrapped_func

def buns(func):
    def wrapped_func(*args, upper_bun, lower_bun, **kwargs):
        result = f'<{upper_bun}>\n'
        result += func(*args, **kwargs)
        result += f'<{lower_bun}>\n'
        return result
    return wrapped_func


@buns
@ingredients
def sandwich(sandwich_filling: str, **kwargs) -> str:
    return '--{}--\n'.format(sandwich_filling)



print(sandwich('Ветчина', upper_ingr='Помидоры', lower_ingr='Салат',
               upper_bun='/--------\ ', lower_bun='\_______/'))