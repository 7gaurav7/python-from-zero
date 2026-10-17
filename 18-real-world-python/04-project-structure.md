# Project Structure

## Learning Objectives
By the end of this lesson you can:
- Organize a multi-file Python project into a sensible folder layout
- Explain the purpose of a `.gitignore` file
- Separate source code, tests, and documentation cleanly
- Recognize this structure in the `19-projects` folder you've already used

## Concept Explanation

A single-file script is fine for a quick exercise, but a real project
needs a predictable place for everything: the actual code, its tests, its
dependencies, and its documentation. You've actually been using a
well-organized structure throughout `19-projects` already — this lesson
makes the pattern explicit so you can apply it to projects of your own.

A typical small real-world Python project looks like:

```
my-project/
├── README.md              ← what it is, how to run it (17-git-and-github)
├── requirements.txt        ← dependencies (previous lesson)
├── .gitignore               ← files Git should never track
├── venv/                     ← virtual environment (never committed)
├── main.py                   ← entry point
├── my_project/                ← the actual package/source code (for larger projects)
│   ├── __init__.py
│   ├── models.py
│   └── utils.py
└── tests/
    └── test_models.py
```

## Syntax

A `.gitignore` file lists patterns Git should ignore — never stage, never
commit, never show in `git status`:

```
# .gitignore
venv/
__pycache__/
*.pyc
.env
*.log
```

## Examples

**Example 1 — A minimal single-file project (what you've built so far)**
```
number-guessing-game/
├── README.md
├── starter.py
└── solution/
    └── solution.py
```
This is exactly the shape of every project in `19-projects/beginner-projects`
— perfectly appropriate for a small, single-purpose script.

**Example 2 — A small project that's grown multiple files**
```
contact-book/
├── README.md
├── requirements.txt
├── main.py                  ← runs the menu loop
├── contact_book.py            ← the ContactBook class
└── tests/
    └── test_contact_book.py
```
Splitting one big file into focused pieces (the class, the CLI, the tests)
makes each part easier to find, read, and test independently — this is
exactly the separation the `19-projects` solutions already demonstrate
between their `solution.py` and `tests/`.

**Example 3 — A `.gitignore` for a typical Python project**
```
# .gitignore
venv/
__pycache__/
*.pyc
.env
*.egg-info/
.DS_Store
```
```
$ git status
On branch main
nothing to commit, working tree clean
```
Even though `venv/` and `__pycache__/` physically exist in the folder,
`.gitignore` keeps them out of `git status` and `git add .` entirely.

**Example 4 — A package-style layout for a larger project**
```
expense_tracker/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── expense_tracker/
│   ├── __init__.py
│   ├── models.py        ← Expense, ExpenseTracker classes
│   ├── storage.py         ← save_to_file / load_from_file
│   └── cli.py              ← menu functions
└── tests/
    ├── test_models.py
    └── test_storage.py
```
This mirrors the "separate logic from I/O" principle from
`19-projects`, taken one step further by splitting into multiple files
once a project grows large enough to justify it.

## Common Mistakes

- **Over-structuring a tiny script.** A 30-line script doesn't need a
  `my_project/` package folder and five subfiles — that's needless
  complexity. Reach for more structure only once a single file becomes
  genuinely hard to navigate.
- **Forgetting a `.gitignore`**, leading to `venv/` or `__pycache__/`
  getting accidentally committed — bloats the repository and can cause
  confusing conflicts between different people's operating systems.
- **Mixing test files into the main source folder** with no clear
  separation — a dedicated `tests/` folder (as `19-projects` uses) keeps
  the distinction obvious at a glance.
- **Not having a single, clear entry point** — someone opening the project
  should be able to tell immediately which file to run first (often
  `main.py`).

## Practice

1. Look at one of your completed `19-projects` folders and describe (in a
   comment or a short paragraph) how its structure separates concerns
   (README, starter/solution, tests).
2. Write a `.gitignore` file appropriate for a Python project using a
   virtual environment.
3. Take a single-file script you've written in an earlier topic and split
   it into two files: one holding a class/functions, one holding the
   "main" code that uses them.
4. Add a `tests/` folder to that split project with at least one test file.

## Challenge

Reorganize one of your own multi-file practice projects (or a `19-projects`
project you've extended) into the "package-style" layout from Example 4 —
a `your_project_name/` folder holding the source files, separate from
`main.py` and `tests/`.

## Mini Project

No dedicated mini project — apply the practices in this lesson going
forward to `20-ai-ml-preparation` and any project you build after this
course.

## Summary

A clear project structure — README, requirements.txt, `.gitignore`, a
clear entry point, separated source and tests — makes a project easier to
understand, run, and safely share, whether that's with a teammate or with
your own future self returning to the code months later. `19-projects`
has been demonstrating this structure throughout the course.

## Next Step

Continue to [`05-configuration-basics.md`](05-configuration-basics.md).
