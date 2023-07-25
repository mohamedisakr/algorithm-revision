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
        self.list.insert(None)
        self.assertIsNone(self.list.tail.val,
                          "The tail value should be None")
        self.assertEqual(len(self.list), 4, "The length should be 4")

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


if __name__ == "__main__":
    # This block runs the test suite when the script is executed
    suite = TestSuite()
    suite.addTest(makeSuite(TestLinkedList))
    TextTestRunner().run(suite)
