"""
Test cases for Intermediate Project 03 - Quiz Game.
Run from inside this project's folder with:
    python -m unittest tests.test_quiz
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import grade_answer  # noqa: E402

SAMPLE_QUESTION = {"question": "2 + 2 = ?", "options": ["3", "4", "5"], "answer": "4"}


class TestGradeAnswer(unittest.TestCase):
    def test_correct_choice(self):
        self.assertTrue(grade_answer(SAMPLE_QUESTION, 2))

    def test_incorrect_choice(self):
        self.assertFalse(grade_answer(SAMPLE_QUESTION, 1))

    def test_out_of_range_choice_is_incorrect(self):
        self.assertFalse(grade_answer(SAMPLE_QUESTION, 99))

    def test_zero_choice_is_incorrect(self):
        self.assertFalse(grade_answer(SAMPLE_QUESTION, 0))


if __name__ == "__main__":
    unittest.main()
