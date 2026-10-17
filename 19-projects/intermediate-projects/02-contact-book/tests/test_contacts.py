"""
Test cases for Intermediate Project 02 - Contact Book.
Run from inside this project's folder with:
    python -m unittest tests.test_contacts
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import ContactBook  # noqa: E402


class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.book = ContactBook()

    def test_add_and_search(self):
        self.book.add_contact("Alice", "555-1234", "alice@example.com")
        result = self.book.search_contact("Alice")
        self.assertEqual(result["phone"], "555-1234")

    def test_add_empty_name_raises(self):
        with self.assertRaises(ValueError):
            self.book.add_contact("   ", "555-0000", "x@example.com")

    def test_search_missing_returns_none(self):
        self.assertIsNone(self.book.search_contact("Nobody"))

    def test_delete_contact(self):
        self.book.add_contact("Bob", "555-0000", "bob@example.com")
        self.book.delete_contact("Bob")
        self.assertIsNone(self.book.search_contact("Bob"))

    def test_delete_missing_raises(self):
        with self.assertRaises(KeyError):
            self.book.delete_contact("Ghost")

    def test_round_trip_serialization(self):
        self.book.add_contact("Carla", "555-9999", "carla@example.com")
        lines = self.book.to_lines()
        reloaded = ContactBook()
        reloaded.load_from_lines(lines)
        self.assertEqual(reloaded.search_contact("Carla")["email"], "carla@example.com")


if __name__ == "__main__":
    unittest.main()
