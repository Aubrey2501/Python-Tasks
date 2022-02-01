# TODO здесь писать код
# Введите строку: aaAAbbсaaaA
# Закодированная строка: a2A2b2с1a3A1

text = input('Введите строку: ')
new_txt = []

count_s = 1
symbol = text[0: 1:]

for i in range(len(text)):
    if text[i + 1:].startswith(symbol):
        count_s += 1
    else:
        new_txt.append(symbol)
        new_txt.append(str(count_s))
        symbol = text[i + 1: i + 2:]
        count_s = 1

print('Закодированная строка:', ''.join(new_txt))
