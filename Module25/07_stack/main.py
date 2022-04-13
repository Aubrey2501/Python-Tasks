# coding: utf-8

class Stack:
    """
    Класс Стэк
    Attribute: stack (list): список с данными, поступающими извне
    """
    def __init__(self):
        self.stack = []

    def add_item(self, new_item):
        """
        Метод Добавление записи
        :param new_item: новая запись стека
        """
        self.stack.append(new_item)

    def remove_item(self):
        """
        Метод Удаление записи из стека
        :return: self.stack.pop() - удаленная последняя запись стека
        """
        return self.stack.pop()


class TaskManager:
    """
    Класс Менеджер, управляет стеком
    Attributes:
        stack (list): ссылка на элемент класса Stack
        lst (list): собственный буферный список с данными для передачи и получения записей из стека
    """
    def __init__(self):
        self.stack = my_stack
        self.lst = []

    def new_task(self, task, priority):
        """
        Метод для добавления новой записи в стек
        :param task: задача (первый элемент записи стека)
        :param priority: приоритет (второй элемент записи стека)
        """
        new_item = (task, priority)
        self.stack.add_item(new_item)

    def __str__(self):
        print_str = self.set_result()
        return print_str

    def set_result(self):
        """
        Метод формирования текстовой строки с результатом для печати,
        вызывает метод Сортировка списка
        :return: result(str): текстовая строка с результатом для вывода на консоль
        """
        self.sort_stack()
        result = 'Результат:\n'
        for item in self.lst:
            result += ' '.join((str(item[1]), item[0], '\n'))
        return result

    def sort_stack(self):
        """Метод Сортировка списка. Сортирует список задач по приоритету"""
        self.get_lst()
        self.lst = sorted(self.lst, key=lambda x: x[1])

    def get_lst(self):
        """
        Геттер для получения последовательности записей из стека
        """
        while True:
            try:
                item = self.stack.remove_item()
                self.lst.append(item)
            except IndexError:
                break


my_stack = Stack()
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# зачет!
