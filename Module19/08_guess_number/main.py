max_number = int(input('Введите максимальное число: '))
# TODO Стоит загадать число - загаданное_число = randint(1, max_number)
set_list = {str(i) for i in range(1, max_number + 1)}

question = ''
exist_set = set()
while True:
    question = input('Нужное число есть среди вот этих чисел?: ')
    if question == 'Помогите!':
        break
    else:
        # TODO Хорошо бы сделать проверки что получили числа set([x for x in question.split() if x.isdigit()])
        set_int = set_list.intersection(set(question.split()))
        print('Ответ Артема:', end=' ')
        # TODO Ответ "нет" если загаданного числа нет в множестве предположений - загаданое_число not in set_int
        #  В этом случае делаем объединение двух множеств "exist_set" и "set_int"
        #  Есть метод "union" https://pythonz.net/references/named/sets.union/
        #  .
        #  Соответственно "если загаданное_число in set_int"  ответ да. В этом случае ничего не делаем
        if set_int == set():
            print('Нет')
        else:
            print('Да')
            exist_set.update(set_int)
# TODO Думаю это лучше сделать в условии на 9 строчке
print('Артём мог загадать следующие числа:', end=' ')
for symbol in sorted(set_list.difference(exist_set)):
    print(symbol, end=' ')
