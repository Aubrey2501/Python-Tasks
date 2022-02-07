# TODO здесь писать код
max_number = int(input('Введите максимальное число: '))
set_list = {str(i) for i in range(1, max_number + 1)}

question = ''
exist_set = set()
while True:
    question = input('Нужное число есть среди вот этих чисел?: ')
    if question == 'Помогите!':
        break
    else:
        set_int = set_list.intersection(set(question.split()))
        print('Ответ Артема:', end=' ')
        if set_int == set():
            print('Нет')
        else:
            print('Да')
            exist_set.update(set_int)

print('Артём мог загадать следующие числа:', end=' ')
for symbol in sorted(set_list.difference(exist_set)):
    print(symbol, end=' ')




