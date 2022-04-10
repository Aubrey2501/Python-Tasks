class Steck:
    def __init__(self):
        self.stack = dict()

    def add_item(self, key, value):
        self.stack[key] = value

    def remove_item(self):
        try:
            return self.stack.popitem()
        except KeyError:
            return 'end of dict'

    # def take_stack(self):
    #     return self.stack

class TaskManager:
    def __init__(self, task: str, priority: int):
        self.steck = my_steck
        self.task = task
        self.priority = priority

    def new_task(self, task, priority):
        self.steck.add_item(task, priority)

    def sort_steck(self):
        sorted_tuple = sorted(self.steck.items(), key=lambda x: x[1])
        sorted_steck = dict(sorted_tuple)
        return sorted_steck

    def __str__(self):
        return self.sort_steck()


my_steck = Steck()
manager = TaskManager()
manager.new_task("������� ������", 4)
manager.new_task("������ ������", 4)
manager.new_task("���������", 1)
manager.new_task("������", 2)
manager.new_task("����� ��", 2)
print(manager)