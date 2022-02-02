# Сообщение: Это задание очень! простое.
# Новое сообщение: отЭ еинадаз ьнечо! еотсорп.
# Пример 2:
# Сообщение: Хотя ,. возм:ожно и нет.
# Новое сообщение: ятоХ ,. мзов:онжо и тен.

massage = input('Сообщение: ')
massage_lst = massage.split(' ')
special = '.,!:;'
new_msg_lst = []

for word in massage_lst:
    word_lst = list(word)
    new_word_lst = []

    new_word_lst = [word_lst[i_sym - 1] for i_sym in range(len(word_lst), 0, -1)]

    for symbol in new_word_lst:
        if symbol in special:
            i_sp = word_lst.index(symbol)
            new_word_lst.remove(symbol)
            new_word_lst.insert(i_sp, symbol)

    new_word = ''.join(new_word_lst)
    new_msg_lst.append(new_word)

new_massage = ' '.join(new_msg_lst)
print('Новое сообщение:', new_massage)

# зачет!
