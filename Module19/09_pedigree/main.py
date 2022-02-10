# Введите количество человек: 9
Romanov_list = ['Alexei Peter_I', 'Anna Peter_I', 'Elizabeth Peter_I', 'Peter_II Alexei', 'Peter_III Anna',
                'Paul_I Peter_III', 'Alexander_I Paul_I', 'Nicholaus_I Paul_I']

Romanov = dict()
for _, pair in enumerate(Romanov_list):
    child, father = pair.split()
    if not (isinstance(child, str) and isinstance(father, str)):
        print('Ошибка ввода!')
        break
    else:
        Romanov[child] = father

generation = dict()
for child in Romanov:
    father = Romanov[child]
    if father not in Romanov:
        generation[father] = 0

    if child not in generation:
        generation[child] = 1
        while father in Romanov:
            generation[child] += 1
            father = Romanov[father]

print('Уровень членов семьи в генеалогическом дереве:')
for member in sorted(generation):
    print(member, ':', generation[member])


