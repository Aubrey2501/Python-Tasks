class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'Person: {self._name}, Age: {self._age}'

    @property
    def age(self):
        return f'{self._age}'

    @age.setter
    def age(self, age):
        if not isinstance(age, int) or age < 0 or age >= 100:
            raise AttributeError('Недопустимое значение возраста')
        self._age = age

    def get_name(self):
        return f'The name of person is {self._name}'

    def set_name(self, name):
        self._name = name


tom = Person('Tom', 25)
print(tom.age)
tom.age = 36
print(tom.age)
print(tom)
