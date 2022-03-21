# encoding: utf-8

try:
    bruce_willis = 42
    input_data = input('Введите строку: ')
    leeloo =int(input_data[4])
except ValueError:
    print('Введенные данные не являются числом!')
except IndexError:
    print('Невозможно выделить пятый элемент!')
except:
    print('Непредвиденная ошибка данных')
else:
    result = bruce_willis * leeloo
    print(f' - Leeloo Dallas! Multi-pass N {result}!')