# TODO здесь писать код
import random
N= [random.randint(0, 2) for _ in range(20)]
print('Список до сжатия:', N)

for i in N:
    if i == 0:
        N.remove(0)
        N.append(0)
# print(N)

N1 = [num for num in N if num != 0]
print('Список после сжатия:', N1)