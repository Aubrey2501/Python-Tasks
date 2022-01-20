A = int(input('Введите число A: '))
B = int(input('Введите число B: '))

list1 = [x for x in range(A, B + 1) if x % 2 == 0]
print(list1)