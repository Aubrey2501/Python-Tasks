import abc
from abc import ABC


class Transport(ABC):
    def __init__(self) -> None:
        self.speed = 0
        self.colour = None
        self.model = None
        self.surface = None

    @abc.abstractmethod
    def move(self, speed):
        self.speed = speed
        print('{} {} {} is moving along the {} at a speed {} mph.\n'.format(
            self.colour, self.__class__.__name__,  self.model, self.surface, self.speed))

    @abc.abstractmethod
    def signal(self):
        print('{} {} {}: Beep!\n'.format(self.colour, self.__class__.__name__, self.model))


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
        super().move(speed)

    def signal(self):
        super().signal()



my_car = Car('Audi', 'Grey')
my_car.move(80)
my_car.signal()
my_car.play('Rolling Stones')

amphy = Amphibious('БТР-80', 'Green')
amphy.move(25, 'water')