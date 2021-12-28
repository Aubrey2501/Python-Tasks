ID_numbers = []
staff_num = int(input('Введите количество сотрудников: '))

for _ in range(staff_num):
    ID_next = int(input('ID сотрудника: '))
    ID_numbers.append(ID_next)

find_ID = int(input('Какой ID ищем?: '))
flag = False
for staff in (ID_numbers):
    if find_ID == staff:
        flag = True

if flag:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')