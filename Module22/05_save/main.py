import os

def write_file(path, text):
    out_file = open(path, 'w')
    out_file.write(text)
    out_file.close()

text = input('Введите строку: ')
while True:
    print('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):')
    path_lst = input().split(' ')
    # path_lst = 'C: Users Евгений PycharmProjects Python_Basic Module22 05_save'.split()
    path = ''
    for i_elem in path_lst:
        path += (i_elem + '/')
    if os.path.exists(path):
        break
    else:
        print('Путь к файлу не существует. Повторите ввод')

while True:
    file_name = input('\nВведите имя файла: ')
    file_name += '.txt'
    file_path = path + file_name
    if os.path.exists(file_path):
        answer = input('Вы действительно хотите перезаписать файл? Y/N: ').upper()
        if answer == 'Y':
            print('Файл успешно перезаписан!')
            write_file(file_path, text)
            break
    else:
        print('Файл успешно сохранён!')
        write_file(file_path, text)
        break