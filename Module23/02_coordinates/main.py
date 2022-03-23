import random

# TODO В функциях сразу проверяйте когда будет деление на ноль, и кидайте исключение вместе с сообщением.
#  raise ZeroDivisionError('Ошибка в функции №1')
def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return (x / y)


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return (y / x, err)


# TODO Открывайте сразу все файлы в одном контекстном менеджере
#  with open(....),
#        open(....)
try:
    err = ''
    file = open('coordinates.txt', 'r')
    for line in file:
        # TODO Добавьте обработчик и ловите конкретные исключения.
        #  В "try" сразу делаем все действия
        #  В "except" ловим исключение с присвоением переменной - except ZeroDivisionError as error
        #  Тогда строку с сообщением можно будет взять из переменной "error"
        nums_list = line.split()
        err = 'с первой фукцией'
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        err = 'со второй фукцией'
        res2, err = f2(int(nums_list[0]), int(nums_list[1]))
        err = ''
        number = random.randint(0, 100)
        my_list = sorted([res1, res2, number])
        file_2 = open('result.txt', 'w')
        file_2.write(' '.join(str(my_list)))

except FileNotFoundError:
    print('Файл не найден')
except Exception:
    print('Что-то пошло не так', err)
else:
    file.close()
    file_2.close()
