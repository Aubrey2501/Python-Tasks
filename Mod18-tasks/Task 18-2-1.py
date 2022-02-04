massage ='Здравствуйте, {client}! Ваш номер заказа: {order}. Приятного дня!'
clients_list = []
while True:
    client_name = input('Имя: ')
    if 'end' in client_name:
        break
    client_num = input('Номер заказа: ')
    clients_list.append([client_name, client_num])


for i_client in clients_list:
    i_massage = massage.format(client=i_client[0], order=i_client[1])
    print(i_massage)