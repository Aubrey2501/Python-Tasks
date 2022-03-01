def my_sum(*args, **kwargs):
    i_sum = kwargs['sum_n']
    for argument in args:
        if isinstance(argument, int):
            i_sum += argument
            kwargs['sum_n'] = i_sum
        else:
            for item in argument:
                i_sum = my_sum(item, sum_n=i_sum)
    return i_sum



print('sum([[1, 2, [3]], [1], 3])')
print('Ответ:', my_sum([[1, 2, [3]], [1], 3], sum_n=0)) # 10

print('sum(1, 2, 3, 4, 5)')
print('Ответ:', my_sum(1, 2, 3, 4, 5, sum_n=0)) # 15