import random
rand_list = [random.randint(0, 100) for _ in range(10)]
print('Исходный список:', rand_list)

print('\nВариант 1:')
new_list = []
for i in range(0, len(rand_list), 2):
     pair = tuple(rand_list[i: i + 2:])
     new_list.append(pair)
print(new_list)

print('Вариант 2:')
new_list = [tuple(rand_list[i: i + 2:]) for i in range(len(rand_list) - 1) if i % 2 == 0]
print(new_list)

print('Вариант 3:')
list1 = [rand_list[i] for i in range(0, len(rand_list), 2)]
list2 = [rand_list[i] for i in range(1, len(rand_list), 2)]
new_list = list(zip(list1, list2))
print(new_list)

print('Вариант 4:')
dict_1 = {i: (rand_list[i], rand_list[i + 1]) for i in range(0, 9, 2)}
new_list = [pair for i, pair in dict_1.items()]
print(new_list)

print('Вариант 5:')
set_1 = {(rand_list[i], rand_list[i + 1]) for i in range(0, 9, 2)}
new_list = list(set_1)
print(new_list)

