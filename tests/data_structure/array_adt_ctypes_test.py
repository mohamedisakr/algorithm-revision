from unittest import TestCase, main
from data_structures.array_adt_ctypes import Array


class TestArray(TestCase):

    # Define a setUp method that runs before each test case
    def setUp(self):
        # Create an empty array object
        self.array = Array()

    # Define a test case for the __len__ method
    def test_len(self):
        # Check that the length of the array is initially zero
        self.assertEqual(len(self.array), 0)
        # Append some items to the array and check the length again
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.assertEqual(len(self.array), 3)

    # Define a test case for the __getitem__ and __setitem__ methods
    def test_get_set_item(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        # Check that the items can be accessed by index
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)
        # Check that the items can be modified by index
        self.array[0] = 4
        self.array[1] = 5
        self.array[2] = 6
        self.assertEqual(self.array[0], 4)
        self.assertEqual(self.array[1], 5)
        self.assertEqual(self.array[2], 6)

    # Define a test case for the append method
    def test_append(self):
        # Check that the array is initially empty
        self.assertEqual(len(self.array), 0)
        # Append some items to the array and check that they are added correctly
        self.array.append(1)
        self.assertEqual(len(self.array), 1)
        self.assertEqual(self.array[0], 1)
        self.array.append(2)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[1], 2)
        self.array.append(3)
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[2], 3)

    # Define a test case for the insert method
    def test_insert(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        # Check that the array has the expected items
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)
        # Insert some items at different positions and check that they are inserted correctly
        self.array.insert(0, 4)  # Insert at the beginning
        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[0], 4)
        self.assertEqual(self.array[1], 1)
        self.assertEqual(self.array[2], 2)
        self.assertEqual(self.array[3], 3)

    def test_right_rotate(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        # Check that the array has the expected items
        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)
        self.assertEqual(self.array[3], 4)

        self.array.right_rotate()

        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[0], 4)
        self.assertEqual(self.array[1], 1)
        self.assertEqual(self.array[2], 2)
        self.assertEqual(self.array[3], 3)

    def test_left_rotate(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)

        # Check that the array has the expected items
        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)
        self.assertEqual(self.array[3], 4)

        # print(self.array)
        self.array.left_rotate()
        # print(self.array)

        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[0], 2)
        self.assertEqual(self.array[1], 3)
        self.assertEqual(self.array[2], 4)
        self.assertEqual(self.array[3], 1)

    def test_right_rotate_steps(self):
        # Append some items to the array
        self.array.append(0)
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)

        # Check that the array has the expected items
        self.assertEqual(len(self.array), 5)
        self.assertEqual(self.array[0], 0)
        self.assertEqual(self.array[1], 1)
        self.assertEqual(self.array[2], 2)
        self.assertEqual(self.array[3], 3)
        self.assertEqual(self.array[4], 4)

        # print(self.array)
        times = 3
        self.array.right_rotate_steps(times)
        # print(self.array)

        self.assertEqual(len(self.array), 5)
        self.assertEqual(self.array[0], 2)
        self.assertEqual(self.array[1], 3)
        self.assertEqual(self.array[2], 4)
        self.assertEqual(self.array[3], 0)
        self.assertEqual(self.array[4], 1)
    '''
    # Define a test case for the pop method
    def test_pop(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        # Check that the array has the expected items
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)

        # Pop some items from different positions and check that
        # they are removed correctly
        # Pop from the beginning
        item = self.array.pop(0)
        self.assertEqual(item, 1)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[0], 2)
        self.assertEqual(self.array[1], 3)

        # Pop from the end
        item = self.array.pop(-1)
        self.assertEqual(item, 3)
        self.assertEqual(len(self.array), 1)
        self.assertEqual(self.array[0], 2)

        # Pop the last item
        item = self.array.pop(0)
        self.assertEqual(item, 2)
        self.assertEqual(len(self.array), 0)
    '''

    def test_pop_from_beginning(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        # Check that the array has the expected items
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)

        # Pop from the beginning
        item = self.array.pop(0)
        self.assertEqual(item, 1)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[0], 2)
        self.assertEqual(self.array[1], 3)

    def test_pop_from_end(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        # Check that the array has the expected items
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)

        # Pop from the end
        item = self.array.pop(-1)
        self.assertEqual(item, 3)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[0], 1)

    def test_pop_last_item(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        # Check that the array has the expected items
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)

        # Pop the last item
        item = self.array.pop(0)
        self.assertEqual(item, 1)
        self.assertEqual(len(self.array), 2)

    # Define a test case for the expand_capacity method

    def test_expand_capacity(self):
        # Check that the array has an initial capacity of 16
        self.assertEqual(self.array._capacity, 16)
        # Append some items to the array until it reaches its capacity
        for i in range(16):
            self.array.append(i)
            self.assertEqual(len(self.array), i+1)
            self.assertEqual(self.array[i], i)
        # Check that the array has not expanded yet
        self.assertEqual(self.array._capacity, 16)
        # Append one more item to the array and check that it triggers an expansion
        self.array.append(16)
        self.assertEqual(len(self.array), 17)
        self.assertEqual(self.array[16], 16)
        # Check that the array has doubled its capacity
        self.assertEqual(self.array._capacity, 32)

    # Define a test case for invalid index errors
    def test_invalid_index_error(self):
        # Check that accessing or modifying an empty array raises an IndexError
        with self.assertRaises(IndexError):
            item = self.array[0]
        with self.assertRaises(IndexError):
            self.array[0] = 1
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        # Check that accessing or modifying an out-of-bounds index raises an IndexError
        with self.assertRaises(IndexError):
            item = self.array[3]
        with self.assertRaises(IndexError):
            item = self.array[-4]
        with self.assertRaises(IndexError):
            self.array[3] = 4
        with self.assertRaises(IndexError):
            self.array[-4] = 4

    # Define a test case for invalid insert errors
    def test_invalid_insert_error(self):
        # Check that inserting into an empty array with a non-zero index raises an AssertionError
        with self.assertRaises(AssertionError):
            self.array.insert(1, 1)
        with self.assertRaises(AssertionError):
            self.array.insert(-1, 1)

        # Define a test case for the __getitem__ and __setitem__ methods with negative index

    def test_get_set_item_negative(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        # Check that the items can be accessed by negative index
        self.assertEqual(self.array[-1], 3)
        self.assertEqual(self.array[-2], 2)
        self.assertEqual(self.array[-3], 1)
        # Check that the items can be modified by negative index
        self.array[-1] = 6
        self.array[-2] = 5
        self.array[-3] = 4
        self.assertEqual(self.array[-1], 6)
        self.assertEqual(self.array[-2], 5)
        self.assertEqual(self.array[-3], 4)

    # Define a test case for the insert method with negative index
    def test_insert_negative(self):
        # Append some items to the array
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        # Check that the array has the expected items
        self.assertEqual(len(self.array), 3)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 3)
        # Insert some items at different negative positions and check that they are inserted correctly
        self.array.insert(-1, 4)  # Insert before the last item
        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[2], 4)
        self.assertEqual(self.array[3], 3)
        self.array.insert(-3, 5)  # Insert in the middle
        self.assertEqual(len(self.array), 5)
        self.assertEqual(self.array[0], 1)


# run the test cases
if __name__ == '__main__':
    main()
