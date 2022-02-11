import random

max_number = int(input('Введите максимальное число: '))
set_list = {i for i in range(1, max_number + 1)}

answer = random.randint(1, max_number)
question = ''

while True:
    question = input('Нужное число есть среди вот этих чисел?: ')
    if question == 'Помогите!':
        break
    else:
        set_int = set(int(number) for number in question.split() if number.isdigit())
        print('Ответ Артема:', end=' ')
        # TODO Хорошо бы прерывать цикл если число явно угадано
        #  if len(set_int) == 1 and answer in set_int
        if answer in set_int:
            print('Да')

        else:
            print('Нет')
            set_list = set_list.difference(set_int)

print('\nАртём мог загадать следующие числа:', end=' ')
for number in sorted(set_list):
    print(number, end=' ')

# зачет!
