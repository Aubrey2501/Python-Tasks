def func_1(x):
    return x + 10


def func_2(func, number):
    result = func(number) * func(number)
    return result


print(func_2(func_1, number=9))