A = int(input('Введите число A: '))
B = int(input('Введите число B: '))
squears = [x ** 2 for x in range(A, B + 1)]
qubs = [x ** 3 for x in range(A, B + 1)]
print('Список квадратов чисел в диапазоне от', A, 'до', B, ':', squears)
print('Список кубов чисел в диапазоне от', A, 'до', B, ':', qubs)