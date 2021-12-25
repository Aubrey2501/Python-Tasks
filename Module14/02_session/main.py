
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x2 - x1
y_diff = y2 - y1
if x1 == x2:
    k = 1
else:
    k = y_diff / x_diff
b = y1 - k * x1

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, "* x +", b)