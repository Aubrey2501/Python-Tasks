small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
while True:
    big_storage.update(small_storage)
    product = input('Введите название товара: ')
    if product == 'end':
        break
    print('Кол-во:', big_storage.get(product))