import random


def file_errors(file):
    with open(file, 'r') as errors_file:
        error_lst = []
        for line in errors_file:
            error_lst.append(line.split(' ')[0])
        return error_lst


try:
    with open('result.txt', 'w') as out_file:
        error_lst = file_errors('errors.txt')
        sum_points = 0
        while sum_points < 777:
            points = int(input('Введите число: '))
            # TODO Магия весов не иначе, почему просто не кидать кубик и сравнивать с 13?
            #  dice = randint(1, 13)
            #  if dice == 13:
            #      выкидываем исключение

            dice = random.randint(1, 13)
            if dice == 13:
                raise ValueError
            else:
                out_file.write(str(points) + '\n')
                sum_points += points

except ValueError:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
finally:
    out_file.close()

# зачет!
