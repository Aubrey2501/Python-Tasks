import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return (x / y)

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return (y / x, err)

try:
    err = ''
    file = open('coordinates.txt', 'r')
    for line in file:
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
