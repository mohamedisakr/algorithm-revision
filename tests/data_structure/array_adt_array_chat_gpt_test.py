from unittest import TestCase, main
from data_structures.array_adt_array_chat_gpt import Array

# define a test class that inherits from TestCase


class TestArray(TestCase):

    # define a method that runs before each test case
    def setUp(self):
        # create an array of size 10
        self.array = Array(10)

    # define a method that runs after each test case
    def tearDown(self):
        # delete the array
        del self.array

    # define a test case for the append method
    def test_append(self):
        # append 5 elements to the array
        for i in range(5):
            self.array.append(i)
        # check that the length of the array is 5
        self.assertEqual(len(self.array), 5)
        # check that the elements of the array are correct
        for i in range(5):
            self.assertEqual(self.array[i], i)
        # check that appending to a full array raises an exception
        for i in range(5):
            self.array.append(i)
        with self.assertRaises(OverflowError):
            self.array.append(10)

    # define a test case for the insert method
    def test_insert(self):
        # insert 5 elements to the array at different positions
        self.array.insert(0, 0)
        self.array.insert(1, 1)
        self.array.insert(1, 2)
        self.array.insert(3, 3)
        self.array.insert(2, 4)
        # check that the length of the array is 5
        self.assertEqual(len(self.array), 5)
        # check that the elements of the array are correct
        self.assertEqual(self.array[0], 0)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 4)
        self.assertEqual(self.array[3], 1)
        self.assertEqual(self.array[4], 3)
        # check that inserting to a full array raises an exception
        for i in range(5):
            self.array.insert(i, i)
        with self.assertRaises(OverflowError):
            self.array.insert(10, 10)
        # check that inserting at an invalid index raises an exception
        with self.assertRaises(IndexError):
            self.array.insert(-1, -1)
        with self.assertRaises(IndexError):
            self.array.insert(11, 11)

    # define a test case for the remove method
    def test_remove(self):
        # append 5 elements to the array
        for i in range(5):
            self.array.append(i)
        # remove 3 elements from the array at different positions
        value = self.array.remove(0)
        self.assertEqual(value, 0)
        value = self.array.remove(2)
        self.assertEqual(value, 3)
        value = self.array.remove(2)
        self.assertEqual(value, 4)
        # check that the length of the array is 2
        self.assertEqual(len(self.array), 2)
        # check that the elements of the array are correct
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        # check that removing from an empty array raises an exception
        value = self.array.remove(0)
        value = self.array.remove(0)
        with self.assertRaises(IndexError):
            value = self.array.remove(0)

    # define a test case for the __len__ method
    def test_len(self):
        # check that the length of an empty array is 0
        self.assertEqual(len(self.array), 0)
        # check that the length of an array with one element is 1
        self.array.append(0)
        self.assertEqual(len(self.array), 1)
        # check that the length of a full array is equal to its size
        for i in range(1, 10):
            self.array.append(i)
        self.assertEqual(len(self.array), 10)

    # define a test case for the __getitem__ method
    def test_getitem(self):
        # append 5 elements to the array
        for i in range(5):
            self.array.append(i)
        # check that getting an element at a valid index returns the correct value
        for i in range(5):
            self.assertEqual(self.array[i], i)
        # check that getting an element at an invalid index raises an exception
        with self.assertRaises(IndexError):
            value = self.array[-1]
        with self.assertRaises(IndexError):
            value = self.array[5]

    # define a test case for the __setitem__ method
    def test_setitem(self):
        # append 5 elements to the array
        for i in range(5):
            self.array.append(i)
        # check that setting an element at a valid index changes the value
        for i in range(5):
            self.array[i] = i + 10
            self.assertEqual(self.array[i], i + 10)
        # check that setting an element at an invalid index raises an exception
        with self.assertRaises(IndexError):
            self.array[-1] = -1
        with self.assertRaises(IndexError):
            self.array[5] = 15

    # define a test case for the append method with invalid values
    def test_append_invalid(self):
        # check that appending a non-integer value raises an exception
        with self.assertRaises(TypeError):
            self.array.append("a")
        with self.assertRaises(TypeError):
            self.array.append(1.5)
        # with self.assertRaises(TypeError):
        #     self.array.append(True)

    # define a test case for the insert method with invalid values
    def test_insert_invalid(self):
        # check that inserting a non-integer value raises an exception
        with self.assertRaises(TypeError):
            self.array.insert(0, "a")
        with self.assertRaises(TypeError):
            self.array.insert(0, 1.5)
        # with self.assertRaises(TypeError):
        #     self.array.insert(0, True)

    # define a test case for the remove method with an empty array
    def test_remove_empty(self):
        # check that removing from an empty array raises an exception
        with self.assertRaises(IndexError):
            value = self.array.remove(0)

    '''
    # define a test case that expects a TypeError
    def test_type_error(self):
        # check that raising a TypeError passes the test
        with self.assertRaises(TypeError):
            raise TypeError("This is a type error")
        # check that raising a different exception fails the test
        with self.assertRaises(TypeError):
            raise ValueError("This is a value error")
    '''


if __name__ == '__main__':
    main()
