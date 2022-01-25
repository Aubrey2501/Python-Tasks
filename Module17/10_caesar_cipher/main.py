word = input('Введите сообщение: ')
K = int(input('Введите сдвиг: '))

alphabet = ('абвгдеёжзийклмнопрстуфхцчшщыьъэюя')
list_alph = list(alphabet)

code_alph = alphabet[K: len(alphabet)]
code_alph += (alphabet[0: K])

code_word = ''
for symbol in word:
    if symbol != ' ':
        code_sym = code_alph[list_alph.index(symbol)]
    else:
        code_sym = ' '
    code_word += code_sym

print('Зашифрованное сообщение:', code_word)

# зачет!
