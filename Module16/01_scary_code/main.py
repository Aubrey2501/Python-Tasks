a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
num_5 = a.count(5)
print('Кол-во цифр 5 при первом объединении:', num_5)
for i in range(num_5):
    a.remove(5)
a.extend(c)
num_3 = a.count(3)
print('Кол-во цифр 3 при втором объединении:', num_3)
print('Итоговый список:', a)
