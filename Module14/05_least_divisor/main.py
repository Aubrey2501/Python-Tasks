n = int(input('Введите число n > 1: '))
for count in range(n, 1, -1):
    if n % count == 0:
        min_divisor = count
print("Наименьший делитель:", min_divisor)
