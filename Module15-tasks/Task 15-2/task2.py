numbers =[]
amount_numbers = int(input('Введите кол-во чисел в списке: '))
for i in range(amount_numbers):
    print('Введите', i + 1, end = ' ')
    number = int(input('число '))
    numbers.append(number)

K = int(input('\nВведите делитель: '))
print()
summ_num = 0
for i_number in range(amount_numbers):
    if numbers[i_number] % K == 0:
        summ_num += i_number
        print('Индекс числа', numbers[i_number], end = ': ')
        print(i_number)

print('Сумма индексов: ', summ_num)