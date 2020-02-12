import unittest

class TestInvalidInput(unittest.TestCase):

    # using a with block is the best way to assert errors
    def test_string_function_failure(self):
        with self.assertRaises(AttributeError):
            x = None.lower()

    # you can specify regex to handle the specific error message
    def test_string_function_failure_with_regex(self):
        with self.assertRaisesRegex(
                AttributeError,
                "'NoneType' object has no attribute 'lower'"):
            x = None.lower()
