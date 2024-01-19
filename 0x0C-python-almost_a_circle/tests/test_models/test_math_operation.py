# tests/test_math_operations.py

import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 7), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)
        self.assertEqual(multiply(-3, 8), -24)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(8, 2), 4)

        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
