goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# TODO здесь писать код

for i_name in goods:
    i_code = goods[i_name]
    sum_number = sum({store[i_code][item]['quantity'] for item in range(len(store[i_code]))})
    sum_price = sum({store[i_code][item]['quantity'] * store[i_code][item]['price'] for item in range(len(store[i_code]))})
    print(i_name, '-', sum_number, 'шт, стоимость -', sum_price, 'руб.')

