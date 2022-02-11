
import random
set1 = {1, 2, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 26, 27, 29}
set2 = {1, 5, 7, 8, 9, 11, 12, 13, 15, 16, 19, 21, 22, 23, 24, 29, 30}

print('\nМинимальный элемент 1-го множества: ', min(set1))
print('Минимальный элемент 2-го множества: ', min(set2))

set1_rand = random.randint(100, 200)
set2_rand = random.randint(100, 200)
print('\nСлучайный элемент 1-го множества: ', set1_rand)
print('Случайный элемент 1-го множества: ', set2_rand)

set1.remove(min(set1))
set2.remove(min(set2))

set1.add(set1_rand)
set2.add(set2_rand)

print('\nОбъединение множеств: ', set1.union(set2))
print('Пересечение множеств: ', set1.intersection(set2))
print('Элементы, входящие в nums_2, но не входящие в nums_1:', set2.difference(set1))
