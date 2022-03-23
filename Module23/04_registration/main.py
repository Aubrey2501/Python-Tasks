with open('registrations.txt', 'r', encoding='utf-8') as file:
    out_file = open('registrations_good.log', 'w')
    err_file = open('registrations_bad.log ', 'w')

    for i_line in file:
        try:
            str_lst = i_line.split(' ')
            if len(str_lst) != 3:
                raise IndexError
            if not str_lst[0].isalpha():
                raise NameError
            if '@' not in str_lst[1] or '.' not in str_lst[1]:
                raise SyntaxError
            if not (10 < int(str_lst[2]) < 99):
                raise ValueError
            out_file.write(i_line)

        except IndexError:
            err_file.write(i_line.replace('\n', '') + '   - НЕ присутствуют все три поля\n')
        except NameError:
            err_file.write(i_line.replace('\n', '') + '   - поле имени содержит НЕ только буквы\n')
        except SyntaxError:
            err_file.write(i_line.replace('\n', '') + '   - поле емейл НЕ содержит @ и .(точку)\n')
        except ValueError:
            err_file.write(i_line.replace('\n', '') + '   - поле возраст НЕ является числом от 10 до 99\n')
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
