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

