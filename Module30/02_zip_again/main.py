from typing import List


letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

my_zip = list(map(lambda x, y: (x, y), letters, numbers))
print(my_zip)

