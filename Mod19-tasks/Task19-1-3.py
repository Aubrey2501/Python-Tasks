dict_tel = dict()
while True:
    print('\nТекущие контакты на телефоне:')
    for i_contact in dict_tel:
        print(i_contact, ':', dict_tel[i_contact])

    name = input('\nВведите имя: ')
    if name in dict_tel:
        print('Ошибка: такое имя уже существует.')
        continue
    elif name == 'end':
        break
    else:
        tel_number = int(input('Введите номер телефона: '))
        dict_tel[name] = tel_number


