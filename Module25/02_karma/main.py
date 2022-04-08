import random


class Karma:
    __exceptions = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
    __count = 0

    def __init__(self):
        self.__karma = 0
        self.__day_karma = 0

    def set_carma(self, rand_karma):
        self.__count += 1
        self.__day_karma = random.choices((rand_karma, random.choice(self.__exceptions)), weights=[10, 1])[0]
        if self.__day_karma not in self.__exceptions:
            self.__karma += self.__day_karma
        else:
            raise Exception(self.__day_karma)

    def get_karma(self):
        return self.__karma

    def get_count(self):
        return self.__count


def one_day(karma):
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