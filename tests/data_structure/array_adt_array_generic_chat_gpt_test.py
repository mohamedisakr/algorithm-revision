# import the unittest module
from unittest import TestCase, main

# import the array class from the previous code
from data_structures.array_adt_array_generic_chat_gpt import Array


class TestArray(TestCase):
    def setUp(self):
        # create an array of size 10 for testing
        self.array = Array(10)

    def test_len(self):
        # test the __len__ method
        # the array should be empty initially
        self.assertEqual(len(self.array), 0)
        self.array.append(1)  # add one element
        # the array should have one element now
        self.assertEqual(len(self.array), 1)

    def test_getitem(self):
        # test the __getitem__ method
        self.array.append(1)  # add one element
        self.assertEqual(self.array[0], 1)  # the first element should be 1
        self.assertEqual(self.array[-1], 1)  # the last element should be 1
        # expect an exception for invalid index
        with self.assertRaises(IndexError):
            self.array[1]  # try to access the second element
        # expect an exception for invalid index
        with self.assertRaises(IndexError):
            self.array[-2]  # try to access the second last element

    def test_setitem(self):
        # test the __setitem__ method
        self.array.append(1)  # add one element
        self.array[0] = 2  # change the first element to 2
        self.assertEqual(self.array[0], 2)  # the first element should be 2
        self.array[-1] = 3  # change the last element to 3
        self.assertEqual(self.array[-1], 3)  # the last element should be 3
        # expect an exception for invalid index
        with self.assertRaises(IndexError):
            self.array[1] = 4  # try to set the second element to 4
        # expect an exception for invalid index
        with self.assertRaises(IndexError):
            self.array[-2] = 5  # try to set the second last element to 5

    def test_append(self):
        # test the append method
        for i in range(10):
            self.array.append(i)  # add 10 elements from 0 to 9
            # check the length of the array
            self.assertEqual(len(self.array), i+1)
            # check the value of each element
            self.assertEqual(self.array[i], i)
            # check the value of each element using negative index
            self.assertEqual(self.array[-i-1], i)

        with self.assertRaises(OverflowError):  # expect an exception for overflow
            self.array.append(10)  # try to add one more element

    def test_insert(self):
        # test the insert method
        for i in range(10):
            # insert 10 elements from 0 to 9 at their respective positions
            self.array.insert(i, i)
            # check the length of the array
            self.assertEqual(len(self.array), i+1)
            # check the value of each element
            self.assertEqual(self.array[i], i)
            # check the value of each element using negative index
            self.assertEqual(self.array[-i-1], i)
        with self.assertRaises(OverflowError):  # expect an exception for overflow
            # try to insert one more element at the end
            self.array.insert(10, 10)
        with self.assertRaises(OverflowError):  # expect an exception for overflow
            # try to insert one more element at the beginning
            self.array.insert(-11, -11)

    def test_remove(self):
        # test the remove method
        for i in range(10):
            self.array.append(i)  # add 10 elements from 0 to 9
        for i in range(9, -1, -1):
            value = self.array.remove(i)  # remove each element from the end
            # check the value of the removed element
            self.assertEqual(value, i)
            # check the length of the array
            self.assertEqual(len(self.array), i)
        # expect an exception for empty array
        with self.assertRaises(IndexError):
            self.array.remove(0)  # try to remove from an empty array


# run the test cases
if __name__ == '__main__':
    main()

'''
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
'''
