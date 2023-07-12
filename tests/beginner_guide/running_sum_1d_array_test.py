from unittest import TestCase, main
from beginner_guide.running_sum_1d_array import runningSum


class TestRunningSum(TestCase):

    def test_empty_list(self):
        self.assertEqual(runningSum([]), [])

    def test_single_element(self):
        self.assertEqual(runningSum([5]), [5])

    def test_positive_numbers(self):
        self.assertEqual(runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_negative_numbers(self):
        self.assertEqual(runningSum([-1, -2, -3, -4]), [-1, -3, -6, -10])

    def test_mixed_numbers(self):
        self.assertEqual(runningSum([1, -2, 3, -4]), [1, -1, 2, -2])


if __name__ == '__main__':
    main()
