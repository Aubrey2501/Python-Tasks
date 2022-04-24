def refactoring(lst1, lst2):
    """
    Функция генерации списка произведений аргументов
    Args:
        lst1 (list, int): первый список со значениями
        lst2 (list, int): второй список со значениями
    Returns:
        result (generator, int) - произведения аргументов из первого списка на аргументы из второго списка
    """
    for x in lst1:
        for y in lst2:
            result = x * y
            yield result


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
my_generator = refactoring(lst1=list_1, lst2=list_2)
if to_find in my_generator:
    print('Found!!!')
else:
    print('Not found')

# зачет!
