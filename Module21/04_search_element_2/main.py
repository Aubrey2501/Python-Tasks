site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth):
    result = None

    if key in struct:
        result = struct[key]
        return result

    if depth > 1:
        for sub_struct in struct.values():
            if key in sub_struct:
                result = sub_struct[key]
                return result

    if depth > 2:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth)
                if result:
                    break

    return result


user_key = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if answer == 'y':
    depth = int(input('Введите максимальную глубину: '))
else:
    depth = 99

value = find_key(site, user_key, depth)
if value:
    print(value)
else:
    print('Такого ключа в структуре нет')

# зачет!
