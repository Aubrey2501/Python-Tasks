number = int(input('Введите целое число: '))
q_dict = dict()
for i_num in range(1, number + 1):
    q_dict[i_num] = i_num ** 2

print(q_dict)
