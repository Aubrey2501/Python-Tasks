# coding: utf-8
import os


def find_dir(dir_name):
    """
    Функция рекурсивного поиска пути к директории с указанным именем в дереве каталогов, начиная с корневого
    Args:
        dir_name (str): наименование искомого каталога
    Returns:
        root(str): абсолютный путь к искомому каталогу
    """
    dir_lst = (i_root for i_root, i_dirs, i_files in os.walk(top='c:/')
               if os.path.isdir(i_root) and i_root.endswith(dir_name))
    yield dir_lst


def gen_files_path(dir_name):
    """
    Функция - генератор имен файлов, находящихся в каталогах искомой директории
    Args:
        dir_name (str): наименование искомого каталога
    Returns:
        files_list (generator list): список- генератор с именами файлов
    """
    dir_list = os.listdir(dir_name)
    for i_elem in dir_list:
        i_path = os.path.join(dir_name, i_elem)
        if os.path.isdir(i_path):
            files_list = (os.path.join(i_path, i_file) for i_file in os.listdir(i_path) if os.path.isdir(i_path))
            yield files_list
        else:
            print(i_path)


print()
dir_list = find_dir(dir_name='Module26')
for i_elem in dir_list:
    dir_list.close()
    for i_dir in i_elem:
        files_list = gen_files_path(dir_name=str(i_dir))
        for item in files_list:
            for i_file in item:
                print(i_file)

# зачет!
