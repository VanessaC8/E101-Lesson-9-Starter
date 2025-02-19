import unittest

class TestIsOdd(unittest.TestCase):

    def test_odd_num(self):
        self.assertTrue(is_odd(3))

if __name__ == '__main__':
    unittest.main()
