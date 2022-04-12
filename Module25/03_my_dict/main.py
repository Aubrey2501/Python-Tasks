class MyDict:
    """
    Класс Dict, описывающий словарь
        Attributes:
            dct (dict) - словарь
            dct_value - значение элемента словаря (по умолчанию 0)
    """
    def __init__(self, dct):
        self.dct = dct
        self.dct_value = 0

    def set_dct(self, dct_key):
        """
        Сеттер для занесения записи в словарь dct
        :param dct_key: ключ словаря
        :param dct_value: значение в словаре по ключу dct_key
        """
        if dct_key.isdigit():
            dct_key = int(dct_key)
        if dct_key in self.dct:
            self.dct_value = self.dct[dct_key]

    def get(self, dct_key):
        """
        Геттер для получения записи из словаря
        :param dct_key: ключ словаря
        :return: dct_value
        """
        self.set_dct(dct_key)
        return self.dct_value


example_dct = {1: 'Вася', 2: 'Петя', 3: 'Саша', 4: 'Вова'}
while True:
    my_dict = MyDict(example_dct)
    i_key = input('Введите ключ словаря: ')
    print(my_dict.get(i_key))
