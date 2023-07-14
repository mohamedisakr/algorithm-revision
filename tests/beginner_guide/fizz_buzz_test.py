from unittest import TestCase, main
from beginner_guide.fizz_buzz import fizzBuzz


class TestFizzBuzz(TestCase):

    def test_fizzBuzz_1(self):
        # Test case for n = 1
        self.assertEqual(fizzBuzz(1), ["1"])

    def test_fizzBuzz_3(self):
        # Test case for n = 3
        self.assertEqual(fizzBuzz(3), ["1", "2", "Fizz"])

    def test_fizzBuzz_5(self):
        # Test case for n = 5
        self.assertEqual(fizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_fizzBuzz_15(self):
        # Test case for n = 15
        self.assertEqual(fizzBuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz",
                         "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

    def test_fizzBuzz_negative(self):
        # Test case for n = -1
        self.assertEqual(fizzBuzz(-1), [])

    def test_fizzBuzz_zero(self):
        # Test case for n = 0
        self.assertEqual(fizzBuzz(0), [])

    def test_fizzBuzz_non_integer(self):
        # Test case for n = 3.5
        with self.assertRaises(TypeError):
            fizzBuzz(3.5)

    def test_fizzBuzz_large_number(self):
        # Test case for n = 1000000
        self.assertEqual(fizzBuzz(1000000)[1], "2")


if __name__ == "__main__":
    main()
