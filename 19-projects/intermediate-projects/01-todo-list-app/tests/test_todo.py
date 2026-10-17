"""
Test cases for Intermediate Project 01 - To-Do List App.
Run from inside this project's folder with:
    python -m unittest tests.test_todo
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import TaskManager  # noqa: E402


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Buy milk")
        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertEqual(self.manager.list_tasks()[0]["text"], "Buy milk")
        self.assertFalse(self.manager.list_tasks()[0]["done"])

    def test_add_empty_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        self.manager.add_task("Walk the dog")
        self.manager.complete_task(0)
        self.assertTrue(self.manager.list_tasks()[0]["done"])

    def test_complete_invalid_index_raises(self):
        with self.assertRaises(IndexError):
            self.manager.complete_task(0)

    def test_remove_task(self):
        self.manager.add_task("Read a book")
        removed = self.manager.remove_task(0)
        self.assertEqual(removed["text"], "Read a book")
        self.assertEqual(len(self.manager.list_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
