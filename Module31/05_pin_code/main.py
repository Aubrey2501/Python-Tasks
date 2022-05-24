import itertools


def rattle_lock(lock_code: tuple) -> str:
    digits = range(10)
    for item in itertools.product(digits, repeat=4):
        if item == lock_code:
            return 'Замок вскрыт. Код: {}-{}-{}-{}'.format(item[0], item[1], item[2], item[3])


my_code = (9, 8, 7, 9)
print(rattle_lock(my_code))