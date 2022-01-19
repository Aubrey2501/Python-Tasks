def input_list(num_list, word):
    list_n = []
    for i in range(num_list):
        print('Введите', i + 1, 'число для', word, end=' ')
        number_i = int(input('списка: '))
        list_n.append(number_i)
    return (list_n)


list_1 = input_list(3, 'первого')
list_2 = input_list(7, 'второго')
print('\nПервый список:', list_1)
print('Второй список:', list_2)
list_1.extend(list_2)
list_new = []
# TODO Сравнение излишние, достаточно - while list_1
while list_1 != []:
    number = list_1[0]
    list_new.append(number)
    count_num = list_1.count(number)
    for _ in range(count_num):
        list_1.remove(number)

print('Новый первый список с уникальными элементами:', list_new)

# зачет!
