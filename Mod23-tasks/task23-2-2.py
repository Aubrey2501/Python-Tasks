# This Python file uses the following encoding: utf-8
file_name = 'ages.txt'
try:
    inp_file = open(file_name, encoding='utf-8')
except IsADirectoryError:
    print('Ожидался файл, но это директория')
else:
    file_lst = inp_file.read().split('\n')
    inp_file.close()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
try:
    out_lst = [alphabet[i] + ': ' + str(file_lst[i]) for i in range(len(file_lst))]
except TypeError or ValueError:
    print('Неверный тип данных и/или некорректное значение')
else:
    print(out_lst)
try:
    out_file = open('result.txt', 'w')
except FileExistsError:
    print('Попытка создания файла или директории, которая уже существует')
else:
    out_file = open('result.txt', 'a')
    for i_elem in out_lst:
        out_file.write(i_elem)
    out_file.close()