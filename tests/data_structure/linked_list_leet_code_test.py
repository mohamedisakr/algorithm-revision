import math
import sys
from unittest import TestCase, main
from data_structures.linked_list_leet_code import MyLinkedList


class TestAddAtHead(TestCase):

    def setUp(self):
        # Create an empty linked list before each test
        self.linked_list = MyLinkedList()

    def test_add_at_head_empty_list(self):
        # Test adding a node to an empty list
        self.linked_list.addAtHead(1)
        self.assertEqual(self.linked_list.head.val, 1)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, 1)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1)  # Check the size

    def test_add_at_head_non_empty_list(self):
        # Test adding a node to a non-empty list
        self.linked_list.addAtHead(1)  # Add a node with value 1
        self.linked_list.addAtHead(2)  # Add another node with value 2
        self.assertEqual(self.linked_list.head.val, 2)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, 1)  # Check the tail value
        self.assertEqual(len(self.linked_list), 2)  # Check the size

    def test_add_at_head_zero_value(self):
        # Test adding a node of value 0 to the list
        self.linked_list.addAtHead(0)
        self.assertEqual(self.linked_list.head.val, 0)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, 0)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1)  # Check the size

    def test_add_at_head_negative_value(self):
        # Test adding a node of value -1 to the list
        self.linked_list.addAtHead(-1)
        self.assertEqual(self.linked_list.head.val, -1)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, -1)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1)  # Check the size

    def test_add_at_head_max_value(self):
        # Test adding a node of value sys.maxsize to the list
        self.linked_list.addAtHead(sys.maxsize)
        self.assertEqual(self.linked_list.head.val,
                         sys.maxsize)  # Check the head value
        self.assertEqual(self.linked_list.tail.val,
                         sys.maxsize)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1)  # Check the size

    def test_add_at_head_max_plus_one_value(self):
        # Test adding a node of value sys.maxsize + 1 to the list
        self.linked_list.addAtHead(sys.maxsize + 1)
        self.assertEqual(self.linked_list.head.val,
                         sys.maxsize + 1)  # Check the head value
        self.assertEqual(self.linked_list.tail.val,
                         sys.maxsize + 1)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1)  # Check the size

    def test_add_at_head_same_value(self):
        # Test adding multiple nodes of the same value to the list
        self.linked_list.addAtHead(1)  # Add a node with value 1
        self.linked_list.addAtHead(1)  # Add another node with value 1
        self.assertEqual(self.linked_list.head.val, 1)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, 1)  # Check the tail value
        self.assertEqual(len(self.linked_list), 2)  # Check the size

    def test_add_at_head_large_number_of_nodes(self):
        # Test adding a large number of nodes to the list
        for i in range(1000):  # Add 1000 nodes with values from 0 to 999
            self.linked_list.addAtHead(i)
        self.assertEqual(self.linked_list.head.val,
                         999)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, 0)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1000)  # Check the size

    def test_add_at_head_existing_value(self):
        # Test adding a node of value that is already in the list
        self.linked_list.addAtHead(1)  # Add a node with value 1
        self.linked_list.addAtHead(2)  # Add another node with value 2
        self.linked_list.addAtHead(1)  # Add another node with value 1
        self.assertEqual(self.linked_list.head.val, 1)  # Check the head value
        self.assertEqual(self.linked_list.tail.val, 1)  # Check the tail value
        self.assertEqual(len(self.linked_list), 3)  # Check the size

    def test_add_at_head_max_or_min_integer_value(self):
        # Test adding a node of value that is equal to the maximum or minimum possible integer value in Python
        # Add a node with the maximum integer value
        self.linked_list.addAtHead(sys.maxsize)
        self.assertEqual(self.linked_list.head.val,
                         sys.maxsize)  # Check the head value
        self.assertEqual(self.linked_list.tail.val,
                         sys.maxsize)  # Check the tail value
        self.assertEqual(len(self.linked_list), 1)  # Check the size

        # Add a node with the minimum integer value
        self.linked_list.addAtHead(-sys.maxsize - 1)
        self.assertEqual(self.linked_list.head.val, -
                         sys.maxsize - 1)  # Check the head value
        self.assertEqual(self.linked_list.tail.val,
                         sys.maxsize)  # Check the tail value
        self.assertEqual(len(self.linked_list), 2)  # Check the size

     # def test_add_at_head_none_value(self):
    #     # Test adding a node of value None to the list
    #     with self.assertRaises(ValueError):  # Expect a ValueError exception
    #         self.linked_list.addAtHead(None)  # Try to add None value

    # def test_add_at_head_invalid_value(self):
    #     # Test adding an invalid value to the list
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         self.linked_list.addAtHead("a")  # Try to add a string value

    # def test_add_at_head_large_or_small_value(self):
    #     # Test adding a node of value that is very large or very small to the list
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         # Try to add the maximum float value
    #         self.linked_list.addAtHead(sys.float_info.max)
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         # Try to add the minimum float value
    #         self.linked_list.addAtHead(sys.float_info.min)
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         self.linked_list.addAtHead(math.inf)  # Try to add infinity value
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         # Try to add negative infinity value
    #         self.linked_list.addAtHead(-math.inf)

    # def test_add_at_head_non_integer_value(self):
    #     # Test adding a node of value that is not an integer to the list
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         self.linked_list.addAtHead(3.14)  # Try to add a float value
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         self.linked_list.addAtHead(True)  # Try to add a boolean value
    #     with self.assertRaises(TypeError):  # Expect a TypeError exception
    #         # Try to add a complex number value
    #         self.linked_list.addAtHead(1 + 2j)


if __name__ == '__main__':
    main()
