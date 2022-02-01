# TODO здесь писать код

text = input('Введите строку: ')
txt_list = text.split(' ')

max_len = max([len(word) for word in txt_list])
max_lst_word = [word for word in txt_list if len(word) == max_len]
# max_word = ', '.join(max_lst_word)   # можно вывести самые длинные слова через запятую, если их несколько

print('Самое длинное слово:', max_lst_word[0])
print('Длина этого слова:', max_len)
