nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def new_list(lst, new_lst):

    for item in lst:
        if isinstance(item, int):
            new_lst.append(item)
        else:
            new_list(list(item), new_lst)

    return new_lst

new_lst = []
print('Ответ:', new_list(nice_list, new_lst))

