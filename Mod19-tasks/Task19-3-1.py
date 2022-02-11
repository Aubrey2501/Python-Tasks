
family = dict()
family = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children":
        [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}
while True:
    child_name = input('\nВведите имя ребенка: ')
    if child_name == 'end':
        break
    bob_srn = 'Nosurename'
    for i_child in family.get('children'):
        if i_child.get('name') == child_name:
            bob_srn = family.get('surname')
            print('Имя:', i_child.get('name'), 'Возраст:', i_child.get('age'))

    print('Фамилия:', bob_srn)

