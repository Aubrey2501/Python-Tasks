def ariphm_oper(string):
    # TODO Все проверки невалидных данных делайте здесь, и кидайте исключение в основной цикл.
    #  Запись в файл перенесите в основной цикл
    result = eval(string)
    out_file = open('result.txt', 'a')
    print(result)
    out_file.write(str(result) + '\n')


arithm_oper = ['+', '-', '*', '/', '//', '%']
# TODO Открывайте файлы через контекстный менеджер
inp_file = open('calc.txt', 'r')
out_file = open('result.txt', 'w')
for i_line in inp_file:
    try:
        line_lst = i_line.split()
        flag_err = False
        if not line_lst[0].isdigit() or not line_lst[2].isdigit():
            flag_err = True
            raise ValueError
        elif line_lst[1] not in arithm_oper:
            flag_err = True
            raise ValueError
        else:
            print(i_line, end=' = ')
            ariphm_oper(i_line)


    except ValueError:
        print('Ошибка в строке', i_line)
        answer = input('Хотите исправить (Да/Нет)?: ').lower()
        if answer == 'да':
            i_line = input('Введите исправленную строку: ')
            print(i_line, end=' = ')
            ariphm_oper(i_line)

        else:
            continue

out_file.close()
