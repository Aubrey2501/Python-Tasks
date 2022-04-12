import random


class Person:
    """
    Базовый класс Человек
        Attributes:
            name (str): имя
            surname (str): фамилия
            age (str): возраст
    """
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Employee(Person):
    """
    Класс Работник. Родитель: Person, дочерние классы: Менеджер, Агент, Рабочий
        Attributes:
            name (str): имя
            surname (str): фамилия
            age (str): возраст
            salary (int): зарплата
            position (str) - название должности
    """
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0
        self.position = ''

    def __str__(self):
        return 'Name: {}\nSurname: {}\nAge: {}\nPosition: {}\nSalary: {}\n'.format(
            self.name, self.surname, self.age, self.position, self.salary)


class Manager(Employee):
    """
    Класс Менеджер. Родитель: Employee
        Attributes:
            name (str): имя
            surname (str): фамилия
            age (str): возраст
            salary (int): зарплата
            position (str) - название должности
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 13000
        self.position = 'Manager'

class Agent(Employee):
    """
    Класс Агент. Родитель: Employee
        Attributes:
            name (str): имя
            surname (str): фамилия
            age (str): возраст
            salary (int): зарплата
            position (str): название должности
            sales (int): объем продаж
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.sales = 0
        self.salary = 0
        self.position = 'Agent'

    def set_salary(self, sales):
        """Сеттер для расчета зарплаты
        param:
            sales (int): объем продаж
        """
        self.sales = sales
        self.salary = round(5000 + 0.05 * self.sales, 2)


class Worker(Employee):
    """
    Класс Рабочий. Родитель: Employee
        Attributes:
            name (str): имя
            surname (str): фамилия
            age (str): возраст
            salary (int): зарплата
            position (str): название должности
            hours_worked (int): количество отработанных часов
    """
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0
        self.hours_worked = 0
        self.position = 'Worker'

    def set_salary(self, hours):
        """Сеттер для расчета зарплаты
        param:
            hours_worked (int): количество отработанных часов
        """
        self.hours_worked = hours
        self.salary = 100 * self.hours_worked


def init_employees (category, names):
    """
    Процедура инициализации работников из списка
    :param category: категория работника
    :param names: список с персональными данными работников
    :argument employee (type): элемент одного из классов: Manager, Agent или Worker
    :return: employers_lst: список со всеми элементами классов
    """
    employers_lst = []
    for i_person in names:
        name, surname, age = i_person.split(' ')
        if category == 0:
            employee = Manager(name, surname, age)
        elif category == 1:
            employee = Agent(name, surname, age)
        elif category == 2:
            employee = Worker(name, surname, age)

        employers_lst.append(employee)
    return employers_lst


names_file = open('names.txt', 'r')
names = names_file.read().split('\n')
names_file.close()

count = 0
for category in range(3):
    category_lst = init_employees(category, [names[i] for i in range(count, count + 3)])
    count += 3
    if category == 0:
        managers = category_lst
    elif category == 1:
        agents = category_lst
    else:
        workers = category_lst

for manager in managers:
    print(manager)
for agent in agents:
    agent.set_salary(sales=random.randint(50000, 100000))
    print(agent)
for worker in workers:
    worker.set_salary(hours=random.randint(100, 120))
    print(worker)


