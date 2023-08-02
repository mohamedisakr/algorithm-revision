import math
from data_structures.node_doubly import Node


class DoublyLinkedList:
    def __init__(self, iter_values=None):
        self.head = None
        self.tail = None
        self.size = 0

        # if iter_values is not None:
        #     for item in iter_values:
        #         pass
        #         # self.insert(item)

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

    def __eq__(self, other):
        # check if other is a linked list
        if not isinstance(other, DoublyLinkedList):
            return False

        # compare the sizes of the linked lists
        if self.size != other.size:
            return False

        # compare the values of the nodes in the linked lists
        current1 = self.head
        current2 = other.head

        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next

        # return True if no differences are found
        return True

    def show_node_list(self):
        current = self.head
        while current is not None:
            print(f'{current.val}', end=' -> ')
            current = current.next
        print(f'{None}', end='')

    def is_empty(self):
        return self.head is None and self.tail is None

    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def insert_front(self, value):
        """Insert a new node with the given value at the front of the list."""
        new_node = Node(value)
        # connect the new node with the head
        self._link(new_node, self.head)
        self.head = new_node  # update the head pointer
        if self.size == 0:  # if the list was empty before
            self.tail = new_node  # update the tail pointer
        self.size += 1  # increment the size

    def insert_end(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self._link(self.tail, new_node)
        self.tail = new_node
        self.size += 1
