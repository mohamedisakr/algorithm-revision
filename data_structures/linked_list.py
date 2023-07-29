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

        # if not all(isinstance(item, int) for item in iter_values):
        #     raise TypeError("all elements in array must be of int data type")

        if iter_values is not None:
            for item in iter_values:
                # try:
                self.insert(item)
                # except:
                #     TypeError()
                #     ValueError()

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def __eq__(self, other):
        # check if other is a linked list
        if not isinstance(other, LinkedList):
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

    # def __eq__(self, other):
    #     # check if other is a linked list
    #     if not isinstance(other, LinkedList):
    #         return False

    #     # compare the sizes of the linked lists
    #     if self.size != other.size:
    #         return False

    #     # compare the values of the nodes in the linked lists
    #     current1 = self.head
    #     current2 = other.head
    #     while current1 and current2:
    #         if current1.val != current2.val:
    #             return False
    #         current1 = current1.next
    #         current2 = current2.next

    #     # return True if no differences are found
    #     return True

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

    def nth_node_back(self, n):
        # if self.is_empty() or n > self.size:
        #     return None
        return self.nth_node(self.size-n+1)

    def nth_node(self, n):
        if n is None or not isinstance(n, int):
            raise TypeError("n must be of int data type")

        # if self.head is None or n < 1 or n > self.size:
        if self.is_empty() or n < 1 or n > self.size:
            return None

        if n == 1:
            return self.head.val

        temp_head = self.head
        for i in range(1, n+1):
            if i == n:
                return temp_head.val
            temp_head = temp_head.next

        return None

    def get_nth_node(self, n):
        if n is None or not isinstance(n, int):
            raise TypeError("n must be of int data type")

        # if self.head is None or n < 1 or n > self.size:
        if self.is_empty() or n < 1 or n > self.size:
            return None

        if n == 1:
            return self.head

        temp_head = self.head
        for i in range(1, n+1):
            if i == n:
                return temp_head
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

    def delete_front(self):
        if self.is_empty():
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            self.max_val = -math.inf
            self.min_val = math.inf
            self.total_sum = 0
            return

        temp_head = self.head
        self.head = temp_head.next
        self.total_sum -= temp_head.val
        self.min_val = self.head.val
        self.size -= 1
        temp_head = None

    def delete_rear_simple(self):
        if self.is_empty():
            return
        if self.size == 1:
            self.delete_front()
            return

        second_last = self.get_nth_node(self.size-1)
        self.delete_nth(self.size)
        self.tail = second_last
        second_last.next = None

    def delete_rear(self):
        if self.is_empty():
            return

        if self.size <= 1:
            self.delete_front()
            return

        # del_value = self.tail.val
        # second_last = self.nth_node(self.size-1)
        # self.tail = second_last
        # second_last.next = None
        # self.size -= 1
        # self.total_sum -= del_value
        # self.max_val = self.tail.val

        # '''
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            self.max_val = -math.inf
            self.min_val = math.inf
            self.total_sum = 0
            return

        previous = None
        current = self.head
        del_value = 0

        while current is not None:
            if current.val == self.tail.val:
                del_value = current.val
                self.tail = previous
            previous, current = current, current.next
        self.size -= 1
        self.total_sum -= del_value
        self.max_val = self.tail.val
        current = None
        # '''

    def delete_nth_simple(self, n):
        if n is None or not isinstance(n, int):
            raise TypeError("n must be of int data type")

        if self.is_empty() or n < 1 or n > self.size:
            raise ValueError(f"This #{n}th node does not exist")

        if n == 1:
            self.delete_front()
            return

        if n == self.size:
            self.delete_rear()
            return

        before_nth = self.get_nth_node(n-1)
        nth_node = before_nth.next
        del_value = nth_node.val
        after_nth = nth_node.next
        before_nth.next = after_nth
        nth_node = None

        self.size -= 1
        self.total_sum -= del_value

    def delete_nth(self, n):
        if n is None or not isinstance(n, int):
            raise TypeError("n must be of int data type")

        if self.is_empty() or n < 1 or n > self.size:
            raise ValueError(f"This #{n}th node does not exist")

        if n == 1:
            self.delete_front()
            return

        if n == self.size:
            self.delete_rear()
            return

        previous = None
        current = self.head
        del_value = 0

        for i in range(1, n+1):
            if i == n:
                if current is not None and previous is None:
                    del_value = current.val
                    # current = current.next
                    self.head = current.next
                    current = None
                    self.size -= 1
                    return
                else:
                    del_value = current.val
                    previous.next = current.next
            previous, current = current, current.next

        self.size -= 1
        self.total_sum -= del_value
        current = None

    def delete_value(self, value):
        if value is None or not isinstance(value, int) or isinstance(value, bool):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        if value is not None and value < 0:
            # raise an exception if val is not None and negative
            raise ValueError("val must be non-negative")

        if self.is_empty():  # or value < 1 or value > self.size:
            return

        if value == self.head.val:
            self.delete_front()
            return

        if value == self.tail.val:
            self.delete_rear()
            return

        previous = None
        current = self.head
        del_value = 0

        while current is not None:
            if current.val == value:
                del_value = current.val
                previous.next = current.next
                self.size -= 1
                self.total_sum -= del_value
                current = None
                return

            previous, current = current, current.next

    def insert(self, value):
        if value is None or not isinstance(value, int) or isinstance(value, bool) or isinstance(value, str):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        if value is not None and value < 0:
            # raise an exception if val is not None and negative
            raise ValueError("val must be non-negative")

        '''
        if item < 0:
            raise ValueError(
                f"{item} must be of positive integer")

        if not isinstance(item, int):
            raise TypeError(
                f"all elements in {iter_values} must be of int data type")
        '''

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

    def is_identical(self, other) -> bool:
        if self.size != other.size:
            return False

        temp_head, other_head = self.head, other.head

        for i in range(self.size):
            if temp_head.val != other_head.val:
                return False
            temp_head, other_head = temp_head.next, other_head.next

        return True

    def swap_pairs(self):
        if self.is_empty():
            return

        if self.size == 1:
            return

        previous = None
        current = self.head

        while current and current.next:
            previous, current = current, current.next
            previous.val, current.val = current.val, previous.val
            current = current.next

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        # self.tail = prev
