import random
list1 = [random.randint(0, 100) for _ in range(10)]
A = random.randint(1, 10)
B = random.randint(1, 10)
# B = A
print(list1, A, B)
if A < B:
    list_new = list1[:A] + list1[B + 1:]
else:
    list_new = list1[:B] + list1[A + 1:]

print(list_new)