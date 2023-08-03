class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        """Конструктор класса Node"""
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, self.tail)
        else:
            old_head = self.head
            self.head = Node(data, old_head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.insert_beginning(data)
        elif self.tail is None:
            self.tail = Node(data, None)
            self.head.next_node = self.tail
        else:
            old_tail = self.tail
            self.tail = Node(data, None)
            old_tail.next_node = self.tail

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
