student = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ')
student_lst = student.split()
dict_student = dict()

dict_student['Имя'] = student_lst[0]
dict_student['Фамилия'] = student_lst[1]
dict_student['Город'] = student_lst[2]
dict_student['Место учебы'] = student_lst[3]
dict_student['Оценки'] = student_lst[4:]

print('Результат:')
for i_info in dict_student:
      print(i_info, '-', dict_student[i_info])