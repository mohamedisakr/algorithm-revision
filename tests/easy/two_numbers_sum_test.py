from unittest import TestCase, main
from easy.two_numbers_sum import find_two_numbers_sum_sort_first


class TestFindTwoNumbersSumSortFirst(TestCase):

    def test_normal_case(self):
        # Test a normal case where the pair exists
        array = [3, 5, 2, -4, 8, 11]
        target_sum = 7
        expected = [-4, 11]
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_no_pair_case(self):
        # Test a case where the pair does not exist
        array = [1, 2, 3]
        target_sum = 6
        expected = []
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_invalid_input_case(self):
        # Test a case where the input is invalid
        array = "hello"
        target_sum = 10
        with self.assertRaises(TypeError):
            find_two_numbers_sum_sort_first(array, target_sum)

    def test_empty_array_case(self):
        # Test a case where the array is empty
        array = []
        target_sum = 10
        expected = []
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_single_element_array_case(self):
        # Test a case where the array has only one element
        array = [5]
        target_sum = 10
        expected = []
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_multiple_pairs_case(self):
        # Test a case where there are multiple pairs that satisfy the condition
        array = [1, 2, 3, 4, 5, 6]
        target_sum = 7
        expected = [1, 6]
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_negative_target_sum_case(self):
        # Test a case where the target sum is negative
        array = [-1, -2, -3, -4, -5, -6]
        target_sum = -7
        expected = [-6, -1]
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_same_element_pair_case(self):
        # Test a case where the pair consists of the same element
        array = [1, 2, 3, 4, 4]
        target_sum = 8
        expected = [4, 4]
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)

    def test_zero_target_sum_case(self):
        # Test a case where the target sum is zero
        array = [-1, 0, 1, 2, 3]
        target_sum = 0
        expected = [-1, 1]
        actual = find_two_numbers_sum_sort_first(array, target_sum)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
