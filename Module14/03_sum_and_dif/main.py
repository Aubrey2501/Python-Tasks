def summ_num(N):
    summ = 0
    while N != 0:
        summ += N % 10
        N //= 10
    return (summ)


def vol_num(N):
    vol = 0
    while N != 0:
        N //= 10
        vol += 1
    return (vol)


N = int(input('Введите число N: '))
summ = summ_num(N)
vol = vol_num(N)
print('\nСумма цифр:', summ)
print('Кол-во цифр в числе:', vol)
print('Разность суммы и кол-ва цифр:', summ - vol)

# зачет!
