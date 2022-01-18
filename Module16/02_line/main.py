# TODO здесь писать код

class1 = list(range(160, 176 + 1, 2))
class2 = list(range(162, 180 + 1, 3))
print(class1)
print(class2)
ind = 0
count_cl2 = len(class2)

for student1 in class1:
    student2 = class2[0]
    while student2 <= student1:
        ind = class1.index(student1)
        class1.insert(ind, student2)
        class2.remove(student2)
        student2 = class2[0]

for i_student2 in range(0, len(class2)):
    class1.append(class2[i_student2])

# class1.extend(class2)
# class1.sort()

print('Отсортированный список учеников:', class1)