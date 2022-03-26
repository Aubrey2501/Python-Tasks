import random
class Varrior:
    hp = 100
    alive = True

    def __init__(self, index):
        self.index = index

    def attack(self):
        print('Атакует воин {}! Здоровье - {}'.format(self.index, self.hp))

    def defend(self):
        self.hp -= 20
        print('Защищается воин {}! Здоровье - 20! Осталось здоровья: {}'.format(self.index, self.hp))

    def is_alive(self):
        if self.hp <= 0:
            self.alive = False
            print('Воин {} пал в бою! Бой окончен'.format(self.index))
            return False
        return True

    def var_info(self):
        print('Воин номер {}: здоровье- {}'.format(self.index, self.hp))


varriors = [Varrior(index) for index in range(1, 3)]
count = 0
while True:
    count += 1
    print()
    for i_varrior in varriors:
        i_varrior.var_info()
    print('Ход номер', count, end=':\n')
    dice = random.randint(0, 1)
    varriors = [i_varrior(i).attack() if i == dice else i_varrior(i).defend() for i_varrior in varriors]
    # for i_varrior in varriors:
    #     print(i_varrior.is_alive())

    # if not all([i_varrior.is_alive() for i_varrior in varriors]):
    #     break

