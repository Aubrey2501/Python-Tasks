import os


def directory_content(cur_path, num_dir, num_files, sum_size):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isdir(path):
            num_dir += 1
            data = directory_content(path, num_dir, num_files, sum_size)
            num_dir = data[0]
            num_files = data[1]
            sum_size = data[2]
        elif os.path.isfile(path):
            num_files += 1
            sum_size += os.path.getsize(path)
    return (num_dir, num_files, sum_size)


while True:
    # cur_path = input('\nПожалуйста, введите путь до директории:')
    cur_path = ('C:\\Users\\Евгений\PycharmProjects\Python_Basic\Mod 20 - tasks')
    if os.path.exists(cur_path):
        data = directory_content(cur_path, 0, 0, 0)
        break
    else:
        print('Данных по указанному адресу не обнаружено. Повторите ввод:')

print('Размер каталога (в Кб):', data[2])
print('Количество подкаталогов:', data[0])
print('Количество файлов', data[1])

# зачет!
