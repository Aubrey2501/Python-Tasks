# Первая строка: abcd
# Вторая строка: cdab

str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')

flag = False
for i in range(len(str1)):
    if str1[i::] + str1[0:i:] == str2:
        print('Первая строка получается из второй со сдвигом', i)
        flag = True

if not flag:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')

# зачет!
