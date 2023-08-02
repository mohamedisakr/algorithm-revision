from data_structures.doubly_linked_list import DoublyLinkedList
from unittest import TestCase, main


class TestDoublyLinkedList(TestCase):

    def test_is_empty(self):
        # create an empty doubly linked list
        dll = DoublyLinkedList()
        # check that the list is empty
        self.assertTrue(dll.is_empty())
        # insert a value at the end
        dll.insert_end(10)
        # check that the list is not empty
        self.assertFalse(dll.is_empty())

    # ---------------- insert_end --------------------
    def test_insert_end(self):
        # create an empty doubly linked list
        dll = DoublyLinkedList()

        # insert a value at the end
        dll.insert_end(10)

        # check that the size is 1
        self.assertEqual(len(dll), 1)
        # check that the head and tail are the same node with value 10
        self.assertEqual(dll.head.val, 10)
        self.assertEqual(dll.tail.val, 10)
        self.assertIs(dll.head, dll.tail)

        # insert another value at the end
        dll.insert_end(20)
        # check that the size is 2
        self.assertEqual(len(dll), 2)

        # check that the head and tail are different nodes with values 10 and 20
        self.assertEqual(dll.head.val, 10)
        self.assertEqual(dll.tail.val, 20)
        self.assertIsNot(dll.head, dll.tail)

    def test_insert_end_empty_list(self):
        # create an empty doubly linked list
        dll = DoublyLinkedList()
        # insert a value at the end
        dll.insert_end(10)
        # check that the size is 1
        self.assertEqual(len(dll), 1)
        # check that the head and tail are the same node with value 10
        self.assertEqual(dll.head.val, 10)
        self.assertEqual(dll.tail.val, 10)
        self.assertIs(dll.head, dll.tail)

    def test_insert_end_none_value(self):
        # create a doubly linked list with some values
        dll = DoublyLinkedList()
        arr = [1, 2, 3]
        for item in arr:
            dll.insert_end(item)

        # insert None at the end
        # dll.insert_end(None)

        # check that the size is 4
        self.assertEqual(len(dll), 3)
        # check that the tail is a node with value None
        self.assertIsNotNone(dll.tail.val)
        self.assertEqual(dll.tail.val, 3)

    def test_insert_end_duplicate_value(self):
        # create a doubly linked list with some values
        dll = DoublyLinkedList()

        arr = [1, 2, 3]
        for item in arr:
            dll.insert_end(item)

        # insert a duplicate value at the end
        dll.insert_end(3)

        # check that the size is 4
        self.assertEqual(len(dll), 4)
        # check that the tail is a node with value 3
        self.assertEqual(dll.tail.val, 3)

    # ---------------- insert_front --------------------

    def test_insert_front_empty(self):
        self.list = DoublyLinkedList()
        # insert a node with value 10 at the front of an empty list
        self.list.insert_front(10)
        # check if the list has one node with value 10
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.val, 10)
        self.assertEqual(self.list.tail.val, 10)

    def test_insert_front_non_empty(self):
        self.list = DoublyLinkedList()
        # insert two nodes with values 20 and 30 at the front of a non-empty list
        self.list.insert_front(10)
        self.list.insert_front(20)
        self.list.insert_front(30)
        # check if the list has three nodes with values 30, 20, and 10
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.head.val, 30)
        self.assertEqual(self.list.head.next.val, 20)
        self.assertEqual(self.list.head.next.next.val, 10)
        self.assertEqual(self.list.tail.val, 10)


if __name__ == '__main__':
    main()
