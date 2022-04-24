class SqrtInt:
    """
    Класс-итератор для определения последовательности квадратов чисел
    Attributes:
        __cur_num (int): текущее число в последовательности
        __sqrt (int): квадрат от __cur_num

    Args:
        max_num (int): предельное число в последовательности __cur_num
    """
    def __init__(self, max_num):
        self.__max_num = max_num
        self.__cur_num = 0
        self.__sqrt = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Шаг next итератора
        Returns:
        символьная строка для вывода ответа
        """
        self.__cur_num += 1
        if self.__cur_num > self.__max_num:
            raise StopIteration
        self.__sqrt = self.__cur_num ** 2
        return '{:<2} **  2  = {}'.format(self.__cur_num, self.__sqrt)


def sqrt_gen(max_num):
    """
    Функция - генератор для вычисления квадратов чисел
    Args:
        max_num (int): предельное число в последовательности чисел
    Returns:
        i_num (int): текущее число в последовательности
        i_sqrt (int): квадрат от числа i_num
    """
    for i_num in range(1, max_num + 1):
        i_sqrt = i_num ** 2
        yield i_num, i_sqrt


N = 20
my_iter = SqrtInt(N)
print('Реализация итератора:')
for item in my_iter:
    print(item)

print('\nРеализация генератора:')
my_generator = sqrt_gen(N)
for i_num, i_sqrt in my_generator:
    print('{:<2} **  2  = {}'.format(i_num, i_sqrt))

print('\nРеализация генераторного выражения:')
gen_term = ((i_num, i_num ** 2) for i_num in range(1, N + 1))
for i_num, i_sqrt in gen_term:
    print('{:<2} **  2  = {}'.format(i_num, i_sqrt))

# зачет!
