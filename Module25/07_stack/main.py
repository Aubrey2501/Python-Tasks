class Steck:
    def __init__(self):
        self.stack = dict()

    def add(self, key, value):
        self.stack[key] = value

    def remove(self, other):
        element = self.stack.pop()
        return element

    def __str__(self):
        return self.stack

class TaskManager:
    def __init__(self, task: str, priority: int):
        self.steck = my_steck
        self.task = task
        self.priority = priority

    def new_task(self, task, priority):
        self.steck[task] = priority



my_steck = Steck()