from unittest import TestCase, main
from data_structures.node import Node


class TestNode(TestCase):

    def setUp(self):
        # create some nodes for testing
        self.node1 = Node(1)
        self.node2 = Node(2, self.node1)
        self.node3 = Node(3, self.node2)

    def test_init(self):
        # test the initialization of nodes
        self.assertEqual(self.node1.val, 1)
        self.assertEqual(self.node1.next, None)
        self.assertEqual(self.node2.val, 2)
        self.assertEqual(self.node2.next, self.node1)
        self.assertEqual(self.node3.val, 3)
        self.assertEqual(self.node3.next, self.node2)

    def test_str(self):
        # test the string representation of nodes
        self.assertEqual(str(self.node1), "1")
        self.assertEqual(str(self.node2), "2")
        self.assertEqual(str(self.node3), "3")

    def test_show_node_list(self):
        # test the show_node_list method
        # use a StringIO object to capture the output
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        self.node3.show_node_list(self.node3)
        sys.stdout = sys.__stdout__
        # compare the output with the expected string
        self.assertEqual(output.getvalue(), "3 -> 2 -> 1 -> None")

    def test_find(self):
        # test the find method
        # use assertIs to check if the returned node is the same object as expected
        self.assertIs(self.node3.find(self.node3, 3), self.node3)
        self.assertIs(self.node3.find(self.node3, 2), self.node2)
        self.assertIs(self.node3.find(self.node3, 1), self.node1)
        # use assertIsNone to check if the value is not found
        self.assertIsNone(self.node3.find(self.node3, 4))


if __name__ == "__main__":
    main()
