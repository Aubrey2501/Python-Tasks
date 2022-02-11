# TODO здесь писать код

# word = input('Введите слово: ').lower()
word = 'это Питон!'.lower()
K = int(input('Введите сдвиг: '))
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщыьъэюя')
print(alphabet)


code = [(alphabet[(alphabet.index(symbol) + K) % 33] if symbol in alphabet else symbol) for symbol in word]
print(''.join(code))


