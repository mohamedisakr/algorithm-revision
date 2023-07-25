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

    def test_init_invalid_1(self):
        # test the initialization of nodes with invalid values
        # use assertRaises to check if an exception is raised
        with self.assertRaises(TypeError):
            # try to create a node with a non-numeric value
            node = Node("a")
        with self.assertRaises(ValueError):
            # try to create a node with a negative value
            node = Node(-1)

    def test_show_node_list_empty(self):
        # test the show_node_list method with an empty node list
        # use a StringIO object to capture the output
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        # create an empty node
        node = Node(None)
        node.show_node_list(node)
        sys.stdout = sys.__stdout__
        # compare the output with the expected string
        self.assertEqual(output.getvalue(), "")

    def test_find_empty(self):
        # test the find method with an empty node list
        # create an empty node
        node = Node(None)
        # use assertIsNone to check if the value is not found
        self.assertIsNone(node.find(node, 1))

    def test_find_invalid(self):
        # test the find method with an invalid value
        # use assertIsNone to check if the value is not found
        self.assertIsNone(self.node3.find(self.node3, "a"))


if __name__ == "__main__":
    main()
