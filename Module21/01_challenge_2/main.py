def print_num(num):
    print(num)
    num -= 1
    if num == 0:
        return 0
    else:
        print_num(num)


num = int(input('Введите num: '))
print_num(num)