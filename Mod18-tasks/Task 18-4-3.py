string = input('Введите строку: ')
count_list = [symbol.isupper() for symbol in string]
# print(count_list)

if count_list.count(True) >= count_list.count(False):
   print(string.upper())
else:
    print(string.lower())