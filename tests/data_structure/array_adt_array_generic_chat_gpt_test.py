# import the unittest module
from unittest import TestCase, main

# import the array class from the previous code
from data_structures.array_adt_array_generic_chat_gpt import Array

# define a test class that inherits from unittest.TestCase


class TestArray(TestCase):

    # define a method that runs before each test case
    def setUp(self):
        # create an array of size 10 and typecode 'i'
        self.array = Array(10, 'i')

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


# run the test cases
if __name__ == '__main__':
    main()
