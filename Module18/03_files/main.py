# TODO здесь писать код

err_list = list('@№$%^&*()')
while True:
    file_name = input('\nНазвание файла: ')
    is_name_error = [True if file_name.startswith(symbol) else False for symbol in err_list]

    if is_name_error.count(True) != 0:
        print('Ошибка: название начинается на один из специальных символов')
    elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('Файл назван верно.')
        break



