string = input('Введите строку: ')
set_str = set(string)
string_num = {sym for sym in set_str if '0' <= sym <= '9'}
string_new = ''.join(sorted(string_num))
print('Уникальные цифры строки:', string_new)

