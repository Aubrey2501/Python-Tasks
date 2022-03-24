try:
    total_sym = 0
    line_count = 0
    inp_file = open('people.txt', 'r')
    for i_line in inp_file:
        line_count += 1
        line_len = len(i_line)
        if i_line.endswith('\n'):
            line_len -= 1
        if line_len < 3:
            raise ValueError
        else:
            total_sym += line_len


except FileNotFoundError:
    print('Указанный файл не существует')
except ValueError:
    print('Длина строки {string} меньше 3-х'.format(string=line_count))
finally:
    print('Общая длина строк:', total_sym, 'символов')

# зачет!
