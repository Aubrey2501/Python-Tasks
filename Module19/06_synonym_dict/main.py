syn_dict = dict()
num_pars = int(input('Введите количество пар слов: '))
for i in range(num_pars):
    print(i + 1, 'пара', end=': ')
    string = input().lower()
    l_string = string.split()
    word_1 = l_string[0]
    word_2 = l_string[len(l_string) - 1]
    syn_dict[word_1] = word_2
    syn_dict[word_2] = word_1

print()
while True:
    search_w = input('Введите слово: ').lower()
    found_w = syn_dict.get(search_w)
    if not found_w:
        print('Такого слова в словаре нет.')
    else:
        print('Синоним:', found_w)
        break

# зачет!
