"""
Test cases for Beginner Project 01 - Number Guessing Game.
Run from inside this project's folder with:
    python -m unittest tests.test_game
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import check_guess  # noqa: E402


class TestCheckGuess(unittest.TestCase):
    def test_guess_too_low(self):
        self.assertEqual(check_guess(50, 10), "too_low")

    def test_guess_too_high(self):
        self.assertEqual(check_guess(50, 90), "too_high")

    def test_guess_correct(self):
        self.assertEqual(check_guess(50, 50), "correct")

    def test_boundary_values(self):
        self.assertEqual(check_guess(1, 1), "correct")
        self.assertEqual(check_guess(100, 99), "too_low")
        self.assertEqual(check_guess(100, 100), "correct")


if __name__ == "__main__":
    unittest.main()
