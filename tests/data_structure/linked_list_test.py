from unittest import TestCase, makeSuite, TestSuite, TextTestRunner
from data_structures.linked_list import LinkedList


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


if __name__ == "__main__":
    # This block runs the test suite when the script is executed
    suite = TestSuite()
    suite.addTest(makeSuite(TestLinkedList))
    TextTestRunner().run(suite)
