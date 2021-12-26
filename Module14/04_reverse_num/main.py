
def reverse(str_number):
    str1 = str2 = ''
    flag = False
    for symbol in (str_number):
        if symbol == '.':
           flag = True
        elif flag:
            str2 = symbol + str2
        else:
            str1 = symbol + str1
    str_reverse = str1 + '.' + str2
    num_reverse = float(str_reverse)
    return num_reverse

N = float(input('Введите число N: '))
str_N = str(N)
N_rev = reverse(str_N)

K = float(input('Введите число K: '))
str_K = str(K)
K_rev = reverse(str_K)

print('\nПервое число наоборот:', N_rev)
print('Второе число наоборот:', K_rev)
print('Сумма:', N_rev + K_rev)

