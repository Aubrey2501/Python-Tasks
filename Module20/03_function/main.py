def slicer(prime, symbol):
    new_tuple = tuple()
    if symbol in prime:
        new_tuple = prime[prime.index(symbol):]
        for index, i_sym in enumerate(new_tuple):
            if i_sym == symbol and index != 0:
                new_tuple = new_tuple[:index + 1]
                break
    return new_tuple


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

# зачет!
