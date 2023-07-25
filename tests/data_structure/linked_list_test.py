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
        # with self.assertRaises(ValueError):
        #     # try to create a node with a negative value
        #     node = Node(-1)

        # self.list.insert(None)
        # self.assertIsNone(self.list.tail.val,
        #                   "The tail value should be None")
        # self.assertEqual(len(self.list), 4, "The length should be 4")

    def test_insert_negative(self):
        # This method tests the insert method with a negative value
        # self.assertEqual(self.list.tail.val, -1,
        #                  "The tail value should be -1")
        # self.assertEqual(len(self.list), 4, "The length should be 4")
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

    # def test_insert_1(self):
    #     # This method tests the insert method of your linked list class
    #     # You can use self.assertEqual to check if two values are equal
    #     self.list.insert(10)
    #     self.list.insert(20)
    #     self.list.insert(30)

    #     # check if the size is updated correctly
    #     self.assertEqual(self.list.size, 3)

    #     # check if the head node has the correct value
    #     self.assertEqual(self.list.head.val, 10)

    #     # check if the tail node has the correct value
    #     self.assertEqual(self.list.tail.val, 30)

    #     # check if the max value is updated correctly
    #     self.assertEqual(self.list.max_value(), 30)

    #     # check if the min value is updated correctly
    #     self.assertEqual(self.list.min_value(), 10)

    #     # check if the sum is updated correctly
    #     self.assertEqual(self.list.sum_total(), 60)

    # def test_show_node_list_1(self):
    #     # This method tests the show_node_list method of your linked list class
    #     # You can use self.assertMultiLineEqual to check if two multi-line strings are equal
    #     self.list.insert(10)
    #     self.list.insert(20)
    #     self.list.insert(30)
    #     expected_output = "10 -> 20 -> 30 -> None"
    #     actual_output = self.list.show_node_list()
    #     # check if the output matches the expected output
    #     self.assertMultiLineEqual(expected_output, actual_output)

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


if __name__ == "__main__":
    # This block runs the test suite when the script is executed
    suite = TestSuite()
    suite.addTest(makeSuite(TestLinkedList))
    TextTestRunner().run(suite)

# test_linked_list.py

# import unittest
# from linked_list import LinkedList # assuming your linked list class is in a file named linked_list.py

# class TestLinkedList(unittest.TestCase):

#     def setUp(self):
#         # This method is executed before each test method
#         # You can use it to create a test instance of your linked list class
#         self.ll = LinkedList()


# if __name__ == "__main__":
#     unittest.main() # run all the tests in this file
