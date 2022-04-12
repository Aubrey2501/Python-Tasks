import random


class Person:
    """
    ������� ����� �������
        Attributes:
            name (str): ���
            surname (str): �������
            age (str): �������
    """
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Employee(Person):
    """
    ����� ��������. ��������: Person, �������� ������: ��������, �����, �������
        Attributes:
            name (str): ���
            surname (str): �������
            age (str): �������
            salary (int): ��������
            position (str) - �������� ���������
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
    ����� ��������. ��������: Employee
        Attributes:
            name (str): ���
            surname (str): �������
            age (str): �������
            salary (int): ��������
            position (str) - �������� ���������
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 13000
        self.position = 'Manager'

class Agent(Employee):
    """
    ����� �����. ��������: Employee
        Attributes:
            name (str): ���
            surname (str): �������
            age (str): �������
            salary (int): ��������
            position (str): �������� ���������
            sales (int): ����� ������
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.sales = 0
        self.salary = 0
        self.position = 'Agent'

    def set_salary(self, sales):
        """������ ��� ������� ��������
        param:
            sales (int): ����� ������
        """
        self.sales = sales
        self.salary = round(5000 + 0.05 * self.sales, 2)


class Worker(Employee):
    """
    ����� �������. ��������: Employee
        Attributes:
            name (str): ���
            surname (str): �������
            age (str): �������
            salary (int): ��������
            position (str): �������� ���������
            hours_worked (int): ���������� ������������ �����
    """
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0
        self.hours_worked = 0
        self.position = 'Worker'

    def set_salary(self, hours):
        """������ ��� ������� ��������
        param:
            hours_worked (int): ���������� ������������ �����
        """
        self.hours_worked = hours
        self.salary = 100 * self.hours_worked


def init_employees (category, names):
    """
    ��������� ������������� ���������� �� ������
    :param category: ��������� ���������
    :param names: ������ � ������������� ������� ����������
    :argument employee (type): ������� ������ �� �������: Manager, Agent ��� Worker
    :return: employers_lst: ������ �� ����� ���������� �������
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


