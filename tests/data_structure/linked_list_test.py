import math
from unittest import TestCase, main, makeSuite, TestSuite, TextTestRunner
from data_structures.linked_list import LinkedList


class TestLinkedListDataIntegrity(TestCase):
    def test_verify_empty_defaults(self):
        self.empty_list = LinkedList()
        self.assertEqual(self.empty_list.size, 0)
        self.assertTrue(self.empty_list.is_empty())
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)

    def test_verify_1_element(self):
        self.one_element_list = LinkedList([1])
        self.assertEqual(self.one_element_list.size, 1)
        self.assertIsNotNone(self.one_element_list.head)
        self.assertIsNotNone(self.one_element_list.tail)
        self.assertEqual(self.one_element_list.head,
                         self.one_element_list.tail)

    def test_verify_2_elements(self):
        self.two_element_list = LinkedList([1, 2])
        self.assertEqual(self.two_element_list.size, 2)
        self.assertIsNotNone(self.two_element_list.head)
        self.assertIsNotNone(self.two_element_list.tail)
        self.assertEqual(self.two_element_list.head.next,
                         self.two_element_list.tail)
        # self.assertEqual(self.two_element_list.size, len(self._debug_data))


class TestLinkedList(TestCase):

    def setUp(self):
        # This method runs before each test method and creates a sample linked list
        self.list = LinkedList()
        self.list.insert(1)
        self.list.insert(2)
        self.list.insert(3)

    def test_init(self):
        # This method tests the initialization of the linked list
        self.assertEqual(self.list.head.val, 1, "The head value should be 1")
        self.assertEqual(self.list.tail.val, 3, "The tail value should be 3")
        self.assertEqual(len(self.list), 3, "The length should be 3")

    def test_init_fill_with_array(self):
        arr = [1, 2, 3]
        self.list = LinkedList(arr)

        # This method tests the initialization of the linked list
        self.assertEqual(self.list.head.val, 1, "The head value should be 1")
        self.assertEqual(self.list.tail.val, 3, "The tail value should be 3")
        self.assertEqual(len(self.list), 3, "The length should be 3")

    def test_insert(self):
        # This method tests the insert method of the linked list
        self.list.insert(4)
        self.assertEqual(self.list.tail.val, 4, "The tail value should be 4")
        self.assertEqual(len(self.list), 4, "The length should be 4")

    def test_show_node_list(self):
        # This method tests the show_node_list method of the linked list
        # It captures the output of the print function using a StringIO object
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        self.list.show_node_list()
        sys.stdout = sys.__stdout__
        expected_output = "1 -> 2 -> 3 -> None"
        self.assertEqual(output.getvalue().strip(), expected_output,
                         "The output should match the expected output")

    def test_init_empty(self):
        # This method tests the initialization of an empty linked list
        empty_list = LinkedList()
        self.assertIsNone(empty_list.head, "The head should be None")
        self.assertIsNone(empty_list.tail, "The tail should be None")
        self.assertEqual(len(empty_list), 0, "The length should be 0")

    def test_insert_none(self):
        # This method tests the insert method with a None value
        with self.assertRaises(TypeError):
            # try to create a node with a non-numeric value
            self.list.insert(None)

    def test_insert_negative(self):
        with self.assertRaises(ValueError):
            # try to create a node with a negative value
            self.list.insert(-1)

    def test_show_node_list_empty(self):
        # This method tests the show_node_list method with an empty linked list
        # It captures the output of the print function using a StringIO object
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        empty_list = LinkedList()
        empty_list.show_node_list()
        sys.stdout = sys.__stdout__
        expected_output = "None"
        self.assertEqual(output.getvalue().strip(), expected_output,
                         "The output should match the expected output")

    def test_length(self):
        self.list.insert(10)
        self.list.insert(20)
        self.list.insert(30)

        # check if the size is updated correctly
        # self.assertEqual(self.list.size, 3)
        self.assertEqual(len(self.list), 6)

    def test_insert_error(self):
        # This method tests if the insert method raises an error when the
        # list is fulist
        # You can use self.assertRaises to check if an exception is
        # raised
        for i in range(10):
            self.list.insert(i)
        # check if a ValueError is raised when inserting more than 10
        # elements
        # with self.assertRaises(ValueError):
        #     self.list.insert(10)
        self.list.insert(10)
        self.assertEqual(len(self.list), 14)

    def test_nth_node(self):
        # create a linked list with some nodes
        my_list = LinkedList()
        my_list.insert(1)
        my_list.insert(2)
        my_list.insert(3)

        # my_list.show_node_list()

        # check that the nth node function returns the correct node data
        self.assertEqual(my_list.nth_node(1), 1)  # first node
        self.assertEqual(my_list.nth_node(2), 2)  # second node
        self.assertEqual(my_list.nth_node(3), 3)  # third node

    def test_nth_node_out_of_range(self):
        # create a linked list with some nodes
        my_list = LinkedList()
        my_list.insert(1)
        my_list.insert(2)
        my_list.insert(3)

        # my_list.show_node_list()

        self.assertIsNone(my_list.nth_node(0))
        self.assertIsNone(my_list.nth_node(4))

    def test_empty_list(self):
        # create an empty linked list
        my_list = LinkedList()

        self.assertIsNone(my_list.nth_node(0))
        self.assertIsNone(my_list.nth_node(1))
        self.assertIsNone(my_list.nth_node(-1))

    def test_negative_n(self):
        # create a linked list with some nodes
        my_list = LinkedList()
        my_list.insert(1)
        my_list.insert(2)
        my_list.insert(3)

        self.assertIsNone(my_list.nth_node(-1))
        self.assertIsNone(my_list.nth_node(-2))
        self.assertIsNone(my_list.nth_node(-3))

    def test_large_n(self):
        # create a linked list with some nodes
        my_list = LinkedList()
        my_list.insert(1)
        my_list.insert(2)
        my_list.insert(3)

        self.assertIsNone(my_list.nth_node(4))
        self.assertIsNone(my_list.nth_node(5))
        self.assertIsNone(my_list.nth_node(6))

    def test_one_node_list(self):
        # create a linked list with one node
        my_list = LinkedList()
        my_list.insert(1)

        # check that the nth node function returns the only node data
        self.assertEqual(my_list.nth_node(1), 1)  # first and only node

        self.assertIsNone(my_list.nth_node(0))
        self.assertIsNone(my_list.nth_node(2))

    def test_index_found(self):
        # Test if the function returns the correct index for a value that is in the list
        # The first node has value 1 and index 0
        self.assertEqual(self.list.index(1), 0)
        # The third node has value 3 and index 2
        self.assertEqual(self.list.index(3), 2)

    def test_index_not_found(self):
        # Test if the function returns -1 for a value that is not in the list
        # There is no node with value 5 in the list
        self.assertEqual(self.list.index(5), -1)
        # There is no node with value -1 in the list
        self.assertEqual(self.list.index(-1), -1)

    def test_index_empty_list(self):
        # Test if the function returns -1 for an empty list
        empty_list = LinkedList()  # Create an empty linked list
        # There is no node in the empty list
        self.assertEqual(empty_list.index(1), -1)

    def test_index_invalid_argument(self):
        # Test if the function raises a TypeError for an invalid argument
        with self.assertRaises(TypeError):
            # None is not a valid value to search for in the list
            self.list.index(None)

    def test_index_first_last(self):
        # Test if the function returns the correct index for the first and last node in the list
        # The first node has value 1 and index 0
        self.assertEqual(self.list.index(1), 0)
        # The last node has value 4 and index 3
        self.assertEqual(self.list.index(3), 2)

    def test_index_duplicate_value(self):
        # Test if the function returns the index of the first occurrence of a duplicate value in the list
        # Add another node with value 2 at the end of the list
        self.list.insert(2)
        # The first node with value 2 has index 1
        self.assertEqual(self.list.index(2), 1)

    def test_index_single_node(self):
        # Test if the function returns 0 for a single-node list
        single_list = LinkedList()  # Create a single-node linked list
        single_list.insert(5)  # Add a node with value 5
        # The only node has value 5 and index 0
        self.assertEqual(single_list.index(5), 0)

    def test_index_non_integer_value_string(self):
        # Test if the function works for non-integer values in the list
        # Add a node with a string value at the end of the list
        with self.assertRaises(TypeError):
            # None is not a valid value to search for in the list
            self.list.insert('a')

    def test_index_non_integer_value_boolean(self):
        # Add a node with a boolean value at the end of the list
        with self.assertRaises(TypeError):
            self.list.insert(True)

        # # # The node with vst.index(True), 3)

    def test_index_negative_value(self):
        # Test if the function works for negative values in the list
        # Add a node with a negative value at the end of the list
        with self.assertRaises(ValueError):
            self.list.insert(-3)
        # The node with value st.index(-3), 3)

    def test_index_zero_value(self):
        # Test if the function works for zero value in the list
        # Add a node with zero value at the end of the list
        self.list.insert(0)

        # The node with value 0 has index 5
        self.assertEqual(self.list.index(0), 3)

    def test_index_large_value(self):
        # Test if the function works for large values in the list
        # Add a node with a large value at the end of the list
        self.list.insert(1000000)

        # The node with value 1000000 has index 6
        self.assertEqual(self.list.index(1000000), 3)

    def test_index_transposition_valid(self):
        # test the function with a valid value that exists in the list
        index = self.list.index_transposition(3)
        # the value 30 should be swapped with 20 and return index 1
        self.assertEqual(index, 1)
        # self.assertEqual(self.list.get_name, 20) # the value at index 2 should be 20 after swapping

    def test_index_transposition_invalid(self):
        # test the function with an invalid value that does not exist in the list
        index = self.list.index_transposition(60)
        # the function should return -1 if the value is not found
        self.assertEqual(index, -1)

    def test_index_transposition_type_error(self):
        # test the function with an invalid type of value that is not an integer
        # the function should raise a TypeError if the value is not an integer
        with self.assertRaises(TypeError):
            self.list.index_transposition("hello")

    def test_index_transposition_head(self):
        # test the function with the value at the head of the list
        index = self.list.index_transposition(1)
        # the function should return 0 if the value is at the head of the list
        self.assertEqual(index, 0)
        # the value at the head of the list should not

    def test_index_transposition_empty(self):
        # test the function with an empty list
        empty_list = LinkedList()  # create an empty list
        index = empty_list.index_transposition(10)
        # the function should return -1 if the list is empty
        self.assertEqual(index, -1)
        self.assertIsNone(empty_list.head)  # the list should remain empty

    def test_index_transposition_tail(self):
        # test the function with the value at the tail of the list
        index = self.list.index_transposition(3)
        # the function should return 3 if the value is at the tail of the list
        self.assertEqual(index, 1)

    def test_index_transposition_negative(self):
        # test the function with a negative value that does not exist
        # in the list
        index = self.list.index_transposition(-10)
        # the function should return -1 if the value is not found
        self.assertEqual(index, -1)

    def test_index_transposition_none(self):
        # test the function with a None value that is not valid
        # the function should raise a TypeError if the value is None
        with self.assertRaises(TypeError):
            self.list.index_transposition(None)

    def test_index_transposition_duplicate(self):
        # test the function with a value that appears more than once in the list
        self.list.insert(40)  # add another 30 to the end of the list
        index = self.list.index_transposition(40)
        # the function should return 1 if the value is the first occurrence of 30 in the list
        self.assertEqual(index, 2)

    def test_index_transposition_zero(self):
        # test the function with a zero value that exists in the list
        self.list.insert(0)  # add a zero to the end of the list
        index = self.list.index_transposition(0)

        # the function should return 4 if the value is zero at the end of the list
        self.assertEqual(index, 2)

    # def test_random_n(self):
    #     # create a linked list with some random nodes
    #     my_list = LinkedList()
    #     for i in range(10):
    #         # insert random numbers from 1 to 100
    #         my_list.insert(randint(1, 100))

    #     # check that the nth node function returns the correct node data for some random n
    #     for i in range(10):
    #         n = randint(1, 10)  # generate random n from 1 to 10
    #         # compare with the get_data method
    #         self.assertEqual(my_list.nth_node(n), my_list.get_data(n))

    def test_insert_front_empty(self):
        self.list = LinkedList()
        # Test inserting a value to an empty list
        self.list.insert_front(10)
        # Check if the head and tail are the same node
        self.assertEqual(self.list.head, self.list.tail)
        # Check if the node has the correct value
        self.assertEqual(self.list.head.val, 10)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 1)
        self.assertEqual(self.list.max_val, 10)
        self.assertEqual(self.list.min_val, 10)
        self.assertEqual(self.list.total_sum, 10)

    def test_insert_front_non_empty(self):
        self.list = LinkedList()

        # Test inserting a value to a non-empty list
        self.list.insert(5)  # Insert a value at the end
        self.list.insert_front(10)  # Insert a value at the front
        # Check if the head and tail are different nodes
        self.assertNotEqual(self.list.head, self.list.tail)
        # Check if the head node has the correct value
        self.assertEqual(self.list.head.val, 10)
        # Check if the second node has the correct value
        self.assertEqual(self.list.head.next.val, 5)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 2)

    def test_insert_front_error(self):
        self.list = LinkedList()

        # Test inserting more than 10 values to the list
        for i in range(10):
            self.list.insert(i)  # Insert 10 values at the end
        # Expect a ValueError when inserting another value at the front
        # with self.assertRaises(ValueError):
        self.list.insert_front(10)
        self.assertEqual(self.list.head.val, 10)

    def test_insert_front_negative(self):
        self.list = LinkedList()

        # Test inserting a negative value to the list
        with self.assertRaises(ValueError):
            self.list.insert_front(-10)

        # # Check if the head node has the correct value
        # self.assertEqual(self.list.head.val, -10)
        # # Check if the size, max_val, min_val, and total_sum are updated correctly
        # self.assertEqual(self.list.size, 1)

    def test_insert_front_zero(self):
        self.list = LinkedList()

        # Test inserting a zero value to the list
        self.list.insert_front(0)
        # Check if the head node has the correct value
        self.assertEqual(self.list.head.val, 0)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 1)

    def test_insert_front_duplicate(self):
        self.list = LinkedList()

        # Test inserting a duplicate value to the list
        self.list.insert(10)  # Insert a value at the end
        self.list.insert_front(10)  # Insert the same value at the front
        # Check if the head and tail are different nodes
        self.assertNotEqual(self.list.head, self.list.tail)

        # Check if the head and tail nodes have the same value
        self.assertEqual(self.list.head.val, 10)
        self.assertEqual(self.list.tail.val, 10)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 2)

    def test_insert_front_traditional(self):
        self.list = LinkedList([4])

        # Test inserting a duplicate value to the list
        self.list.insert_front(3)  # Insert the same value at the front
        self.list.insert_front(2)  # Insert the same value at the front
        self.list.insert_front(1)  # Insert the same value at the front

        # Check if the head and tail are different nodes
        self.assertNotEqual(self.list.head, self.list.tail)

        # Check if the head and tail nodes have the same value
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 4)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 4)

    def test_insert_front_none(self):
        self.list = LinkedList()

        # Test inserting a None value to the list
        # Expect a TypeError when inserting None at the front
        with self.assertRaises(TypeError):
            self.list.insert_front(None)

    # ... previous test methods ...

    def test_insert_front_large(self):
        self.list = LinkedList()

        # Test inserting a large value to the list
        self.list.insert_front(1000)
        # Check if the head node has the correct value
        self.assertEqual(self.list.head.val, 1000)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 1)
        self.assertEqual(self.list.max_val, 1000)
        self.assertEqual(self.list.min_val, 1000)
        self.assertEqual(self.list.total_sum, 1000)

    def test_insert_front_small(self):
        self.list = LinkedList()

        # Test inserting a small value to the list
        with self.assertRaises(ValueError):
            self.list.insert_front(-1000)
            # self.list.insert_front(-10)

    def test_insert_front_non_integer(self):
        self.list = LinkedList()

        # Test inserting a non-integer value to the list
        # Expect a TypeError when inserting a string at the front
        with self.assertRaises(TypeError):
            self.list.insert_front("hello")
        # Expect a TypeError when inserting a float at the front
        with self.assertRaises(TypeError):
            self.list.insert_front(3.14)

    def test_insert_front_duplicate_multiple(self):
        self.list = LinkedList()

        # Test inserting a value that is already in the list multiple times
        for i in range(5):
            self.list.insert(10)  # Insert 10 five times at the end
        self.list.insert_front(10)  # Insert 10 at the front
        # Check if the head and tail nodes have the same value
        self.assertEqual(self.list.head.val, 10)
        self.assertEqual(self.list.tail.val, 10)
        # Check if the size, max_val, min_val, and total_sum are updated correctly
        self.assertEqual(self.list.size, 6)
        self.assertEqual(self.list.max_val, 10)
        self.assertEqual(self.list.min_val, 10)
        self.assertEqual(self.list.total_sum, 60)

    def test_insert_front_equal_max_min(self):
        self.list = LinkedList()

        # Test inserting a value that is equal to the max_val or min_val of the list
        self.list.insert(5)  # Insert 5 at the end
        self.list.insert(10)  # Insert 10 at the end
        self.list.insert_front(5)  # Insert 5 at the front
        self.list.insert_front(10)  # Insert 10 at the front
        # Check if the head and tail nodes have different values
        self.assertEqual(self.list.head.val, self.list.tail.val)
        # Check if the head and second nodes have the same value as max_val
        self.assertEqual(self.list.head.val, 10)
        self.assertEqual(self.list.head.next.val, 5)
        # self.assertEqual(self.list.max_val, 10)
        # Check if the third and tail nodes have the same value as min_val
        self.assertEqual(self.list.head.next.next.val, 5)
        self.assertEqual(self.list.tail.val, 10)
        # self.assertEqual(self.list.min_val, 5)
        # Check if the size and total_sum are updated correctly
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.total_sum, 30)

        # delete front
    def test_delete_front_non_empty(self):
        # create a linked list with three nodes
        my_list = LinkedList([1, 2, 3])
        # delete the front node
        my_list.delete_front()
        # check that the head is now 2
        self.assertEqual(my_list.head.val, 2)
        # check that the tail is still 3
        self.assertEqual(my_list.tail.val, 3)
        # check that the size is now 2
        self.assertEqual(my_list.size, 2)
        # check that the sum is now 5
        self.assertEqual(my_list.total_sum, 5)

    def test_delete_front_empty(self):
        # create an empty list
        my_list = LinkedList()
        # try to delete the front node
        my_list.delete_front()
        # check that the head is still None
        self.assertIsNone(my_list.head)
        # check that the tail is still None
        self.assertIsNone(my_list.tail)
        # check that the size is still 0
        self.assertEqual(my_list.size, 0)
        # check that the sum is still 0
        self.assertEqual(my_list.total_sum, 0)

    def test_delete_front_single(self):
        # create a list with one node
        my_list = LinkedList([5])
        # delete the front node
        my_list.delete_front()
        # check that the head is now None
        self.assertIsNone(my_list.head)
        # check that the tail is now None
        self.assertIsNone(my_list.tail)
        # check that the size is now 0
        self.assertEqual(my_list.size, 0)
        # check that the sum is now 0
        self.assertEqual(my_list.total_sum, 0)

    def test_delete_front_negative(self):
        # create a list with negative values
        my_list = LinkedList([1, 2, 3])
        # delete the front node
        my_list.delete_front()
        # check that the head is now 2
        self.assertEqual(my_list.head.val, 2)
        # check that the tail is still 3
        self.assertEqual(my_list.tail.val, 3)
        # check that the size is now 2
        self.assertEqual(my_list.size, 2)
        # check that the sum is now 5
        self.assertEqual(my_list.total_sum, 5)

    # def test_delete_front_exception(self):
    #     # create a list with an invalid value
    #     my_list = LinkedList([1, 2, "a"])
    #     # try to delete the front node
    #     with self.assertRaises(TypeError):
    #         my_list.delete_front()

    # ------------- nth_node_back --------------------

    def test_nth_node_back_valid(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with valid inputs
        self.assertEqual(self.list.nth_node_back(1), 5)  # last node
        self.assertEqual(self.list.nth_node_back(3), 3)  # third node from back
        self.assertEqual(self.list.nth_node_back(5), 1)  # first node

    def test_nth_node_back_invalid(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with invalid inputs
        self.assertIsNone(self.list.nth_node_back(0))  # n should be positive
        # n should not exceed list size
        self.assertIsNone(self.list.nth_node_back(6))
        # n should not be negative
        self.assertIsNone(self.list.nth_node_back(-1))

    def test_nth_node_back_empty(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with an empty list
        empty_list = LinkedList()
        self.assertIsNone(empty_list.nth_node_back(1))  # no nodes in list

    # def setUp(self):
    #     # create a sample linked list with 5 nodes
    #     self.list = LinkedList([1, 2, 3, 4, 5])

    def test_nth_node_back_valid_1(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with valid inputs
        self.assertEqual(self.list.nth_node_back(1), 5)  # last node
        self.assertEqual(self.list.nth_node_back(3), 3)  # third node from back
        self.assertEqual(self.list.nth_node_back(5), 1)  # first node

    def test_nth_node_back_invalid_1(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with invalid inputs
        self.assertIsNone(self.list.nth_node_back(0))  # n should be positive
        # n should not exceed list size
        self.assertIsNone(self.list.nth_node_back(6))
        # n should not be negative
        self.assertIsNone(self.list.nth_node_back(-1))

    def test_nth_node_back_empty_1(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with an empty list
        empty_list = LinkedList()
        self.assertIsNone(empty_list.nth_node_back(1))  # no nodes in list

    def test_nth_node_back_none(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with None as input
        # self.assertIsNone(self.list.nth_node_back(None)) # n should be an integer
        with self.assertRaises(TypeError):
            self.list.nth_node_back(None)

    def test_nth_node_back_non_integer(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with non-integer inputs
        # self.assertIsNone(self.list.nth_node_back('a'))  # n should be an integer
        # self.assertIsNone(self.list.nth_node_back(3.5))  # n should be an integer

        with self.assertRaises(TypeError):
            self.list.nth_node_back('a')
            self.list.nth_node_back(3.5)

    def test_nth_node_back_large_small(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with very large or very small inputs
        # n should not exceed list size
        self.assertIsNone(self.list.nth_node_back(1000000))
        self.assertIsNone(self.list.nth_node_back(-1000000))
        # n should not be negative

    def test_nth_node_back_equal_size(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # test the function with input equal to list size
        self.assertEqual(self.list.nth_node_back(5), 1)  # same as first node

    # ------------- is_identical ---------------

    def test_is_identical_empty_lists(self):
        # Create two empty linked lists
        list1 = LinkedList()
        list2 = LinkedList()

        # Check that is_identical returns True for empty lists
        self.assertTrue(list1.is_identical(list2))

    def test_is_identical_equal_lists(self):
        # Create two linked lists with identical data
        list1 = LinkedList([1, 2, 3])
        list2 = LinkedList([1, 2, 3])

        # Check that is_identical returns True for equal lists
        self.assertTrue(list1.is_identical(list2))

    def test_is_identical_different_lengths(self):
        # Create two linked lists with different lengths
        list1 = LinkedList([1, 2, 3])
        list2 = LinkedList([1, 2])

        # Check that is_identical returns False for lists with different lengths
        self.assertFalse(list1.is_identical(list2))

    def test_is_identical_different_values(self):
        # Create two linked lists with different values
        list1 = LinkedList([1, 2, 3])
        list2 = LinkedList([4, 5, 6])

        # Check that is_identical returns False for lists with different values
        self.assertFalse(list1.is_identical(list2))

    def test_is_identical_different_data_types(self):
        # Create two linked lists with different data types
        list1 = LinkedList([1, 2, 3])
        list2 = LinkedList([10, 20, 30])

        # Check that is_identical returns False for lists with different data types
        self.assertFalse(list1.is_identical(list2))

   # ------------- delete_rear ---------------

    def test_delete_rear_empty(self):
        # test deleting from an empty list
        lst = LinkedList()
        lst.delete_rear()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(lst.size, 0)

    def test_delete_rear_one(self):
        # test deleting from a list with one element
        lst = LinkedList([1])
        lst.delete_rear()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(lst.size, 0)

    def test_delete_rear_many(self):
        # test deleting from a list with many elements
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.delete_rear()
        self.assertEqual(lst.head.val, 1)
        self.assertEqual(lst.tail.val, 4)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_negative(self):
        # test deleting from a list with negative values
        # lst = LinkedList([-1, -2, -3, -4, -5])
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.delete_rear()
        self.assertEqual(lst.head.val, 1)
        self.assertEqual(lst.tail.val, 4)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_none(self):
        # test deleting from a list with None values
        with self.assertRaises(TypeError):
            lst = LinkedList([None, 1, None, 2, None])
            # self.list.nth_node_back('a')
        # lst.delete_rear()
        # self.assertEqual(lst.head.val, None)
        # self.assertEqual(lst.tail.val, 2)
        # self.assertEqual(lst.size, 4)

    def test_delete_rear_sorted(self):
        # test deleting from a sorted list
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.delete_rear()
        self.assertEqual(lst.head.val, 1)
        self.assertEqual(lst.tail.val, 4)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_reverse_sorted(self):
        # test deleting from a reverse sorted list
        lst = LinkedList([5, 4, 3, 2, 1])
        lst.delete_rear()
        self.assertEqual(lst.head.val, 5)
        self.assertEqual(lst.tail.val, 2)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_mixed(self):
        # test deleting from a list with mixed types
        with self.assertRaises(TypeError):
            lst = LinkedList([1, "a", True, None, 3.14])
        # with self.assertRaises(TypeError):
        #     lst.delete_rear()
        # self.assertEqual(lst.head.val, 1)
        # self.assertEqual(lst.tail.val, None)
        # self.assertEqual(lst.size, 4)

    def test_delete_rear_duplicate(self):
        # test deleting from a list with duplicate values
        lst = LinkedList([1, 2, 2, 3, 3])
        lst.delete_rear()
        # lst.show_node_list()
        self.assertEqual(lst.head.val, 1)
        # self.assertEqual(lst.tail.val, 3)
        self.assertEqual(lst.size, 4)

   # ------------- delete_rear_simple ---------------

    def test_delete_rear_simple_empty(self):
        # test deleting from an empty list
        lst = LinkedList()
        lst.delete_rear_simple()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(lst.size, 0)

    def test_delete_rear_simple_one(self):
        # test deleting from a list with one element
        lst = LinkedList([1])
        lst.delete_rear_simple()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(lst.size, 0)

    def test_delete_rear_simple_many(self):
        # test deleting from a list with many elements
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.delete_rear_simple()
        self.assertEqual(lst.head.val, 1)
        self.assertEqual(lst.tail.val, 4)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_simple_negative(self):
        # test deleting from a list with negative values
        # lst = LinkedList([-1, -2, -3, -4, -5])
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.delete_rear_simple()
        self.assertEqual(lst.head.val, 1)
        self.assertEqual(lst.tail.val, 4)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_simple_none(self):
        # test deleting from a list with None values
        with self.assertRaises(TypeError):
            lst = LinkedList([None, 1, None, 2, None])
            # self.list.nth_node_back('a')
        # lst.delete_rear_simple()
        # self.assertEqual(lst.head.val, None)
        # self.assertEqual(lst.tail.val, 2)
        # self.assertEqual(lst.size, 4)

    def test_delete_rear_simple_sorted(self):
        # test deleting from a sorted list
        lst = LinkedList([1, 2, 3, 4, 5])
        lst.delete_rear_simple()
        self.assertEqual(lst.head.val, 1)
        self.assertEqual(lst.tail.val, 4)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_simple_reverse_sorted(self):
        # test deleting from a reverse sorted list
        lst = LinkedList([5, 4, 3, 2, 1])
        lst.delete_rear_simple()
        self.assertEqual(lst.head.val, 5)
        self.assertEqual(lst.tail.val, 2)
        self.assertEqual(lst.size, 4)

    def test_delete_rear_simple_mixed(self):
        # test deleting from a list with mixed types
        with self.assertRaises(TypeError):
            lst = LinkedList([1, "a", True, None, 3.14])
        # with self.assertRaises(TypeError):
        #     lst.delete_rear_simple()
        # self.assertEqual(lst.head.val, 1)
        # self.assertEqual(lst.tail.val, None)
        # self.assertEqual(lst.size, 4)

    def test_delete_rear_simple_duplicate(self):
        # test deleting from a list with duplicate values
        lst = LinkedList([1, 2, 2, 3, 3])
        lst.delete_rear_simple()
        # lst.show_node_list()
        self.assertEqual(lst.head.val, 1)
        # self.assertEqual(lst.tail.val, 3)
        self.assertEqual(lst.size, 4)

    # ------------------------- delete_nth --------------------------------

    def test_delete_nth_first(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete the first node and check if the head is updated
        self.list.delete_nth(1)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.head.val, 2)

    def test_delete_nth_last(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # delete the last node and check if the tail is updated
        self.list.delete_nth(4)
        self.assertEqual(self.list.tail.val, 5)

    def test_delete_nth_middle(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # delete a middle node and check if the size is reduced
        self.list.delete_nth(2)
        self.assertEqual(self.list.size, 4)

    def test_delete_nth_invalid(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # delete an invalid node and check if nothing changes
        with self.assertRaises(ValueError):
            self.list.delete_nth(10)
        # self.assertEqual(self.list.size, 5)

    def test_delete_nth_empty(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # create an empty linked list and try to delete any node
        empty_list = LinkedList()

        self.assertIsNone(empty_list.head)
        self.assertIsNone(empty_list.tail)
        self.assertEqual(empty_list.size, 0)
        self.assertEqual(empty_list.max_val, -math.inf)
        self.assertEqual(empty_list.min_val, math.inf)
        self.assertEqual(empty_list.total_sum, 0)

        with self.assertRaises(ValueError):
            empty_list.delete_nth(1)

    def test_delete_nth_negative(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # try to delete a negative node and check if nothing changes

        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 5)
        self.assertEqual(self.list.size, 5)
        self.assertEqual(self.list.max_val, 5)
        self.assertEqual(self.list.min_val, 1)
        self.assertEqual(self.list.total_sum, 15)

        with self.assertRaises(ValueError):
            self.list.delete_nth(-1)

    def test_delete_nth_zero(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # try to delete the zeroth node and check if nothing changes
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 5)
        self.assertEqual(self.list.size, 5)
        self.assertEqual(self.list.max_val, 5)
        self.assertEqual(self.list.min_val, 1)
        self.assertEqual(self.list.total_sum, 15)

        with self.assertRaises(ValueError):
            self.list.delete_nth(0)

    def test_delete_nth_one_element(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # create a linked list with one element and delete it
        one_element_list = LinkedList([10])
        one_element_list.delete_nth(1)
        self.assertIsNone(one_element_list.head)
        self.assertIsNone(one_element_list.tail)
        self.assertEqual(one_element_list.size, 0)
        self.assertEqual(one_element_list.max_val, -math.inf)
        self.assertEqual(one_element_list.min_val, math.inf)
        self.assertEqual(one_element_list.total_sum, 0)

    # def setUp(self):
    #     # create a sample linked list with values 1, 2, 3, 4, 5
    #     self.list = LinkedList([1, 2, 3, 4, 5])

    def test_delete_nth_max_val(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete the node with the maximum value and check if the max_val is updated
        self.list.delete_nth(5)
        self.assertEqual(self.list.max_val, 4)

        # delete the node with the new maximum value and check if the max_val is updated
        self.list.delete_nth(4)
        self.assertEqual(self.list.max_val, 3)

    def test_delete_nth_min_val(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete the node with the minimum value and check if the min_val is updated
        self.list.delete_nth(1)
        self.assertEqual(self.list.min_val, 2)

        # delete the node with the new minimum value and check if the min_val is updated
        self.list.delete_nth(1)
        self.assertEqual(self.list.min_val, 3)

    def test_delete_nth_total_sum(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete a node and check if the total_sum is reduced by its value
        self.list.delete_nth(3)
        self.assertEqual(self.list.total_sum, 12)

        # delete another node and check if the total_sum is reduced by its value
        self.list.delete_nth(2)
        self.assertEqual(self.list.total_sum, 10)

    # ------------------------- delete_nth_simple --------------------------------

    def test_delete_nth_simple_first(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete the first node and check if the head is updated
        self.list.delete_nth_simple(1)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.head.val, 2)

    def test_delete_nth_simple_last(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # delete the last node and check if the tail is updated
        self.list.delete_nth_simple(4)
        self.assertEqual(self.list.tail.val, 5)

    def test_delete_nth_simple_middle(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # delete a middle node and check if the size is reduced
        self.list.delete_nth_simple(2)
        self.assertEqual(self.list.size, 4)

    def test_delete_nth_simple_invalid(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # delete an invalid node and check if nothing changes
        with self.assertRaises(ValueError):
            self.list.delete_nth_simple(10)
        # self.assertEqual(self.list.size, 5)

    def test_delete_nth_simple_empty(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # create an empty linked list and try to delete any node
        empty_list = LinkedList()

        self.assertIsNone(empty_list.head)
        self.assertIsNone(empty_list.tail)
        self.assertEqual(empty_list.size, 0)
        self.assertEqual(empty_list.max_val, -math.inf)
        self.assertEqual(empty_list.min_val, math.inf)
        self.assertEqual(empty_list.total_sum, 0)

        with self.assertRaises(ValueError):
            empty_list.delete_nth_simple(1)

    def test_delete_nth_simple_negative(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # try to delete a negative node and check if nothing changes

        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 5)
        self.assertEqual(self.list.size, 5)
        self.assertEqual(self.list.max_val, 5)
        self.assertEqual(self.list.min_val, 1)
        self.assertEqual(self.list.total_sum, 15)

        with self.assertRaises(ValueError):
            self.list.delete_nth_simple(-1)

    def test_delete_nth_simple_zero(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # try to delete the zeroth node and check if nothing changes
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 5)
        self.assertEqual(self.list.size, 5)
        self.assertEqual(self.list.max_val, 5)
        self.assertEqual(self.list.min_val, 1)
        self.assertEqual(self.list.total_sum, 15)

        with self.assertRaises(ValueError):
            self.list.delete_nth_simple(0)

    def test_delete_nth_simple_one_element(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # create a linked list with one element and delete it
        one_element_list = LinkedList([10])
        one_element_list.delete_nth_simple(1)
        self.assertIsNone(one_element_list.head)
        self.assertIsNone(one_element_list.tail)
        self.assertEqual(one_element_list.size, 0)
        self.assertEqual(one_element_list.max_val, -math.inf)
        self.assertEqual(one_element_list.min_val, math.inf)
        self.assertEqual(one_element_list.total_sum, 0)

    # def setUp(self):
    #     # create a sample linked list with values 1, 2, 3, 4, 5
    #     self.list = LinkedList([1, 2, 3, 4, 5])

    def test_delete_nth_simple_max_val(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete the node with the maximum value and check if the max_val is updated
        self.list.delete_nth_simple(5)
        self.assertEqual(self.list.max_val, 4)

        # delete the node with the new maximum value and check if the max_val is updated
        self.list.delete_nth_simple(4)
        self.assertEqual(self.list.max_val, 3)

    def test_delete_nth_simple_min_val(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete the node with the minimum value and check if the min_val is updated
        self.list.delete_nth_simple(1)
        self.assertEqual(self.list.min_val, 2)

        # delete the node with the new minimum value and check if the min_val is updated
        self.list.delete_nth_simple(1)
        self.assertEqual(self.list.min_val, 3)

    def test_delete_nth_simple_total_sum(self):
        self.list = LinkedList([1, 2, 3, 4, 5])
        # delete a node and check if the total_sum is reduced by its value
        self.list.delete_nth_simple(3)
        self.assertEqual(self.list.total_sum, 12)

        # delete another node and check if the total_sum is reduced by its value
        self.list.delete_nth_simple(2)
        self.assertEqual(self.list.total_sum, 10)

    # --------------------- delete_value ------------------------

    # def setUp(self):
    #     # create a sample linked list for testing
    #     self.ll = LinkedList([1, 2, 3, 4, 5])

    def test_delete_value_head(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # test if the function deletes the head node correctly
        self.list.delete_value(1)
        self.assertEqual(self.list.head.val, 2)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.total_sum, 14)

    def test_delete_value_tail(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # test if the function deletes the tail node correctly
        self.list.delete_value(5)
        self.assertEqual(self.list.tail.val, 4)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.total_sum, 10)

    def test_delete_value_not_found(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # test if the function does nothing when the value is not found
        self.list.delete_value(6)
        self.assertEqual(self.list.size, 5)
        self.assertEqual(self.list.total_sum, 15)

    def test_delete_value_invalid_input(self):
        # test if the function raises an exception for invalid inputs
        with self.assertRaises(TypeError):
            self.list.delete_value(None)
        with self.assertRaises(TypeError):
            self.list.delete_value("a")
        with self.assertRaises(ValueError):
            self.list.delete_value(-1)

    def test_delete_value_middle(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # test if the function deletes a middle node correctly
        self.list.delete_value(3)
        self.assertEqual(self.list.head.next.next.val, 4)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.total_sum, 12)

    def test_delete_value_all_occurrences(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # test if the function deletes all occurrences of a value in the list
        self.list.delete_value(2)
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.head.next.val, 3)
        self.assertEqual(self.list.head.next.next.val, 4)
        self.assertEqual(self.list.head.next.next.next.val, 5)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.total_sum, 13)

    def test_delete_value_multiple_nodes_in_a_row(self):
        self.list = LinkedList([1, 2, 3, 4, 5])

        # test if the function deletes multiple nodes in a row that have the same value
        self.list.delete_value(2)
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.head.next.val, 3)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.total_sum, 13)
        self.assertEqual(self.list.head.next.next.val, 4)


if __name__ == "__main__":
    # main()
    # This block runs the test suite when the script is executed
    suite = TestSuite()
    suite.addTest(makeSuite([TestLinkedList, TestLinkedListDataIntegrity]))
    TextTestRunner().run(suite)
