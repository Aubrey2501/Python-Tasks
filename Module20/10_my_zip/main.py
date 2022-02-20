string = 'abcd'
a_tuple = (10, 20, 30, 40)
print('Строка:',  string)
print('Кортеж чисел:', a_tuple)

new_tuple = zip(string, a_tuple)
print(new_tuple)
for i_pare in new_tuple:
    print(i_pare)