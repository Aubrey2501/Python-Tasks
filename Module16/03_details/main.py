shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
component = input('Название детали: ')
count = 0
summ_price = 0
for detail, price in shop:
    if detail == component:
        count += 1
        summ_price += price
print('\nКол-во деталей -', count)
print('Общая стоимость -', summ_price)
