# path = input('Путь к файлу: ')
path = 'C:/user/docs/folder/new_file.txt'
disk = input('На каком диске должен лежать файл: ')
extention = input('Требуемое расширение файла: ')

if not path.startswith(disk):
    print('Ошибка диска!')
elif not path.endswith(extention):
    print('Ошибка типа файла!')
else:
    print('Путь корректен! Путь:', path)