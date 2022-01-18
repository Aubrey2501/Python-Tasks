# TODO здесь писать код
num_skates = int(input('Кол-во коньков: '))
skates = []
for i in range(num_skates):
    print('Размер', i + 1, end=' ')
    skate = int(input('пары: '))
    skates.append(skate)

num_people = int(input('\nКол-во людей: '))
sizes = []
for i in range(num_people):
    print('Размер ноги', i + 1, end=' ')
    size = int(input('человека: '))
    sizes.append(size)

men = 0
for size in sizes:
    count_skates = skates.count(size)
    if count_skates != 0:
        men += 1
        skates.remove(size)

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', men)


