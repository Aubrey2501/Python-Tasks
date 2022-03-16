import os


def count_sym(word_lst):
    for symbol in word_lst:
        if symbol.isalpha():
            symbol = symbol.lower()
            if symbol not in sym_dict:
                sym_dict[symbol] = 1
            else:
                sym_dict[symbol] += 1


zen_file = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r')
zen_lst = zen_file.read().split('\n')
zen_file.close()
num_strings = len(zen_lst)
num_words = 0
sym_dict = dict()
for i_string in zen_lst:
    string_lst = i_string.split(' ')
    num_words += len(string_lst)
    for i_word in string_lst:
        word_lst = list(i_word)
        count_sym(word_lst)

num_sym = sum(sym_dict.values())
min_count = min(sym_dict.values())
symbol = (i_sym for i_sym, i_num in sym_dict.items() if i_num == min_count)
for sym in symbol:
    min_sym = sym

print('Количество букв в файле:', num_sym)
print('Количество слов в файле:', num_words)
print('Количество строк в файле:', num_strings)
print('Наиболее редкая буква:', min_sym)

# зачет!
