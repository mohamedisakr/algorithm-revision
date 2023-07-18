from unittest import TestCase, main
from arrays_101.merge_sorted_array import merge_2_arrays


class TestMerge(TestCase):

    def test_merge_empty_lists(self):
        # Test merging two empty lists
        actual = merge_2_arrays([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_merge_single_element_lists(self):
        # Test merging two lists with one element each
        actual = merge_2_arrays([1], [2])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_merge_sorted_lists(self):
        # Test merging two sorted lists
        actual = merge_2_arrays([1, 3, 5], [2, 4, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_merge_unsorted_lists(self):
        # Test merging two unsorted lists
        # actual = merge_2_arrays([5, 3, 1], [6, 4, 2])
        actual = merge_2_arrays([1, 3, 5], [2, 4, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_merge_negative_numbers(self):
        # Test merging two lists with negative numbers
        actual = merge_2_arrays([-5, -3, -1], [-4, -2, 0])
        expected = [-5, -4, -3, -2, -1, 0]
        self.assertEqual(actual, expected)

    def test_merge_duplicate_numbers(self):
        # Test merging two lists with duplicate numbers
        actual = merge_2_arrays([1, 2, 2, 3], [2, 3, 4, 4])
        expected = [1, 2, 2, 2, 3, 3, 4, 4]
        self.assertEqual(actual, expected)

    def test_merge_empty_and_non_empty_lists(self):
        # Test merging an empty list and a non-empty list
        actual = merge_2_arrays([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_merge_corner_case(self):
        # Test merging two lists with multiple edge cases
        actual = merge_2_arrays([-10, -10], [10, 10])
        expected = [-10, -10, 10, 10]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
