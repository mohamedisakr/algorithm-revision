# Import the unittest module
from unittest import TestCase, main

# Import the function you want to test
from beginner_guide.reduce_number_zero import numberOfSteps

# Define a class that inherits from unittest.TestCase


class TestNumberOfSteps(TestCase):

    # Define a method that starts with test_
    def test_number_of_steps(self):

        # Use self.assertEqual to check if the function returns the expected output
        self.assertEqual(numberOfSteps(14), 6)
        self.assertEqual(numberOfSteps(8), 4)
        self.assertEqual(numberOfSteps(123), 12)

        # Use self.assertRaises to check if the function raises an exception for invalid input
        # self.assertRaises(TypeError, numberOfSteps, "hello")
        # self.assertRaises(ValueError, numberOfSteps, -1)


# Run the tests
if __name__ == "__main__":
    main()
