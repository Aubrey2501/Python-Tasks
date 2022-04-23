from typing import Optional, Any


class Node:
    """  Класс "Узел" """
    def __init__(self, value: Optional[Any] = None, next: Optional[Any] = None) ->None:
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node [{value}]'.format(value=str(self.value))


class LinkedList:
    """ Класс "Связанный список" """
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def append(self, value: Any) -> None:
        """
        Метод добавить узел
        Args:
            value: данные узла
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        """
        Метод удаления узла
        Args:
            index (int): индекс подлежащего удалеению узла
        """
        cur_index = 0
        cur_node = self.head
        if self.length == 0 or index >= self.length:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

            while cur_node is not None:
                if cur_index == index:
                    break

                prev = cur_node
                cur_node = cur_node.next
                cur_index += 1

            prev.next = cur_node.next
            self.length -= 1

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'Nodes: []'

    def get(self, index) -> None:
        """
        Геттер для получения содержимого узла по индексу
        Args:
            index(int): индекс узла
        """
        cur_index = 0
        cur_node = self.head
        if self.length == 0 or index >= self.length:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                return self.head.value

            while cur_node is not None:
                if cur_index == index:
                    return cur_node.value
                cur_node = cur_node.next
                cur_index += 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)