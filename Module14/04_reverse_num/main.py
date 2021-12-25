def reverse(number):
    whole_part = number // 1
    fract_part = number % 1
    count = 0

    while round(fract_part % 1, 2) > 0:
        fract_part *= 10
        count += 1
    fract_part //= 1

    rev_whole = reverse_number(whole_part)
    rev_fract_part = reverse_number(fract_part)
    rev_fract = rev_fract_part / 10 ** count
    rev_number = rev_whole + rev_fract
    return(rev_number)

def reverse_number(number):
    new_number = 0
    while number != 0:
        next_num = number % 10
        number //= 10
        new_number *= 10
        new_number += next_num
    return(new_number)


N = float(input('Введите число N: '))
K = float(input('Введите число K: '))
N_rev = reverse(N)
K_rev = reverse(K)

print('\nПервое число наоборот:', N_rev)
print('Второе число наоборот:', K_rev)
print('Сумма:', N_rev + K_rev)

