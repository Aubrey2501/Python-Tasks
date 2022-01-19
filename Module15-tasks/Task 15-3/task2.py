S = input('Введите строку символов: ')
pos = int(input('Введите номер позиции: '))
S_list = list(S)
sym = S_list[pos - 1]
prev_sym = S_list[pos - 2]
post_sym = S_list[pos]
equal = 0
print('\nСимвол слева:', prev_sym)
print('Символ справа:', post_sym)
if prev_sym == post_sym== sym:
    print('Есть два совпалдения')
elif post_sym == sym or prev_sym == sym:
    print('Есть ровно один такой же символ')
else:
    print('Совпадений нет')

