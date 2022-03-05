site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find_key(struct, key, product):
    for sub_key, sub_struct in struct.items():
        if key in sub_struct:
            result_lst = sub_struct.split()
            result_lst[result_lst.index(key)] = product
            struct[sub_key] = ' '.join(result_lst)
            break
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, product)


def print_site(site, pos):
    for i_key, item in site.items():
        print(pos * ' ', end="'")
        print(i_key, end="': ")
        if isinstance(item, dict):
            print('{')
            new_pos = pos + 8
            print_site(item, new_pos)
        else:
            print(" ", end="'")
            print(item, end="'\n")
    print((pos - 1) * ' ', '}')


key = 'iphone'
product = ''
while True:
    product = input('\nВведите название продукта для нового сайта: ')
    if product == 'end':
        break
    find_key(site, key, product)

    print('Сайт для', product, ':')
    print('site = {')
    print_site(site, 8)

    key = product

# зачет!
