string = input('Введите строку: ')
symbol = input('Введите доп. символ: ')
list_string = list(string)
double_str = [letter * 2 for letter in list_string]
double_str_plus = [letter * 2 + symbol for letter in list_string]
print('Список удвоенных символов:', double_str)
print('Склейка с доп.символом:', double_str_plus)