S = input('Введите текст: ')
s_list = list(S)
print('Измененный текст:', end = ' ')
replace = 0
for symbol in (s_list):
    if symbol == ':':
        symbol = ';'
        replace += 1
    print(symbol, end = '')
print('\nВсего замен:', replace)

