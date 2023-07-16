from unittest import TestCase, main
from arrays_101.even_numbers_of_digits import findNumbers


class TestFindNumbers(TestCase):

    def test_findNumbers(self):
        self.assertEqual(findNumbers([12, 345, 2, 6, 7896]), 2)
        self.assertEqual(findNumbers([555, 901, 482, 1771]), 1)
        self.assertEqual(findNumbers([0]), 0)
        self.assertEqual(findNumbers([]), 0)
        self.assertEqual(findNumbers([100000]), 1)

    def test_empty_list(self):
        self.assertEqual(findNumbers([]), 0)

    def test_example_list(self):
        self.assertEqual(findNumbers([12, 345, 2, 6, 7896]), 2)

    def test_all_even_digits(self):
        self.assertEqual(findNumbers([22, 44, 66]), 3)

    def test_all_odd_digits(self):
        self.assertEqual(findNumbers([111, 333, 555]), 0)

    def test_one_digit_numbers(self):
        self.assertEqual(findNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)

    def test_large_numbers(self):
        self.assertEqual(findNumbers([10**9, 10**10, 10**11]), 2)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            findNumbers([12, "345", 2.6, True])

    def test_zero(self):
        self.assertEqual(findNumbers([0]), 0)

    # def test_negative_numbers(self):
    #     self.assertEqual(findNumbers([-12, -345, -2, -6, -7896]), 2)


# Run the tests
if __name__ == "__main__":
    main()
