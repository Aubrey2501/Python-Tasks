# orders_list = ['Иванов Пепперони 1',
# 'Петров Де-Люкс 2', 'Иванов Мясная 3', 'Иванов Мексиканская 2', 'Иванов Пепперони 2', 'Петров Интересная 5']

orders_dict = dict()
num_orders = int(input('Введите кол-во заказов: '))
orders_dict = dict()
for i in range(num_orders):
    print(i + 1, end='-й ')
    order = input('заказ: ')
    # order = orders_list[i]         # test
    # print('заказ: ', order)         # test

    l_order = order.split()
    client = l_order[0]
    pizza = l_order[1]
    amount = int(l_order[2])

    if client not in orders_dict:
        orders_dict[client] = {pizza: amount}
    else:
        if pizza not in orders_dict[client]:
            orders_dict[client] |= {pizza: amount}
        else:
            orders_dict[client][pizza] += amount

print()
for client in sorted(orders_dict.keys()):
    print(client)
    for order in orders_dict[client].keys():
        print('      ', order, ':', orders_dict[client][order])

# зачет!
