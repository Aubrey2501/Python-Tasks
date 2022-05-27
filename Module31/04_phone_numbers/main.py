import re

telephone_lst = ['9999999999', '999999-999', '99999x9999', '8495123456', '84991234567']
numbers = ("первый", "второй", "третий", "четвертый", "пятый", "шестой", "седьмой", "восьмой", "девятый", "десятый")

for elem in telephone_lst:
    print('{} номер \t{}:\t'.format(numbers[telephone_lst.index(elem)], elem), end=' ')
    result = re.match(r'\b[8-9]\d{9}\b', elem)
    if result:
        print('все в порядке')
    else:
        print('не подходит')

# зачет!
