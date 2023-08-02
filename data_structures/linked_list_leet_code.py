"""Design your implementation of the linked list. 
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to 
the next node.
If you want to use the doubly linked list, you will need one more attribute 
prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.
"""


class Node:
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

    def __len__(self) -> int:
        return self.size

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

    def get(self, index: int) -> int:
        """ Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1
        Assume all nodes in the linked list are 0-indexed.
        """
        pass

    def addAtTail(self, val: int) -> None:
        """ Append a node of value val as the last element of the linked list.
        """
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        """ Add a node of value val before the indexth node in the linked list. 
        If index equals the length of the linked list, the node will be appended 
        to the end of the linked list. 
        If index is greater than the length, the node will not be inserted.
        Assume all nodes in the linked list are 0-indexed.
        """
        pass

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
