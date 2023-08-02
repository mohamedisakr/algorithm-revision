import math


class DoublyLinkedList:
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
                pass
                # self.insert(item)

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

    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first
