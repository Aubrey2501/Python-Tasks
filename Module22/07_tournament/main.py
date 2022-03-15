def create_dict(string, limit):
    string_lst = string.split()
    if int(string_lst[2]) > limit:
        string_lst[1] = string_lst[1][0] + '.'
        new_string = ' '.join(string_lst)
        file_dct[string_lst[2]] = new_string


inp_file = open('first_tour.txt', 'r')
file_lst = inp_file.read().split('\n')
limit = int(file_lst.pop(0))
inp_file.close()
file_dct = dict()
for i_elem in file_lst:
    create_dict(i_elem, limit)

out_file = open('second_tour.txt', 'w')
out_file.write(str(len(file_dct)) + '\n')

out_file = open('second_tour.txt', 'a')
num = 0
for i, i_value in sorted(file_dct.items(), reverse=True):
    num += 1
    place = str(num) + '). '
    out_file.write(place)
    out_file.write(i_value + '\n')
out_file.close()

