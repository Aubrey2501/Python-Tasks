punct = {'.',',', ';', ':', '!', '?'}
text = input('Введите текст: ')
count = 0
for symbol in text:
    if symbol in punct:
        count += 1

print('Кол-во знаков пунктуации:', count)