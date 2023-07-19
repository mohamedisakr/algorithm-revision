from unittest import TestCase, main
from sorting.bubble_sort import sort


# A test case class that inherits from unittest.TestCase
class TestSort(TestCase):

    def test_sort(self):
        # An example input array
        arr = [5, 2, 4, 1, 3]
        # The expected output array
        expected = [1, 2, 3, 4, 5]
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)

    # A test method that checks if the sort function works with an empty array
    def test_sort_empty(self):
        # An empty input array
        arr = []
        # The expected output array
        expected = []
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)

    # A test method that checks if the sort function works with a single element array
    def test_sort_single(self):
        # A single element input array
        arr = [42]
        # The expected output array
        expected = [42]
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)

    # A test method that checks if the sort function works with a sorted array
    def test_sort_sorted(self):
        # A sorted input array
        arr = [1, 2, 3, 4, 5]
        # The expected output array
        expected = [1, 2, 3, 4, 5]
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)

    # A test method that checks if the sort function works with a reverse sorted array
    def test_sort_reverse(self):
        # A reverse sorted input array
        arr = [5, 4, 3, 2, 1]
        # The expected output array
        expected = [1, 2, 3, 4, 5]
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)

    # A test method that checks if the sort function works with an array that contains duplicates
    def test_sort_duplicates(self):
        # An input array that contains duplicates
        arr = [5, 2, 4, 2, 3]
        # The expected output array
        expected = [2, 2, 3, 4, 5]
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)

    # my first test case
    def test_my_first_test_case(self):
        # An input array that contains duplicates
        arr = [3, 2, 5, 9, 8, 1]
        # The expected output array
        expected = [1, 2, 3, 5, 8, 9]
        # Call the sort function and store the result
        result = sort(arr)
        # Use assertEqual to check if the result matches the expected output
        self.assertEqual(result, expected)


# Run the tests
if __name__ == '__main__':
    main()
