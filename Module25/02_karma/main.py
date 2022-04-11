import random


class Karma:
    """
    Базовый класс Карма
    Attributes:
        count (int): счетчик дней
        exceptions (list): список исключений
        karma (int): счетчик накопленных очков кармы
        day_karma (int): количество очков кармы за текущий день
    """
    __exceptions = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
    __count = 0

    def __init__(self):
        self.__karma = 0
        self.__day_karma = 0

    def set_carma(self, rand_karma):
        """
        Сетер для определения очков дневной кармы и подсчета суммарной кармы за период
        :param rand_karma (int): случайное значение очков дневной кармы от 1 до 7
        Attributes:
            count (int): счетчик дней
            exceptions (list): список исключений
            day_karma (int or exception): количество очков кармы за текущий день или исключение
            karma (int): счетчик накопленных очков кармы
        """
        self.__count += 1
        self.__day_karma = random.choices((rand_karma, random.choice(self.__exceptions)), weights=[10, 1])[0]
        if self.__day_karma not in self.__exceptions:
            self.__karma += self.__day_karma
        else:
            raise Exception(self.__day_karma)

    def get_karma(self):
        """
        Геттер для получения суммы накопленной кармы за период
        :return: karma -  сумма накопленной кармы за период
        :rtype: int
        """
        return self.__karma

    def get_count(self):
        """
        Геттер для получения значения счетчика дней
        :return: count
        :rtype: int
        """
        return self.__count

def one_day(karma):
    """
    Процедура инициализации расчета дневной кармы
    :param karma (type): элемент класса Карма
    :param: rand_karma (int): случайное значение очков кармы за день от 1 до 7
    """
    rand_karma = random.randint(1, 7)
    karma.set_carma(rand_karma)


my_karma = Karma()
file = open('karma.log', 'w')
while True:
    try:
        one_day(my_karma)
        if my_karma.get_karma() >= 5000:
            print('\nIt took {} days to reach 5000 karma points'.format(my_karma.get_count()))
            file.close()
            break

    except Exception as error:
        file.write('Day {}: Exception {}\n'.format(my_karma.get_count(), error))