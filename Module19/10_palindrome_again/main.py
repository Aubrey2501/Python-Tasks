# TODO здесь писать код
string = input('Введите строку: ')
sym_dict = {symbol: string.count(symbol) for symbol in string}

odds = 0
for number in sym_dict.values():
    if number % 2 != 0:
        odds += 1
if odds > 1:            # Если нечётных букв больше чем одна
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

