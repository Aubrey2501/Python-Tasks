N = int(input('Введите количество собак: '))
points = []
for dog in range(N):
    dogs_point = int(input('Кол-во очков: '))
    points.append(dogs_point)

maximum = points[0]
i_max = 0
minimum = points[0]
i_min = 0

for i in range(N):
    if maximum < points[i]:
        maximum = points[i]
        i_max = i
    if minimum > points[i]:
        minimum = points[i]
        i_min = i

print('Первоначальный список:', points)
points[i_max] = minimum
points[i_min] = maximum
print('Исправленный список:', points)