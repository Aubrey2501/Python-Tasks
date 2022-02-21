import random
import string
letters = list('абвгдеёжзиклмнопрстуфхцчщьъэюя')
letters_dict1 = dict()
letters_dict2 = dict()

list1 = [random.choice(letters) for i in range(10)]
list2 = [random.choice(letters) for i in range(10)]
print('Первый список:', list1)
print('Второй список:', list2)
# for index, symbol in enumerate(list1):
letters_dict1 = {index: symbol for index, symbol in enumerate(list1)}
letters_dict2 = {index: symbol for index, symbol in enumerate(list2)}
print('\nПервый словарь:', letters_dict1)
print('Второй словарь:', letters_dict2)