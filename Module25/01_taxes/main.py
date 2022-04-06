class Property():
    __coeff = 0
    __tax = 0

    def __init__(self, object, worth):
        self.__object = object
        self.__worth = worth

    def get_tax(self):
        self.tax = self.__worth * self.coeff
        return self.tax

    def __str__(self):
        return 'Property object: {}\nWorth: {:>19,}\nTax rate: {:>13.1%}\nTax: {:>19,}\n'.format(self.__object, self.__worth, self.coeff, self.tax)


class Apartment(Property):
    def __init__(self, object, worth):
        super().__init__(object, worth)
        self.coeff = 0.001
        self.tax = self.get_tax()


class Car(Property):
    def __init__(self, object, worth):
        super().__init__(object, worth)
        self.coeff = 0.005
        self.tax = self.get_tax()

class CountryHouse(Property):
    def __init__(self, object, worth):
        super().__init__(object, worth)
        self.coeff = 0.002
        self.tax = self.get_tax()


sum_tax = 0
answer = ''
while True:
    try:
        print('Выберите тип объекта недвижимости:')
        answer = input('Квартира - (1), Автомобиль - (2), Загородный дом - (3), Выход - end : ').lower()

        if answer.isdigit():
            answer = int(answer)
            cost = int(input('Укажите стоимость для целей налогообложения: '))
            if answer == 1:
                property = Apartment(object='Apartment', worth=cost)
            elif answer == 2:
                property = Car(object='Car', worth=cost)
            elif answer == 3:
                property = CountryHouse(object='Country House', worth=cost)
            else:
                raise ValueError('Ошибка ввода! Введите число от 1 до 3')

        else:
            if answer == 'end':
                break
            else:
                raise ValueError('Ошибка ввода. Введите число или слово "end"!')

        print(property)
        sum_tax += property.tax

    except ValueError as error:
        print(error)

print('\nИтоговая сумма налога:', sum_tax)

