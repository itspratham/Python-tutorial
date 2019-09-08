import unittest
import math


class MyMathTestCase1(unittest.TestCase):

    def test_both_number(self):
        self.assertEqual(math.multiply(2,5), 10)

    def test_minus_both_number(self):
        self.assertEqual(math.multiply(-2, 5), -10)

class MyMathTestCase2(unittest.TestCase):
    def test_one_str_one_number(self):
        self.assertEqual(math.multiply('a', 5), 'aaaaa')

    def test_both_minus_both_number(self):
        self.assertEqual(math.multiply(-2, -5), 10)

    def test_both_str(self):
        self.assertEqual(math.multiply("12", "5"), None)

if __name__ == "__main__":
    unittest.main()



