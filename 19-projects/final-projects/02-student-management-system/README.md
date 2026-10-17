# Final Project 02 — Student Management System

## 1. Problem Statement
Build a command-line system for managing a small class of students: add
students, record grades, compute averages/letter grades, and persist data.

## 2. Learning Objectives
- Modeling a one-to-many relationship (`Classroom` holding many `Student`s)
- Deriving computed values (`average()`, `letter_grade()`) from state
- Ranking objects by a computed property
- Designing and testing a text file format for a collection of objects

## 3. Requirements

### Functional
- Add a student by name; add one or more grades.
- View a student's full record (grades, average, letter grade).
- View a class summary sorted by average, highest first.
- Identify the top-performing student.
- Persist all data to a file, reloading on startup.

### Technical
- `Student` class with `add_grade()`, `average()`, `letter_grade()`.
- `Classroom` class with `add_student()`, `get_student()`,
  `class_summary()`, `top_student()`, `save_to_file()`, `load_from_file()`.
- PEP 8, standard library only.

## 4. Features
- [ ] Add a student by name
- [ ] Add grades to a student
- [ ] View a student's full record
- [ ] View a class summary sorted by average
- [ ] Identify the top-performing student
- [ ] Persist and auto-reload data
- [ ] (Stretch) Multiple subjects per student

## 5. Suggested Folder Structure
```
02-student-management-system/
├── README.md
├── starter.py
├── tests/test_student_system.py
└── solution/solution.py
```
File format: one student per line, `name:grade1,grade2,grade3`.

## 6. Step-by-Step Milestones
1. Core data model: `Student.add_grade()`, `average()`, `letter_grade()`;
   `Classroom.add_student()`.
2. Viewing: single-student record and sorted class summary.
3. Persistence: save/load using your own file format.
4. Robustness: invalid grades, duplicate/unknown names, bad menu choices.
5. (Stretch) `top_student()` and `class_average()`.

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_student_system.py`](tests/test_student_system.py). Run with:
```
python -m unittest tests.test_student_system
```

## 9. Expected Behavior
```
No existing student file found. Starting fresh.

1. Add student
2. Add grade
3. View student
4. Class summary
5. Top student
6. Save & Quit
Choose an option: 1
Student name: Alice
```

## 10. Extension Challenges
- Support multiple subjects per student.
- Export the class summary to a formatted report file.
- Validate grades are between 0 and 100.

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`13-oop`](../../../13-oop/README.md),
[`10-file-handling`](../../../10-file-handling/README.md),
[`04-conditions`](../../../04-conditions/README.md).
