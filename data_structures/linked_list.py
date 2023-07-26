# from sys import
import math  # from math import inf
from data_structures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_val = -math.inf
        self.min_val = math.inf
        self.total_sum = 0

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

    def insert(self, value):
        if value is not None and not isinstance(value, int):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        if value is not None and value < 0:
            # raise an exception if val is not None and negative
            raise ValueError("val must be non-negative")

        new_node = Node(value)

        # empty linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        self.max_val = max(self.max_val, value)
        self.min_val = min(self.min_val, value)
        self.total_sum += value
