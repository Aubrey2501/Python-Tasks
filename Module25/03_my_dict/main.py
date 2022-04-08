class Dict:

    def __init__(self, dct):
        self.dct = dct
        self.dct_value = ''

    def set_dct(self, dct_key):
        if dct_key.isdigit():
            dct_key = int(dct_key)
        if dct_key in self.dct:
            self.dct_value = self.dct[dct_key]

    def get_dct(self):
        return self.dct_value


example_dct = {0: 'Вася', 1: 'Петя', 3: 'Саша', 4: 'Вова'}
my_dict = Dict(example_dct)
i_key = input('Введите ключ словаря: ')
my_dict.set_dct(i_key)
print(my_dict.get_dct())
