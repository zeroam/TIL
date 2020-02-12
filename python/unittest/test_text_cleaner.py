import unittest

class TextCleaner:

    def lower_and_trim(self, text: str) -> str:
        result = text.lower().strip()
        return result


class TestTextCleaner(unittest.TestCase):

    def test_lower_and_trim(self):
        text_cleaner = TextCleaner()
        x = '     SOME TEXT     '
        x = text_cleaner.lower_and_trim(x)
        self.assertEqual(x, 'some text')


if __name__ == '__main__':
    unittest.main()