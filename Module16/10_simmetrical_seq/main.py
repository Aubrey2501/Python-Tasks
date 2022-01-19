def list_inp(string, begin , end):
    list_i = []
    for i in range(begin, end + 1):
        list_i.append(string[i])
    return(list_i)

N = int(input('Кол-во чисел: '))
string = []
for _ in range(N):
    number = int(input('Число: '))
    string.append(number)
print('\nПоследовательность:', string)

first_point = N//2

for point in range(first_point, N - 1):
    point_left = point - (N - 1 - point)
    list1 = list_inp(string, point_left, point - 1)
    list2 = list_inp(string, point + 1, N - 1)
    if list1 == list2:
        break

print('Нужно приписать чисел:', point_left + 1)
string_n =[]
for i in range(point_left, -1, -1):
    to_append = string[i]
    string_n.append(to_append)

print('Сами числа:', string_n)

# зачет!
