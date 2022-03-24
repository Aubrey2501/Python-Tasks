# encoding: utf-8
try:
    inp_file = open('people.txt', 'r')
    name_lst = inp_file.read().split('\n')
    inp_file.close()
    sum_sym = 0

    for i in range(len(name_lst)):
        if len(name_lst[i]) < 3:
            raise BaseException('Количество символов в строке {num} меньше 3'.format(num=i))
        else:
            sum_sym += len(name_lst[i])

    print('Общее количество символов:', sum_sym)

except FileNotFoundError:
    print('Файл не найден')


