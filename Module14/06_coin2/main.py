import math
print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
rad = float(input('Введите радиус: '))

if math.sqrt(x ** 2 + y ** 2) <= rad:
    print('\nМонетка где-то рядом')
else:
    print('Монетки в области нет')

# зачет!
