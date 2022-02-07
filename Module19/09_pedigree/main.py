# Введите количество человек: 9
Romanov_list = ['Alexei Peter_I', 'Anna Peter_I', 'Elizabeth Peter_I', 'Peter_II Alexei', 'Peter_III Anna', 'Paul_I Peter_III', 'Alexander_I Paul_I', 'Nicholaus_I Paul_I']

Romanov = dict()
generations = dict()

Romanov = {succession.split()[0]: succession.split()[1] for succession in Romanov_list}

for heir in Romanov.keys():
    generation = 1
    child = heir
    while True:
        father = Romanov[child]
        if father not in Romanov:
            generations[father] = 0
            break
        else:
            generation += 1
            child = father
    generations[heir] = generation

print('Уровень императоров дома Романовых в генеалогическом дереве:')
for heir in sorted(generations):
    print(heir, ':', generations[heir])
