guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
status = ''
num_guests = len(guests)

while status != 'Пора спать':
    print('\nСейчас на вечеринке', num_guests, 'человек:', guests)
    status = input('Гость пришел или ушел? ')
    name_guest = input('Имя гостя: ')
    if status == 'пришел':
        if num_guests >= 6:
            print('Прости,', name_guest,', но мест нет')
        else:
            print('Привет,', name_guest, '!')
            num_guests += 1
            guests.append(name_guest)
    elif status == 'ушел':
        print('Пока,', name_guest, '!')
        num_guests -= 1
        guests.remove(name_guest)
    else:
        print()
print('Вечеринка закончилась, все легли спать.')