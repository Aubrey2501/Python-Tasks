def q_hofstadter(Q, lim):
    """
    Фунция- генератор чисел последовальности Q Хофштадтера
    Args:
        Q (list): список из двух первых членов последовательности
        lim (int): число членов генерируемой последовательности
    Returns:
        Q (list): сгенерированная последовательность Хофштадтера
    """
    if Q == [1, 2]:
        raise AttributeError('Недопустимое значение [1, 2]')
    for n in range(2, lim):
        q_n = Q[n - (Q[n - 1])] + Q[n - Q[n - 2]]
        Q.append(q_n)
        yield Q


q = [1, 1]
limit = 20

try:
    hofstadter = q_hofstadter(Q=q, lim=limit)
    for item in hofstadter:
        if len(item) == limit:
            print(item)
except AttributeError as error:
    print(error)

# зачет!
