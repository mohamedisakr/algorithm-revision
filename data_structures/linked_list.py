# from sys import
import math  # from math import inf
from data_structures.node import Node


class LinkedList:

    # def __init__(self):
    def __init__(self, iter_values=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_val = -math.inf
        self.min_val = math.inf
        self.total_sum = 0

        if iter_values is not None:
            for item in iter_values:
                self.insert(item)

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def is_empty(self):
        return self.head is None and self.tail is None

    def show_node_list(self):
        temp_head = self.head
        while temp_head is not None:
            print(f'{temp_head.val}', end=' -> ')
            temp_head = temp_head.next
        print(f'{None}', end='')

    def max_value(self):
        return self.max_val

    def min_value(self):
        return self.min_val

    def sum_total(self):
        return self.total_sum

    def nth_node(self, n):
        if self.head is None or n < 1 or n > self.size:
            return None
        if n == 1:
            return self.head.val

        temp_head = self.head
        for i in range(1, n+1):
            if i == n:
                return temp_head.val
            temp_head = temp_head.next

        return None

    def index(self, value: int) -> int:
        if value is None or not isinstance(value, int):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        temp_head = self.head
        idx = 0
        while temp_head is not None:
            if temp_head.val == value:
                return idx
            temp_head = temp_head.next
            idx += 1
        return -1

    def index_transposition(self, value: int) -> int:
        if self.is_empty is True:
            return -1

        if value is None or not isinstance(value, int):
            raise TypeError("val must be of int data type")

        previous = None
        current = self.head
        idx = 0
        while current is not None:
            if current.val == value:
                if previous is None:
                    return idx
                previous.val, current.val = current.val, previous.val
                return idx-1
            previous, current = current, current.next
            idx += 1
        return -1

    def insert_front(self, value):
        if value is None or not isinstance(value, int) or isinstance(value, bool):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        if value is not None and value < 0:
            # raise an exception if val is not None and negative
            raise ValueError("val must be non-negative")

        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            temp_head = self.head
            self.head = new_node
            new_node.next = temp_head

        self.size += 1

        self.max_val = max(self.max_val, value)
        self.min_val = min(self.min_val, value)
        self.total_sum += value

    def insert(self, value):
        if value is None or not isinstance(value, int) or isinstance(value, bool):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        if value is not None and value < 0:
            # raise an exception if val is not None and negative
            raise ValueError("val must be non-negative")

        new_node = Node(value)

        # empty linked list
        if self.is_empty():  # self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        self.max_val = max(self.max_val, value)
        self.min_val = min(self.min_val, value)
        self.total_sum += value
