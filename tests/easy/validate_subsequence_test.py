from unittest import TestCase, main
from easy.validate_subsequence import is_valid_subsequence


class TestIsValidSubsequence(TestCase):

    def test_valid_subsequence(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_invalid_subsequence(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 26, 22]
        self.assertFalse(is_valid_subsequence(array, sequence))

    def test_empty_sequence(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = []
        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_empty_array(self):
        array = []
        sequence = [1, 6]
        self.assertFalse(is_valid_subsequence(array, sequence))

    def test_type_error(self):
        array = [5, "a", 22]
        sequence = [5]
        with self.assertRaises(TypeError):
            is_valid_subsequence(array, sequence)

    def test_single_element_sequence(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [6]
        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_single_element_array(self):
        array = [5]
        sequence = [5]
        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_same_array_and_sequence(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10]
        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_negative_numbers(self):
        array = [-5, -1, -22, -25, -6, -1, -8, -10]
        sequence = [-1, -6, -1]
        self.assertTrue(is_valid_subsequence(array, sequence))

    def test_duplicate_numbers(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 5]
        self.assertFalse(is_valid_subsequence(array, sequence))


if __name__ == "__main__":
    main()
