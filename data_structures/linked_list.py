from data_structures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def show_node_list(self):
        temp_head = self.head
        while temp_head is not None:
            print(f'{temp_head}', end=' -> ')
            temp_head = temp_head.next
        print(f'{None}', end='')

    def insert(self, value):
        new_node = Node(value)

        # empty linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
