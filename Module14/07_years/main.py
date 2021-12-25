while True:
    first_year = int(input('\nВведите первый год: '))
    second_year = int(input('Введите второй год: '))
    if  9999< (first_year or second_year) or (first_year or second_year) < 1000 or first_year > second_year:
        print('Ошибка ввода')
    else:
        break
print('Года с тремя одинаковыми цифрами:')
for year in range(first_year, second_year + 1):
    this_year = year
    a = year // 1000
    year %= 1000
    b = year // 100
    year %= 100
    c = year // 10
    d = year % 10
    count = 0
    if (a == b == c) or (b == c == d) or (a == c == d):
        print(this_year)
