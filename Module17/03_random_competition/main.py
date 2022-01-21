# TODO здесь писать код
import random
list1 = [round(random.random() * 10, 2) for _ in range(20)]
list2 = [round(random.random() * 10, 2) for _ in range(20)]
list3 = [list1[i] if list1[i] > list2[i] else list2[i] for i in range(20)]
print('Первая команда:', list1)
print('Вторая команда:', list2)
print('Победители тура:', list3)
