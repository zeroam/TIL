import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, 'Should be 6')

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, 'Should be 6')

    def test_bad_type(self):
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
