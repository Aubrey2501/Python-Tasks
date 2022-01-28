greeting = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
names_lst = input('Список людей через запятую: ').split(', ')
ages_str = input('Возраст людей через пробел: ')

ages_lst = [int(age) for age in ages_str.split()]

for man in range(len(names_lst)):
    print(greeting.format(name=names_lst[man], age=str(ages_lst[man])))

