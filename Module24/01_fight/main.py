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
        if self.hp <= 0:
            self.alive = False



def var_info(varriors):
    for i_var in varriors:
        print('Воин номер {}: здоровье- {}'.format(i_var.index, i_var.hp))

varriors = [Varrior(index) for index in range(1, 3)]
var_info(varriors)
count = 0
while True:
    count += 1
    print()
    print('Ход номер', count, end=':\n')
    dice = random.randint(0, 1)
    varriors = [varriors[i].attack() if i == dice else varriors[i].defend() for i in range(2)]
    if  all(varriors.alive == 'True'):
