# TODO здесь писать код

people = int(input('Кол-во человек: '))
rhyme = int(input('Какое число в считалке? '))
print('Значит выбывает каждый', rhyme, 'человек')
ring = list(range(1, people + 1))
i_begin = 0
while len(ring) != 1:
    begin = ring[i_begin]
    print('\nТекущий круг людей:', ring)
    print('Начало счета с номера', begin)
    i_delete = (i_begin + rhyme - 1) % len(ring)
    if i_delete == len(ring) - 1: #последний элемент
        i_begin = 0
    else:
        i_begin = i_delete
    delete = ring[i_delete]
    print('Выбывает человек под номером', delete)
    ring.remove(delete)

print('\nОстался человек под номером', ring[0])
