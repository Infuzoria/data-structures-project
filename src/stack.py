class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """Выводит информацию об объекте (для пользователя)"""
        start_node = self.top
        finished_string = ""
        while self.top is not None:
            finished_string += f"{self.top.data} "
            self.top = self.top.next_node
        self.top = start_node
        return finished_string

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.top is None:
            self.top = Node(data, None)
        else:
            self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        temp_node = self.top
        self.top = self.top.next_node
        return temp_node.data
