class Node:
    def __init__(self, val: int, prev=None, next=None):
        if val is not None and not isinstance(val, int):
            # raise an exception if val is not None and not an int
            raise TypeError("val must be of int data type")

        if val is not None and val < 0:
            # raise an exception if val is not None and negative
            raise ValueError("val must be non-negative")

        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        if self.val is None or not isinstance(self.val, int):
            return ""
        return f'{self.val}'
