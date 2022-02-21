def tpl_sort(x1, x2, x3, x4, x5, x6, x7):
    list_1 = [x1, x2, x3, x4, x5, x6, x7]
    is_int = {True if isinstance(i, int) else False for i in list_1}
    if False in is_int:
        return (tuple(list_1))
    else:
        return (tuple(sorted(list_1)))


print(tpl_sort(6, 3, -1, 8, 4, 10, -5))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

# зачет!
