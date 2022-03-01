def my_zip(*args):
    num_args = len(args)
    min_len = min((len(args[i]) for i in range(num_args)))

    i_tuple = (args[i][j] for j in range(min_len) for i in range(num_args))
    return(i_tuple)
    # for elem in i_tuple:
    #     print(i_tuple[elem])





a = [{'x': 4}, 'b', 'z', 'd']
b = (10, {20, }, [30], 'z')

print(my_zip(a, b))


# print(my_zip(a, b))
# -> [({‘x’: 4}, 10), (‘b’, {20}), (‘z’, [30]), (‘d’, ‘z’)]