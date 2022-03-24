def test_line(line):
    line = line.replace('\n', '')
    str_lst = line.split(' ')
    if len(str_lst) != 3:
        raise ChildProcessError('- в строке НЕ присутствуют все три поля')
    if not str_lst[0].isalpha():
        raise ChildProcessError('- поле имени содержит НЕ только буквы')
    elif '@' not in str_lst[1] or '.' not in str_lst[1]:
        raise ChildProcessError('- поле е-mail НЕ содержит `@` и `.`(точку)')
    elif not str_lst[2].isdigit() or not (10 < int(str_lst[2]) < 99):
        raise ChildProcessError('- поле ВОЗРАСТ не является числом от 10 до 99')
    else:
        return '{name:<15}{mail:<30}{age}\n'.format(name=str_lst[0], mail=str_lst[1], age=str_lst[2])


with open('registrations.txt', 'r', encoding='utf-8') as file, \
    open('registrations_good.log', 'w') as out_file, \
    open('registrations_bad.log ', 'w') as err_file:

    for i_line in file:
        try:
            # line = i_line.replace('\n', '')
            out_string = test_line(i_line)
            out_file.write(out_string)

        except ChildProcessError as error:
            i_line = i_line.replace('\n', '')
            err_file.write(f'{i_line:<40}{error}\n')


# TODO Логику нужно переработать.
#  1 - сделайте функцию, которая обрабатывает строку
#  Функция проверяет строку.
#  Если одно из условий не выполнено
#    - выбрасывает исключение сразу с сообщением ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
#  В другом случае возвращает строку для записи - f'{name:<15} {mail:<30} {age}\n'
#  2 - Основной цикле, где сразу в одном "with" открываем 3 файла.
#  with open(....),
#        open(....)
#  И ловим все исключения в одном блоке "except" - except (исключение_1, исключение_2) as error
#  И в переменную "error" попадает текущее, с которым уже делаем то что нужно
#  .
#  Касаемо форматирования строк поможет разобраться данный пример и статья https://clck.ru/dZHwm
#  print(f'|{"текст":<30}|') #  По левому краю
#  print(f'|{"текст":>30}|') #  По правому краю
#  print(f'|{"текст":^30}|') #  По центру
#  print(f'|{"текст":*^30}|') #  По центру с заполнением оставшихся символов звездочками "*"
#  Число после знаков "<,>,^" означение количество зарезервированного место под строку.
