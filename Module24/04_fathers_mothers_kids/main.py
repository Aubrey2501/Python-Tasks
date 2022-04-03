import random

class Child:
    calm_state = {True: 'спокоен', False: 'плачет'}
    hungry_state = {True: 'голоден', False: 'сыт'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = True
        self.hungry = False

    def child_info(self):
        print('Ребенок: {}\nВозраст: {} лет\nСостояние: {}, {}'.format(self.name, self.age, Child.calm_state[self.calm], Child.hungry_state[self.hungry]))

    def feed_children(self):
        if self.hungry:
            self.hungry = False
        print('Ребенок {} покормлен! Состояние: {}, {}'.format(self.name, Child.hungry_state[self.hungry], Child.calm_state[self.calm]))

    def calm_down(self):
        if not self.calm:
            self.calm = True
        print('Ребенок {} успокоен! Состояние: {}, {}'.format(self.name, Child.hungry_state[self.hungry], Child.calm_state[self.calm]))
class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def parent_info(self):
        print('\nРодитель: {}\nВозраст: {} лет\nДети:'.format(self.name, self.age))
        for i_child in self.children:
            i_child.child_info()


def to_do(num_act, i_child):
    if num_act == 2:
        i_child.child_info()
    elif num_act == 3:
        i_child.feed_children()
    else:
        i_child.calm_down()


def chld_act(num_act, childs, childs_lst):
    sub_action = int(input('всех (1) или конкретного(2)?: '))
    if sub_action == 1:
        for i_child in childs_lst:
            to_do(num_act, i_child)
    elif sub_action == 2:
        i_name = input('Введите имя: ')
        if any(childs[index][0] == i_name for index in range(len(childs))):
            for index in range(len(childs)):
                if childs[index][0] == i_name:
                    i_child = childs_lst[index]
                    to_do(num_act, i_child)
    else:
        print('Ошибка ввода!')



childs = [['Митя', 5], ['Оля', 10], ['Ваня', 8]]
childs_lst = [Child(i_child[0], i_child[1]) for i_child in childs]
parents =[['Владимир', 45], ['Наталья', 35]]
parents_lst = [Parent(parents[i][0], parents[i][1], childs_lst) for i in range(len(parents))]

try:
    while True:
        rand_state = [False, True]
        for i_child in childs_lst:
            i_child.hungry = random.choice(rand_state)
            i_child.calm = random.choice(rand_state)

        action = int(input('\nВыберите дейтвие:\n 1 - Информация о родителях\n 2 - информация о детях\n 3 - покормить детей\n 4 - успокоить детей\n 5 - выход\n >> '))

        if action == 1:
            sub_action = int(input('Вывести информацию о всех родителях (1) или о конкретном(2)?: '))
            if sub_action == 1:
                for i_parent in parents_lst:
                    i_parent.parent_info()
            if sub_action == 2:
                i_name = input('Ввведите имя: ')
                if any(parents[index][0] == i_name for index in range(len(parents))):
                    for index in range(len(parents)):
                        if parents[index][0] == i_name:
                            parents_lst[index].parent_info()
                else:
                    print('Не найдено!')

        elif action == 2:
            print('\nВывести информацию о детях:', end=' ')
            chld_act(action, childs, childs_lst)

        elif action == 3:
            print('\nПокормить детей:', end=' ')
            chld_act(action, childs, childs_lst)

        elif action == 4:
            print('\nУспокоить детей:', end=' ')
            chld_act(action, childs, childs_lst)

        elif action == 5:
            break
        else:
            print('Неверная команда, повторите ввод')

except ValueError:
    print('Ошибка ввода!')
