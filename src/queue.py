class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:
            self.head = self.tail = Node(data, None)
        else:
            old_tail = self.tail
            self.tail = Node(data, None)
            old_tail.next_node = self.tail

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            old_head = self.head
            self.head = self.head.next_node
            return old_head.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        finished_string = ""
        temp_node = self.head
        while temp_node is not None:
            if finished_string == "":
                finished_string += str(temp_node.data)
            else:
                finished_string += f"\n{temp_node.data}"
            temp_node = temp_node.next_node
        return finished_string
