import random

# TODO В функциях сразу проверяйте когда будет деление на ноль, и кидайте исключение вместе с сообщением.
#  raise ZeroDivisionError('Ошибка в функции №1')
def f(x, y):
    error = ''
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError('Ошибка в функции №1')
        return 0
    else:
        return (x / y)


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError('Ошибка в функции №2')
        return 0
    else:
        return (y / x)


# TODO Открывайте сразу все файлы в одном контекстном менеджере
#  with open(....),
#        open(....)
try:
    with open('coordinates.txt', 'r') as file, open('result.txt', 'w') as file_2:
        for line in file:
            # TODO Добавьте обработчик и ловите конкретные исключения.
            #  В "try" сразу делаем все действия
            #  В "except" ловим исключение с присвоением переменной - except ZeroDivisionError as error
            #  Тогда строку с сообщением можно будет взять из переменной "error"
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            file_2.write(' '.join(str(my_list)))

except FileNotFoundError:
    print('Файл не найден')
except ZeroDivisionError as error:
    print(error)
except IndexError:
    print('Координаты:', ' '.join(nums_list), ' - ошибка данных')
else:
    file.close()
    file_2.close()
