def fibonacci(num, prev_num, number_it, fbn_lst):
    new_num = prev_num + num
    number_it -= 1
    if number_it >= 0:
        fbn_lst.append(num)
        fibonacci(new_num, num, number_it, fbn_lst)


position = int(input('Введите позицию числа в ряде Фибоначчи: '))
fbn_lst = []
fibonacci(1, 0, position, fbn_lst)
print('Число: ', fbn_lst[position - 1])

# зачет!
