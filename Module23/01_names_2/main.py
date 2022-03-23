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
            # TODO "BaseException" довольно обширное исключение, стоит использовать одно из "Exception"
            #  Например - ValueError
            #  Статья описывающая иерархию исключений
            #   https://tatyderb.gitbooks.io/python-express-course/content/chapter_exception/3_tree.html
            #  BaseException никогда не используют - это про родитель самый главный наследник из древа

            raise BaseException
        else:
            total_sym += line_len


except FileNotFoundError:
    print('Указанный файл не существует')
except BaseException:
    print('Длина строки {string} меньше 3-х'.format(string=line_count))
finally:
    print('Общая длина строк:', total_sym, 'символов')
