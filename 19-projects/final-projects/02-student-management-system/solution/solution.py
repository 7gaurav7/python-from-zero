"""
Final Project 02 - Student Management System (solution)

File format (one student per line):
    name:grade1,grade2,grade3
"""

FILENAME = "students.txt"


class Student:
    """Represents a single student and their grades."""

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def to_line(self):
        grades_text = ",".join(str(g) for g in self.grades)
        return f"{self.name}:{grades_text}"

    @classmethod
    def from_line(cls, line):
        name, grades_text = line.strip().split(":", 1)
        student = cls(name)
        if grades_text:
            student.grades = [float(g) for g in grades_text.split(",")]
        return student


class Classroom:
    """Holds a collection of Student objects, keyed by name."""

    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print(f"{name} is already in the class.")
            return
        self.students[name] = Student(name)

    def get_student(self, name):
        return self.students.get(name)

    def class_summary(self):
        if not self.students:
            print("No students yet.")
            return
        ranked = sorted(
            self.students.values(), key=lambda s: s.average(), reverse=True
        )
        print("\n-- Class Summary (highest average first) --")
        for student in ranked:
            print(f"{student.name}: avg={student.average():.1f} ({student.letter_grade()})")

    def top_student(self):
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.average())

    def save_to_file(self, filename=FILENAME):
        with open(filename, "w") as file:
            for student in self.students.values():
                file.write(student.to_line() + "\n")

    def load_from_file(self, filename=FILENAME):
        try:
            with open(filename, "r") as file:
                for line in file:
                    if line.strip():
                        student = Student.from_line(line)
                        self.students[student.name] = student
            print(f"Loaded {len(self.students)} student(s).")
        except FileNotFoundError:
            print("No existing student file found. Starting fresh.")


def prompt_add_student(classroom):
    name = input("Student name: ").strip()
    classroom.add_student(name)


def prompt_add_grade(classroom):
    name = input("Student name: ").strip()
    student = classroom.get_student(name)
    if not student:
        print("Student not found.")
        return
    try:
        grade = float(input("Grade (0-100): "))
        student.add_grade(grade)
        print("Grade added.")
    except ValueError:
        print("Please enter a valid number.")


def prompt_view_student(classroom):
    name = input("Student name: ").strip()
    student = classroom.get_student(name)
    if not student:
        print("Student not found.")
        return
    print(f"\n{student.name}")
    print(f"Grades: {student.grades}")
    print(f"Average: {student.average():.1f}")
    print(f"Letter grade: {student.letter_grade()}")


def show_top_student(classroom):
    top = classroom.top_student()
    if top:
        print(f"Top student: {top.name} (avg={top.average():.1f})")
    else:
        print("No students yet.")


def main():
    classroom = Classroom()
    classroom.load_from_file()

    menu = (
        "\n1. Add student\n2. Add grade\n3. View student\n4. Class summary"
        "\n5. Top student\n6. Save & Quit"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            prompt_add_student(classroom)
        elif choice == "2":
            prompt_add_grade(classroom)
        elif choice == "3":
            prompt_view_student(classroom)
        elif choice == "4":
            classroom.class_summary()
        elif choice == "5":
            show_top_student(classroom)
        elif choice == "6":
            classroom.save_to_file()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
