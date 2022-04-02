class Water:
    name = 'Вода'
    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Mud()
        else:
            return None
class Air:
    name = 'Воздух'
    def __add__(self, other):
        if other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        if other.name == 'Вода':
            return Storm()
        else:
            return None
class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if other.name == 'Земля':
            return Lava()
        elif other.name == 'Вода':
            return Steam()
        if other.name == 'Воздух':
            return Lightning()
        else:
            return None
class Soil:
    name = 'Земля'
    def __add__(self, other):
        if other.name == 'Огонь':
            return Lava()
        elif other.name == 'Вода':
            return Mud()
        elif other.name == 'Воздух':
            return Dust()
        else:
            return None
class Storm:
    name = 'Шторм'
class Steam:
    name = 'Пар'
class Mud:
    name = 'Грязь'
class Lightning:
    name = 'Молния'
class Lava:
    name = 'Лава'
class Dust:
    name = 'Пыль'

try:
    while True:
        first_elem = int(input('\nВыберите первый элемент: Вода(1), Воздух(2), Огонь(3) или Земля(4): '))
        second_elem = int(input('Выберите второй элемент: Вода(1), Воздух(2), Огонь(3) или Земля(4): '))
        elements = []
        for i_elem in (first_elem, second_elem):
            if i_elem == 1:
                element = Water()
            elif i_elem == 2:
                element = Air()
            elif i_elem == 3:
                element = Fire()
            elif i_elem == 4:
                element = Soil()
            else:
                raise ValueError('Введено неправильное значение!')
            elements.append(element)

        new_element = elements[0] + elements[1]
        if new_element == None:
            new_element = elements[0]
        print('Соединили: {} + {} и получили'.format(elements[0].name, elements[1].name), end=' ')
        print(new_element.name)

except ValueError as error:
    print(error)