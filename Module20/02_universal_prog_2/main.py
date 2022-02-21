data = [
    'О Дивный Новый мир!',
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ('a', 'b', 'c', 'd'),
    {'bcad': 1, 4: 2, 5: 'abc', 6: 4, 7: 'a'}]


def crypto(data):
    return scrypt(data)


def scrypt(x_data):
    if not isinstance(x_data, dict):
        list_ind = [value for index, value in enumerate(x_data) if is_prime(index)]
    else:
        list_ind = [{value: x_data[value]} for index, value in enumerate(x_data) if is_prime(index)]
    return list_ind


def is_prime(num):
    if num in (0, 1):
        return False
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True


for i_data in data:
    print(crypto(i_data))

# зачет!
