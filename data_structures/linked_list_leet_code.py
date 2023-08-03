"""Design your implementation of the linked list. 
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to 
the next node.
If you want to use the doubly linked list, you will need one more attribute 
prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.
"""


# class Node:
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next

class Node:
    slots = ('val', 'prev', 'next')
    # use slots to save memory

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    """ Initializes the MyLinkedList object.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        # self.head = Node(None)  # use sentinel nodes as dummy head and tail
        # self.tail = Node(None)
        # self.head.next = self.tail
        # self.tail.prev = self.head
        # self.size = 0

    def __len__(self) -> int:
        return self.size

    def show_node_list(self):
        current = self.head
        while current is not None:
            print(f'{current.val}', end=' -> ')
            current = current.next
        print(f'{None}', end='')

    def addAtHead(self, val: int) -> None:
        """ Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked 
        list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """ Append a node of value val as the last element of the linked list.
        """

        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def get(self, index: int) -> int:
        """ Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1
        Assume all nodes in the linked list are 0-indexed.
        """
        # if the index is negative or greater than the length, do nothing
        if self.head is None:
            return -1

        if index < 0 or index > self.size-1:
            return -1

        # if the index is zero, insert at the head
        if index == 0:
            return self.head.val

        # if the index is equal to the length, insert at the tail
        if index == self.size:  # changed from index == self.size-1
            return self.tail.val

        # find the node before the index
        prev_node = self.head
        for _ in range(index):  # - 1
            prev_node = prev_node.next

        return prev_node.val

    def addAtIndex(self, index: int, val: int) -> None:
        # if the index is negative or greater than the length, do nothing
        if index < 0 or index > self.size:
            return

        # if the index is zero, insert at the head
        if index == 0:
            self.addAtHead(val)
            return

        # if the index is equal to the length, insert at the tail
        if index == self.size:  # changed from index == self.size-1
            self.addAtTail(val)
            return

        # create a new node with the given value
        new_node = Node(val)

        # otherwise, insert between two existing nodes
        # find the node before the index
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        # find the node after the index
        next_node = prev_node.next

        # link the new node with the previous and next nodes
        new_node.prev = prev_node
        new_node.next = next_node

        # link the previous and next nodes with the new node
        prev_node.next = new_node
        next_node.prev = new_node

        # increment the size of the linked list
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """ Delete the indexth node in the linked list, if the index is valid.
        Assume all nodes in the linked list are 0-indexed.
        """
        pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
