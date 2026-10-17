"""
Test cases for Final Project 02 - Student Management System.
Run from inside this project's folder with:
    python -m unittest tests.test_student_system
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solution"))
from solution import Student, Classroom  # noqa: E402


class TestStudent(unittest.TestCase):
    def test_average_with_grades(self):
        student = Student("Alice")
        student.add_grade(80)
        student.add_grade(90)
        self.assertEqual(student.average(), 85)

    def test_average_with_no_grades_is_zero(self):
        student = Student("Bob")
        self.assertEqual(student.average(), 0)

    def test_letter_grade_boundaries(self):
        student = Student("Carla")
        student.add_grade(90)
        self.assertEqual(student.letter_grade(), "A")

    def test_line_round_trip(self):
        student = Student("Dan")
        student.add_grade(70)
        student.add_grade(85)
        line = student.to_line()
        rebuilt = Student.from_line(line)
        self.assertEqual(rebuilt.name, "Dan")
        self.assertEqual(rebuilt.grades, [70.0, 85.0])


class TestClassroom(unittest.TestCase):
    def setUp(self):
        self.classroom = Classroom()
        self.classroom.add_student("Alice")
        self.classroom.get_student("Alice").add_grade(95)
        self.classroom.add_student("Bob")
        self.classroom.get_student("Bob").add_grade(60)

    def test_get_student(self):
        self.assertIsNotNone(self.classroom.get_student("Alice"))
        self.assertIsNone(self.classroom.get_student("Nobody"))

    def test_top_student(self):
        top = self.classroom.top_student()
        self.assertEqual(top.name, "Alice")

    def test_duplicate_student_not_overwritten(self):
        original = self.classroom.get_student("Alice")
        self.classroom.add_student("Alice")
        self.assertIs(self.classroom.get_student("Alice"), original)


if __name__ == "__main__":
    unittest.main()
