class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('Картошка еще не созрела!\n')
                return False
            else:
                print('Вся картошка созрела! Можно собирать\n')
                return True

    def harvesting(self):
        print('Садовник собирает урожай')
        for i_potato in self.potatoes:
            i_potato.state = 0
            i_potato.print_state()
        self.are_all_ripe()

class Gardener:

    def __init__(self, garden):
        self.garden = garden

    def take_care(self):
        print('Садовник ухаживает за грядкой')
        self.garden.grow_all()
        if self.garden.are_all_ripe():
            self.garden.harvesting()








my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
my_gardener = Gardener(my_garden)
for _ in range(3):
    my_gardener.take_care()

