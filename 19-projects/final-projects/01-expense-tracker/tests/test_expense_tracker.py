"""
Test cases for Final Project 01 - Expense Tracker.
Run from inside this project's folder with:
    python -m unittest tests.test_expense_tracker
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import Expense, ExpenseTracker  # noqa: E402


class TestExpense(unittest.TestCase):
    def test_str_formatting(self):
        expense = Expense(12.5, "Food", "Lunch")
        self.assertIn("Food", str(expense))
        self.assertIn("Lunch", str(expense))

    def test_line_round_trip(self):
        expense = Expense(9.99, "Transport", "Bus ticket")
        line = expense.to_line()
        rebuilt = Expense.from_line(line)
        self.assertEqual(rebuilt.amount, 9.99)
        self.assertEqual(rebuilt.category, "Transport")
        self.assertEqual(rebuilt.description, "Bus ticket")


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()
        self.tracker.add_expense(20, "Food", "Groceries")
        self.tracker.add_expense(15, "Food", "Coffee")
        self.tracker.add_expense(50, "Transport", "Train pass")

    def test_total_spent(self):
        self.assertEqual(self.tracker.total_spent(), 85)

    def test_total_by_category(self):
        totals = self.tracker.total_by_category()
        self.assertEqual(totals["Food"], 35)
        self.assertEqual(totals["Transport"], 50)

    def test_delete_expense(self):
        self.tracker.delete_expense(0)
        self.assertEqual(len(self.tracker.expenses), 2)
        self.assertEqual(self.tracker.total_spent(), 65)

    def test_empty_tracker_total_is_zero(self):
        empty_tracker = ExpenseTracker()
        self.assertEqual(empty_tracker.total_spent(), 0)


if __name__ == "__main__":
    unittest.main()
