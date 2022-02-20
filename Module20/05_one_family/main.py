family = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Тимофеев', 'Сергей'): 45,
    ('Левитин', 'Олег'): 28,
    ('Балаба', 'Марина'): 49
}

surname = input('Введите фамилию: ').lower()
if surname[len(surname) - 1:] == 'а':
    surname = surname[0: len(surname) - 1]
print('Члены семьи:')
found = False

for i_person, i_age in family.items():
    if surname in str(i_person).lower():
        found = True
        print(i_person[0], i_person[1], i_age)

if not found:
    print('Не найдено!')