class MyDict:

    def __init__(self, dct):
        self.dct = dct
        self.dct_value = 0

    def set_dct(self, dct_key):
        if dct_key.isdigit():
            dct_key = int(dct_key)
        if dct_key in self.dct:
            self.dct_value = self.dct[dct_key]

    def get(self, dct_key):
        self.set_dct(dct_key)
        return self.dct_value


example_dct = {0: 'Вася', 1: 'Петя', 3: 'Саша', 4: 'Вова'}
while True:
    my_dict = MyDict(example_dct)
    i_key = input('Введите ключ словаря: ')
    print(my_dict.get(i_key))
