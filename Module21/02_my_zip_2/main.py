def my_zip(*args):
    num_args = len(args)
    list_args = [list(args[i]) for i in range(num_args)]
    min_len = min(len(args[i]) for i in range(num_args))

    new_list = [tuple(elem[i] for elem in list_args) for i in range(min_len)]
    return new_list


a = [{'x': 4}, 'b', 'z', 'd']
b = (10, {20, }, [30], 'z')
print(my_zip(a, b))

a = [1, 2, 3, 4, 5]
b = {1: 's', 2: 'q', 3: 4}
x = (1, 2, 3, 4, 5)
print(my_zip(a, b, x))


