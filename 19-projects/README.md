# 19 — Projects

This is where everything comes together. Projects are organized into
three tiers of increasing difficulty. Every project follows the same
11-part structure: Problem Statement, Learning Objectives, Requirements,
Features, Suggested Folder Structure, Step-by-Step Milestones, Starter
Code, Test Cases, Expected Behavior, Extension Challenges, and a Solution
kept in its own `solution/` subfolder.

## How to Use This Folder

1. Read the whole README for a project before writing any code.
2. Build it milestone by milestone in `starter.py`.
3. Run the project's tests as you go:
   ```
   cd 19-projects/<tier>/<project-folder>
   python -m unittest tests.test_<name>
   ```
4. Only open `solution/solution.py` after a genuine attempt.
5. Try at least one extension challenge before moving on.

## Project Tiers

### Beginner Projects — reinforce topics 00-05
| # | Project | Core Skills |
|---|---|---|
| 01 | [Number Guessing Game](beginner-projects/01-number-guessing-game/README.md) | loops, conditions, `random` |
| 02 | [Simple Calculator](beginner-projects/02-simple-calculator/README.md) | functions, operators, exceptions |

### Intermediate Projects — reinforce topics 06-11
| # | Project | Core Skills |
|---|---|---|
| 01 | [To-Do List App](intermediate-projects/01-todo-list-app/README.md) | lists, dictionaries, functions |
| 02 | [Contact Book](intermediate-projects/02-contact-book/README.md) | dictionaries, file handling |
| 03 | [Quiz Game](intermediate-projects/03-quiz-game/README.md) | dictionaries, loops, logic |

### Final Projects — capstones combining everything through 13-oop
| # | Project | Core Skills |
|---|---|---|
| 01 | [Expense Tracker](final-projects/01-expense-tracker/README.md) | OOP, file persistence, aggregation |
| 02 | [Student Management System](final-projects/02-student-management-system/README.md) | OOP, collections of objects, sorting |

## A Note on Testable Design

Every solution here separates **logic** (plain functions/classes with no
`input()`/`print()`) from **input/output** (the menu functions). That's
why each project can be unit tested without simulating keyboard input —
and it's a professional habit worth carrying into your own code.

Once done with these plus topics `14`-`18`, you're ready for
[`20-ai-ml-preparation`](../20-ai-ml-preparation/README.md) if that's your
next interest.
