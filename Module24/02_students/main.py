class Student:

    def __init__(self, fio, group, grades):
        self.fio = fio
        self.group = group
        self.grades = grades
        from statistics import mean
        self.avg_grade = mean(self.grades)

    def print_info(self):
        print('Ф.И.О.: {}\nГруппа: {}\nОценки: {}\nСредний балл: {}\n'.
            format(self.fio, self.group, self.grades, self.avg_grade)
            )

def sort_by_avg(stud):
    return stud.avg_grade

import random
with open('surnames.txt', 'r') as inp_file:
    surnames_lst = [i_surname.replace('\n', '') for i_surname in inp_file]
    students_lst = [Student(fio=surnames_lst[index], group='123', grades=[random.randint(3, 5) for _ in range(5)])
                    for index in range(len(surnames_lst))]

    students_lst.sort(key=sort_by_avg)
    for i_student in students_lst:
        i_student.print_info()


