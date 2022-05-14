class Robot:
    """Родительский класс Робот"""
    def __init__(self):
        self.model = None

    def get_info(self):
        return 'Я - робот!'.format(self.model)


class Drone(Robot):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.altitude = 0
        self.speed = 0

    def takeoff(self):
        print('\nДрон {} модели {}: Взлетаю!'.format(self.__class__.__name__, self.model))
        self.altitude += 100
        self.speed = 250
        print(self.get_info())

    def fly(self, altitude, speed):
        self.altitude = altitude
        self.speed = speed
        print(self.get_info())
        if self.altitude <= 50 or self.speed <= 100:
            self.speed = 0
            self.altitude = 0
            print('Дрон {} модели {} разбился!'.format(self.__class__.__name__, self.model))
            print(self.get_info())

    def landing(self):
        self.altitude = 0
        self.speed = 0
        print('Дрон {} модели {} успешно приземлился'.format(self.__class__.__name__, self.model))
        print(self.get_info())

    def get_info(self):
        return '{}: Скорость - {} км/ч, Высота - {} м.'.format(
            self.model, self.speed, self.altitude)


class ReconDrone(Drone):
    def __init__(self, model):
        super().__init__(model)

    def operate(self):
        if self.speed == 0 and self.altitude == 0:
            self.takeoff()
            self.altitude = 500
            self.speed = 150
        print('Веду разведку с воздуха')
        print(self.get_info())

    def __str__(self):
        return self.get_info()


class FightingDrone(Drone):
    def __init__(self, model, weapon=None):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        if self.speed == 0 and self.altitude == 0:
            self.takeoff()
            self.altitude = 300
            self.speed = 150
        print('Защищаю объект с воздуха при помощи {}'.format(self.weapon))
        print(self.get_info())

    def __str__(self):
        return self.get_info()


scouter = ReconDrone('Астигматизм')
fighter = FightingDrone('Орлангутанг', weapon='Пушка')

scouter.takeoff()
scouter.fly(altitude=350, speed=150)
scouter.operate()
scouter.fly(altitude=50, speed=200)

fighter.takeoff()
fighter.fly(altitude=350, speed=150)
fighter.operate()
fighter.fly(altitude=150, speed=200)
fighter.landing()