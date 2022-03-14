import os

def count_sym(word_lst, num_sym):
    for symbol in word_lst:
        if symbol.isalpha():
            num_sym += 1
            symbol = symbol.lower()
            if symbol not in sym_dict:
                sym_dict[symbol] = 1
            else:
                sym_dict[symbol] += 1
    return num_sym

zen_file = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r')
zen_lst = zen_file.read().split('\n')
num_strings = len(zen_lst)
num_symbols = num_words = 0
sym_dict = dict()
for i_string in zen_lst:
    string_lst = i_string.split(' ')
    num_words += len(string_lst)
    for i_word in string_lst:
        word_lst = list(i_word)
        num_symbols = count_sym(word_lst, num_symbols)
min_sym_count = min(sym_dict.values())
for i_sym, i_num in sym_dict.items():
    if i_num == min_sym_count:
        min_sym = i_sym
        break
print('Количество букв в файле:', num_symbols)
print('Количество слов в файле:', num_words)
print('Количество строк в файле:', num_strings)
print('Наиболее редкая буква:', min_sym)
