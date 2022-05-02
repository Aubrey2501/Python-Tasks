import abc
from abc import ABC


class Transport(ABC):
    def __init__(self) -> None:
        self.speed = 0
        self.colour = colour
        self.model = None
        self.surface = None

    @abc.abstractmethod
    def move(self, speed):
        self.speed = speed
        print('{} {} {} is moving along the {} at a speed {} mph.\n'.format(
            self.colour, self.__class__.__name__,  self.model, self.surface, self.speed))

    def __str__(self):
        return f'{self.colour} {self.__class__.__name__}, model {self.model}, speed {self.speed} mph'

    def signal(self):
        print('{} {} {}: Beep!\n'.format(self.colour, self.__class__.__name__, self.model))


    @property
    def colour(self):
        return 'The colour of {} {} is {}.\n'.format(
            self.__class__.__name__,  self.model, self.colour)

    @colour.setter
    def colour(self, colour):
        self.colour = colour
        print(self.colour)
        prev_colour = self.colour
        self.colour = colour
        print('{} {} changed colour from {} to {}.\n'.format(
            self.__class__.__name__,  self.model, prev_colour, self.colour))
        print('')
        self.colour = colour


class PlayMusic:
    def play(self, music):
        print(f"{music} music playing in the {self.colour} {self.__class__.__name__} {self.model}\n")


class Car(Transport, PlayMusic):
    def __init__(self, model, colour):
        super().__init__()
        self.colour = colour
        self.model = model
        self.surface = 'ground'

    def move(self, speed):
        super().move(speed)

    def signal(self):
        super().signal()



class Boats(Transport):
    def __init__(self, model, colour):
        super().__init__()
        self.colour = colour
        self.model = model
        self.surface = 'water'

    def move(self, speed):
        super().move(speed)

    def signal(self):
        super().signal()


class Amphibious(Transport):
    def __init__(self, model, colour):
        super().__init__()
        self.colour = colour
        self.model = model
        self.surface = None

    def move(self, speed, surface):
        self.surface = surface
        self.speed = speed
        super().move(speed)

    def signal(self):
        super().signal()


my_car = Car(model='Audi', colour='Green')
print(my_car.colour)
my_car.colour = 'Gray'
print(my_car.colour)

print(my_car)
my_car.move(80)
my_car.signal()

# my_car.play('Rolling Stones')
# my_car.colour = 'Gray'
# print(my_car.colour)

#
# amphy = Amphibious('БТР-80', 'Green')
# amphy.move(25, 'water')