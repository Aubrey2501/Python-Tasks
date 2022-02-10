geography = dict()
num_counries = int(input('Кол-во стран: '))

for i_country in range(num_counries):
    while True:
        print(i_country + 1, end=' ')
        string = input('страна: ')
        l_string = string.split()

        if len(l_string) != 4:
            print('Ошибка ввода! Повторите')
        else:
            break

    geography[l_string[0]] = [l_string[1], l_string[2], l_string[3]]
# print(geography)

for i in range(3):
    print()
    print(i + 1, end='-й ')
    i_city = input('город: ')
    is_city = False
    for i_country in geography:
        if i_city in geography[i_country]:
            print('Город', i_city, 'расположен в стране', i_country)
            is_city = True
            break

    if not is_city:
        print('По городу', i_city, 'данных нет')

# зачет!
