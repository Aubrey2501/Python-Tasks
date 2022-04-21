# coding: utf-8
import os


def gen_files_path(dir_name):
    for root, dirs, files in os.walk(top='c:/'):
        if os.path.isdir(root) and root.endswith(dir_name):
            dir_path = root
            break

    dir_list = os.listdir(dir_path)
    for i_elem in dir_list:
        i_path = os.path.join(dir_path, i_elem)
        if os.path.isdir(i_path):
            files_list = (os.path.join(i_path, i_file) for i_file in os.listdir(i_path) if os.path.isdir(i_path))
            yield files_list
        else:
            print(i_path)

print('\n')
files_list = gen_files_path(dir_name='Module26')
for item in files_list:
    for i_elem in item:
        print(i_elem)


