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


class TestAddAtTail(TestCase):
    def setUp(self):
        # this method runs before each test case and creates a new linked list object
        self.my_list = MyLinkedList()

    def test_add_at_tail_empty_list(self):
        # this method tests adding a node to an empty list
        self.my_list.addAtTail(10)  # add a node with value 10
        # check that the size of the list is 1
        self.assertEqual(len(self.my_list), 1)
        # check that the head node has value 10
        self.assertEqual(self.my_list.head.val, 10)
        # check that the tail node has value 10
        self.assertEqual(self.my_list.tail.val, 10)
        # check that the head node has no previous node
        self.assertIsNone(self.my_list.head.prev)
        # check that the tail node has no next node
        self.assertIsNone(self.my_list.tail.next)

    def test_add_at_tail_non_empty_list(self):
        # this method tests adding a node to a non-empty list
        self.my_list.addAtTail(10)  # add a node with value 10
        self.my_list.addAtTail(20)  # add another node with value 20

        # check that the size of the list is 2
        self.assertEqual(len(self.my_list), 2)

        # check that the head node has value 10
        self.assertEqual(self.my_list.head.val, 10)
        # check that the tail node has value 20
        self.assertEqual(self.my_list.tail.val, 20)

        # check that the head node has no previous node
        self.assertIsNone(self.my_list.head.prev)
        # check that the tail node has no next node
        self.assertIsNone(self.my_list.tail.next)

        # check that the next node of the head has value 20
        self.assertEqual(self.my_list.head.next.val, 20)
        # check that the previous node of the tail has value 10
        self.assertEqual(self.my_list.tail.prev.val, 10)

    def test_add_at_tail_negative_value(self):
        # this method tests adding a node with a negative value
        self.my_list.addAtTail(-10)  # add a node with value -10
        # check that the size of the list is 1
        self.assertEqual(len(self.my_list), 1)
        # check that the head node has value -10
        self.assertEqual(self.my_list.head.val, -10)
        # check that the tail node has value -10
        self.assertEqual(self.my_list.tail.val, -10)
        # check that the head node has no previous node
        self.assertIsNone(self.my_list.head.prev)
        # check that the tail node has no next node
        self.assertIsNone(self.my_list.tail.next)

    def test_add_at_tail_zero_value(self):
        # this method tests adding a node with a zero value
        self.my_list.addAtTail(0)  # add a node with value 0
        # check that the size of the list is 1
        self.assertEqual(len(self.my_list), 1)
        # check that the head node has value 0
        self.assertEqual(self.my_list.head.val, 0)
        # check that the tail node has value 0
        self.assertEqual(self.my_list.tail.val, 0)
        # check that the head node has no previous node
        self.assertIsNone(self.my_list.head.prev)
        # check that the tail node has no next node
        self.assertIsNone(self.my_list.tail.next)

    def test_add_at_tail_none_value(self):
        # this method tests adding a node with a None value
        self.my_list.addAtTail(None)  # add a node with value None
        # check that the size of the list is 1
        self.assertEqual(len(self.my_list), 1)
        # check that the head node has value None
        self.assertIsNone(self.my_list.head.val)
        # check that the tail node has value None
        self.assertIsNone(self.my_list.tail.val)
        # check that the head node has no previous node
        self.assertIsNone(self.my_list.head.prev)
        # check that the tail node has no next node
        self.assertIsNone(self.my_list.tail.next)

    def test_add_at_tail_one_node_list(self):
        # this method tests adding a node to a list that has only one node
        self.my_list.addAtTail(10)  # add a node with value 10
        self.my_list.addAtTail(20)  # add another node with value 20
        # check that the size of the list is 2
        self.assertEqual(len(self.my_list), 2)
        # check that the head node has value 10
        self.assertEqual(self.my_list.head.val, 10)
        # check that the tail node has value 20
        self.assertEqual(self.my_list.tail.val, 20)
        # check that the head node has no previous node
        self.assertIsNone(self.my_list.head.prev)
        # check that the tail node has no next node
        self.assertIsNone(self.my_list.tail.next)
        # check that the next node of the head has value 20
        self.assertEqual(self.my_list.head.next.val, 20)
        # check that the previous node of the tail has value 10
        self.assertEqual(self.my_list.tail.prev.val, 10)

    def tearDown(self):
        # this method runs after each test case and deletes the linked list object
        del self.my_list


# Define a test class that inherits from unittest.TestCase
class TestAddAtIndex(TestCase):

    # Write a test method that starts with test_
    def test_add_at_index_success(self):
        # Create an instance of MyLinkedList
        my_list = MyLinkedList()

        # Add some nodes to the list
        my_list.addAtHead(1)
        my_list.addAtTail(3)

        # Add a node at index 1 with value 2
        my_list.addAtIndex(1, 2)

        # Get the values of the nodes in the list
        values = []
        current = my_list.head
        while current:
            values.append(current.val)
            current = current.next
        # Check that the values match the expected result
        self.assertEqual(values, [1, 2, 3], "Should be [1, 2, 3]")

    # Write test methods that start with test_
    def test_add_at_index_success_1(self):
        # Create an instance of MyLinkedList and add some nodes
        my_list = MyLinkedList()
        my_list.addAtHead(1)
        my_list.addAtTail(3)

        # Call the addAtIndex function with a valid index and value
        my_list.addAtIndex(1, 2)

        # Check that the linked list has the expected values and size
        self.assertEqual(my_list.head.val, 1)
        self.assertEqual(my_list.head.next.val, 2)
        self.assertEqual(my_list.tail.val, 3)
        self.assertEqual(len(my_list), 3)

    def test_add_at_index_invalid(self):
        # Create an instance of MyLinkedList and add some nodes
        my_list = MyLinkedList()
        my_list.addAtHead(1)
        my_list.addAtTail(3)

        # Call the addAtIndex function with an invalid index and value
        my_list.addAtIndex(5, 4)

        # Check that the linked list has not changed
        self.assertEqual(my_list.head.val, 1)
        self.assertEqual(my_list.tail.val, 3)
        self.assertEqual(len(my_list), 2)


if __name__ == '__main__':
    main()
