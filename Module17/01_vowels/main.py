# TODO здесь писать код
def is_vowel(letter):
    result = []
    vowels = ['a', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']
    result = [True for i_letter in vowels if i_letter == letter]
    return (result)


# string = input('Введите текст: ')
string = 'Нужно отнести кольцо в Мордор!'
list_vow = [letter for letter in string if is_vowel(letter)]
print('Список гласных букв:', list_vow)
print('Длина списка:', len(list_vow))

# зачет!
