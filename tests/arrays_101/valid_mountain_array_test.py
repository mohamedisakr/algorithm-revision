from unittest import TestCase, main
from arrays_101.valid_mountain_array import validMountainArray


class TestValidMountainArray(TestCase):

    # Define one or more methods that start with test_ and call your validMountainArray function with different inputs and expected outputs
    def test_valid_mountain_array(self):
        # Use self.assertEqual to check if the function returns True for
        # a valid mountain array
        # self.assertEqual(validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]), True)
        self.assertTrue(validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))

    def test_not_valid_mountain_array(self):
        # Use self.assertFalse to check if the function returns False for
        # an array that is not a valid mountain array
        self.assertFalse(validMountainArray([0, 2, 3, 3, 5, 2, 1, 0]))
        self.assertFalse(validMountainArray([0, 2, 3, 4, 5]))
        self.assertFalse(validMountainArray([5, 4, 3, 2, 1]))

    def test_invalid_input(self):
        # Use self.assertRaises to check if the function raises a ValueError
        # for an array that has more than 10 elements
        with self.assertRaises(ValueError):
            validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Add a main block at the end of your file to run your tests
if __name__ == '__main__':
    main()
