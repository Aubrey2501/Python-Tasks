from typing import List

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код

list1 = []
list2 = []
[list1.extend(nice_list[i]) for i in range(len(nice_list))]
[list2.extend(list1[i]) for i in range(len(list1))]
print('Ответ:', list2)
