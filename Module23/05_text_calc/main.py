def ar_oper(string):
    # TODO Все проверки невалидных данных делайте здесь, и кидайте исключение в основной цикл.
    #  Запись в файл перенесите в основной цикл
    string = string.replace('\n', '')
    res_lst = string.split(' ')
    if not res_lst[0].isdigit() or not res_lst[2].isdigit():
        raise ValueError
    elif res_lst[1] not in arithm_oper:
        raise ValueError
    else:
        result = eval(string)
        return f'{res_lst[0]} {res_lst[1]} {res_lst[2]} = {result}'

arithm_oper = ['+', '-', '*', '/', '//', '%']
# TODO Открывайте файлы через контекстный менеджер
with open('calc.txt', 'r') as inp_file, open('result.txt', 'w') as out_file:
    for i_line in inp_file:
        try:
            result = ar_oper(i_line)

        except ValueError:
            print('Ошибка в строке', i_line)
            answer = input('Хотите исправить (Да/Нет)?: ').lower()
            if answer == 'да':
                i_line = input('Введите исправленную строку: ')
                result = ar_oper(i_line)

        print(result)
        out_file.write(str(result) + '\n')

inp_file.close()
out_file.close()
