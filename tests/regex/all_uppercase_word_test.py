from unittest import TestCase, main
from regex.all_uppercase_word import match_all_uppercase_word


class TestMatchAllUppercaseWord(TestCase):

    def test_empty_string(self):
        # Test that an empty string returns an empty list
        self.assertEqual(match_all_uppercase_word(""), [])

    def test_no_uppercase_words(self):
        # Test that a string with no uppercase words returns an empty list
        self.assertEqual(match_all_uppercase_word("hello world"), [])

    def test_one_uppercase_word(self):
        # Test that a string with one uppercase word returns a list with one element
        self.assertEqual(match_all_uppercase_word(
            "This is an EXAMPLE"), ["EXAMPLE"])

    def test_multiple_uppercase_words(self):
        # Test that a string with multiple uppercase words returns a list with all of them
        self.assertEqual(match_all_uppercase_word(
            "FOO BAR BAZ"), ["FOO", "BAR", "BAZ"])

    def test_mixed_case_words(self):
        # Test that a string with mixed case words only returns the uppercase ones
        self.assertEqual(match_all_uppercase_word(
            # "Foo BAR baz QuX"), ["BAR", "QuX"])
            "Foo BAR baz QuX"), ["BAR"])


if __name__ == '__main__':
    main()
