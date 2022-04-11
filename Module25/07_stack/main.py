# coding: utf-8

class Stack:
    def __init__(self):
        self.stack = []

    def add_item(self, new_item):
        self.stack.append(new_item)

    def remove_item(self):
        return self.stack.pop()



class TaskManager:
    def __init__(self):
        self.stack = my_stack
        self.lst = []

    def new_task(self, task, priority):
        new_item = (task, priority)
        self.stack.add_item(new_item)

    def __str__(self):
        print_str = self.set_result()
        return print_str

    def set_result(self):
        self.sort_stack()
        result = 'Результат:\n'
        for item in self.lst:
            result += ' '.join((str(item[1]), item[0], '\n'))
        return result

    def sort_stack(self):
        self.get_lst()
        self.lst = sorted(self.lst, key=lambda x: x[1])

    def get_lst(self):
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