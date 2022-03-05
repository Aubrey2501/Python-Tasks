def calculating_math_func(data, data_dct):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    data_dct[data] = result
    # return result


data_dct = dict()
while True:
    data = int(input('Введите входные данные: '))
    if data not in data_dct:
        calculating_math_func(data, data_dct)

    print('Результат:', data_dct[data])

# зачет!
