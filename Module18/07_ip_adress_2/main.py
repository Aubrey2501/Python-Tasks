def is_error(symbol):
    flag = False
    if not symbol.isdigit():
        print(symbol, '- не целое число')
    elif int(symbol) > 255:
        print(symbol, 'превышает 255')
    else:
        flag = True
    return (flag)


correct = False
while not correct:
    ip_txt = input('\nВведите IP: ')
    ip_lst = ip_txt.split('.')

    if len(ip_lst) != 4:
        print('Адрес - это четыре числа, разделенные точками')
    else:
        for symbol in ip_lst:
            correct = is_error(symbol)
            if not correct:
                break

print('IP-адрес корректен')

# зачет!
