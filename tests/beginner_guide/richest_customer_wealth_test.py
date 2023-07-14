from unittest import TestCase, main
# assuming your function is in a file called solution.py
from beginner_guide.richest_customer_wealth import maximumWealth


class TestMaximumWealth(TestCase):

    def test_example_1(self):
        accounts = [[1, 2, 3], [3, 2, 1]]
        expected = 6
        actual = maximumWealth(accounts)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        accounts = [[1, 5], [7, 3], [3, 5]]
        expected = 10
        actual = maximumWealth(accounts)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        expected = 17
        actual = maximumWealth(accounts)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
