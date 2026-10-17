"""
Test cases for Beginner Project 02 - Simple Calculator.
Run from inside this project's folder with:
    python -m unittest tests.test_calculator
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import calculate  # noqa: E402


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 4, "-"), 6)

    def test_multiplication(self):
        self.assertEqual(calculate(6, 7, "*"), 42)

    def test_division(self):
        self.assertEqual(calculate(9, 2, "/"), 4.5)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, 0, "/")

    def test_unknown_operator_raises(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "^")


if __name__ == "__main__":
    unittest.main()
