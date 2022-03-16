def ceasar_code(string, shift):
    code = alphabet[shift:] + alphabet[:shift]
    code_dict = {i: code[i] for i in range(len(code))}
    # print(code_dict)
    new_string = ''
    for i_sym in string:
        is_upper = i_sym.isupper()
        i_sym = i_sym.lower()
        if not i_sym.isalpha():
            new_sym = i_sym
        else:
            new_sym = code_dict[alph_dict[i_sym]]
        if is_upper:
            new_sym = new_sym.upper()
        new_string += new_sym
    return new_string


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph_dict = dict()
alph_dict = {alphabet[i]: i for i in range(len(alphabet))}
# print(alph_dict)

input_file = open('text.txt', 'r')
file_lst = input_file.read().split('\n')
input_file.close()
out_file = open('cypher_text.txt', 'w')
out_file = open('cypher_text.txt', 'a')

shift = 0
for i_string in file_lst:
    shift += 1
    code_string = ceasar_code(i_string, shift)
    out_file.write(code_string + '\n')
out_file.close()

# зачет!
