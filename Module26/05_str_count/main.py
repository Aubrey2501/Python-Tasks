import os

def sum_strings(dir_name):
    directory_lst = os.listdir(dir_name)
    # print(directory_lst)
    for i_file in directory_lst:
        if i_file.endswith('.py'):
            with open(i_file, 'r') as open_file:
                string_lst = open_file.read().split('\n')
                # print(string_lst)
                strings_numbers = [num_str for num_str in range(len(string_lst))
                           if not(string_lst[num_str].strip() == '' or string_lst[num_str].lstrip().startswith('#'))]
                yield strings_numbers


directory = os.curdir
strings_num = sum_strings(dir_name=directory)
# print(strings_num)
count = 0
for i_elem in strings_num:
    count += len(i_elem)
print(count)