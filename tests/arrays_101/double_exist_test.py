from unittest import TestCase, main
from arrays_101.double_exist import checkIfExist


class TestCheckIfExist(TestCase):
    def test_empty_array(self):
        # Test that an empty array returns False
        arr = []
        result = checkIfExist(arr)
        self.assertFalse(result)

    def test_positive_array(self):
        # Test that an array with positive integers returns True if there exist two indices i and j such that arr[i] == 2 * arr[j]
        arr = [10, 2, 5, 3]
        result = checkIfExist(arr)
        self.assertTrue(result)

    def test_negative_array(self):
        # Test that an array with negative integers returns True if there exist two indices i and j such that arr[i] == 2 * arr[j]
        arr = [-10, -20, -5, -2]
        result = checkIfExist(arr)
        self.assertTrue(result)

    def test_mixed_array(self):
        # Test that an array with mixed integers returns False if there is no such pair of indices
        arr = [1, 4, 6, 7]
        result = checkIfExist(arr)
        self.assertFalse(result)

    def test_invalid_input(self):
        # Test that an invalid input raises a TypeError
        arr = "hello"
        with self.assertRaises(TypeError):
            checkIfExist(arr)

    def test_empty_array(self):
        # Test that an empty array returns False
        arr = []
        result = checkIfExist(arr)
        self.assertFalse(result)

    def test_positive_array(self):
        # Test that an array with positive integers returns True if there exist two indices i and j such that arr[i] == 2 * arr[j]
        arr = [10, 2, 5, 3]
        result = checkIfExist(arr)
        self.assertTrue(result)

    def test_negative_array(self):
        # Test that an array with negative integers returns True if there exist two indices i and j such that arr[i] == 2 * arr[j]
        arr = [-10, -20, -5, -2]
        result = checkIfExist(arr)
        self.assertTrue(result)

    def test_mixed_array(self):
        # Test that an array with mixed integers returns False if there is no such pair of indices
        arr = [1, 4, 6, 7]
        result = checkIfExist(arr)
        self.assertFalse(result)

    def test_invalid_input(self):
        # Test that an invalid input raises a TypeError
        arr = "hello"
        with self.assertRaises(TypeError):
            checkIfExist(arr)

    def test_zero_array(self):
        # Test that an array with only zeros returns True
        arr = [0, 0, 0, 0]
        result = checkIfExist(arr)
        self.assertTrue(result)

    def test_one_element_array(self):
        # Test that an array with only one element returns False
        arr = [42]
        result = checkIfExist(arr)
        self.assertFalse(result)

    def test_float_array(self):
        # Test that an array with float numbers returns True if there exist two indices i and j such that arr[i] == 2 * arr[j]
        arr = [1.5, 3.0, 4.5, 6.0]
        result = checkIfExist(arr)
        self.assertTrue(result)

    # def test_large_array(self):
    #     # Test that an array with large numbers returns False if there is no such pair of indices
    #     arr = [1000000000, 2000000000, 3000000000, 4000000000]
    #     result = checkIfExist(arr)
    #     self.assertFalse(result)


if __name__ == '__main__':
    main()
