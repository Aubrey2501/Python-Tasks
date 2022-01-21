# TODO здесь писать код
import random
def throw(N, trying, row):
    L_i = random.randint(0, N - 1)
    R_i = random.randint(L_i, N - 1)
    print('Бросок', trying + 1, ': Сбиты палки с номера', L_i + 1, 'по номер', R_i + 1)
    row_left = row[0: L_i]
    row_hit = row[L_i: R_i + 1]
    row_right = row[R_i + 1: N + 1]
    row_hit = ['.' for _ in row_hit]
    row_left.extend(row_hit)
    row_left.extend(row_right)
    return(row_left)


N =random.randint(1, 20)
# print(N)
row = ['I' for _ in range(N)]
K= random.randint(1, 10)
for trying in range(K):
    row = throw(N, trying, row)
    # print('Результат:', row)
print('\nРезультат:', row)