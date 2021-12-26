print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x2 - x1
y_diff = y2 - y1
# TODO Нужно проверить два условия, чтобы сразу вывести ответ.
#  1 - когда "x_diff" равен нулю, сразу выводим ответ точку "х1"
#  2 - когда "y_diff" равен нулю, сразу выводим ответ точку "у1"
#  Во всех остальных случаях делаем расчеты
#  Формула и ход решения отлично описан на сайте https://ru.onlinemschool.com/math/assistance/cartesian_coordinate/p_to_line/
if x1 == x2:
    k = 1
else:
    k = y_diff / x_diff
b = y1 - k * x1

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, "* x +", b)
