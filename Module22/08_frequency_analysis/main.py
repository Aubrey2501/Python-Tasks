inp_file = open('text.txt', 'r')
text = inp_file.read()
inp_file.close()
sym_lst = []
sym_dict = dict()
sym_lst = [i_sym.lower() for i_sym in text if i_sym.isalpha()]
for i_sym in sym_lst:
    if i_sym in sym_dict:
        sym_dict[i_sym] += 1
    else:
        sym_dict[i_sym] = 1

sum_letters = sum(i_num[1] for i_num in sym_dict.items())

new_lst = [[i_sym, round(i_num / sum_letters, 3)] for i_sym, i_num in sym_dict.items()]
lst_set = sorted(set(new_lst[i][1] for i in range(len(new_lst))), reverse=True)

sorted_lst = []
for i in lst_set:
    i_list = [i_elem for i_elem in new_lst if i_elem[1] == i]
    sorted_lst.extend(sorted(i_list))
# print(sorted_lst)

out_file = open('analysis.txt', 'w')
out_file = open('analysis.txt', 'a')
for i_elem in sorted_lst:
    i_elem[1] = str(i_elem[1])
    i_string = ' '.join(i_elem)
    out_file.write(i_string +'\n')
out_file.close()

# зачет!
