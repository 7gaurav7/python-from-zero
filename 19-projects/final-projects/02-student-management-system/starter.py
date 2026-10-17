"""
Final Project 02 - Student Management System (starter)
Build this up milestone by milestone -- see README.md.
"""

FILENAME = "students.txt"


class Student:
    def __init__(self, name):
        # TODO: store name, and an empty list for grades
        pass

    def add_grade(self, grade):
        # TODO: append a grade to self.grades
        pass

    def average(self):
        # TODO: return the average grade, or 0 if there are no grades
        pass

    def letter_grade(self):
        # TODO: use self.average() to return "A"/"B"/"C"/"D"/"F"
        pass


class Classroom:
    def __init__(self):
        self.students = {}  # name -> Student

    def add_student(self, name):
        # TODO: create a Student and add it to self.students
        pass

    def get_student(self, name):
        # TODO: return the Student object, or None if not found
        pass

    def class_summary(self):
        # TODO: print every student with their average, sorted highest first
        pass

    def top_student(self):
        # TODO: return the Student with the highest average
        pass

    def save_to_file(self, filename=FILENAME):
        # TODO: write "name:grade1,grade2,..." for every student
        pass

    def load_from_file(self, filename=FILENAME):
        # TODO: read students back from file, handling FileNotFoundError
        pass


def main():
    # TODO: menu loop tying everything together
    pass


if __name__ == "__main__":
    main()
