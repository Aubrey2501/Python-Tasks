phonebook = dict()

def ins_phone(phonebook):
    while True:
        print('\nДобавление контакта в телефонную книгу')
        name = input('Имя: ')
        surname = input('Фамилия: ')
        tel_number = input('Номер телефона: ')
        if not tel_number.isdigit():
            print('Ошибка ввода. Повторите!')
            continue
        else:
            break
    if (name, surname) not in phonebook:
        phonebook[(name, surname)] = tel_number
    else:
        for i_person in phonebook:
            if (name, surname) in phonebook:
                print('Контакт уже есть в телефонном справочнике:')
                print(name, surname, phonebook[(name, surname)])
                choise = input('Заменить номер контакта? (1)-Да, (0)-Нет: ')
                if choise == '1':
                    phonebook[(name, surname)] = tel_number
                    break
                elif choise == '0':
                    break
                else:
                    print('Ошибка ввода!')
    print('\nТелефонная книга:')

    for i_person in phonebook:
        print(i_person[0], i_person[1], ':', phonebook[i_person])

    return phonebook


def find_phone(phonebook):
    print('\nПоиск контакта в телефонной книге')
    surname = input('Фамилия: ').lower()
    found = False
    for (i_name, i_surname) in phonebook:
        if i_surname.lower()  == surname:
            print(i_name, i_surname, phonebook[(i_name, i_surname)])
            found = True
    if not found:
        print('Не найдено')

while True:
    print('\nВведите номер действия:')
    print(' 1. Добавить контакт')
    print(' 2. Найти человека ')
    print(' 0. Выход')
    act_choise = input()

    if act_choise == '1':
        phonebook = ins_phone(phonebook)
    elif act_choise == '2':
        find_phone(phonebook)

    elif act_choise == '0':
        break
    else:
        print('\nОшибка ввода! Повторите')
        continue





