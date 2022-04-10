# coding: utf-8

class Steck:
    def __init__(self):
        self.stack = dict()

    def add_item(self, key, value):
        self.stack[key] = value

    def remove_item(self):
        return self.stack.popitem()

    # def take_stack(self):
    #     return self.stack

class TaskManager:

    def __init__(self):
        self.steck = my_steck
        self.dct = dict()

    def new_task(self, task, priority):
        self.steck.add_item(task, priority)

    def get_dct(self):
        while True:
            try:
                i_tuple = self.steck.remove_item()
                self.dct[i_tuple[0]] = i_tuple[1]
            except KeyError:
                break

    def sort_steck(self):
        self.get_dct()
        sorted_tuple = sorted(self.dct.items(), key=lambda x: x[1])
        self.dct.clear()
        self.dct = dict(sorted_tuple)

    def set_result(self):
        self.sort_steck()
        result = 'Результат:'
        for i_task, i_priority in self.dct.items():
            result = result.join((str(i_priority), i_task))
            print(result)
        return result

    def __str__(self):
        print_str = self.set_result()
        return print_str


my_steck = Steck()
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)