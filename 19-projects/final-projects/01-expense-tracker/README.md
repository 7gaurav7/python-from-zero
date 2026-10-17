# Final Project 01 — Expense Tracker

## 1. Problem Statement
Build a command-line application to track personal expenses: add them,
categorize them, view summaries, and persist everything to a file.

## 2. Learning Objectives
- Designing two cooperating classes (`Expense`, `ExpenseTracker`)
- Serializing objects to/from plain text and testing the round trip
- Aggregating data with dictionaries (per-category totals)
- Building a menu-driven CLI robust to realistic bad input

## 3. Requirements

### Functional
- Add an expense (amount, category, description).
- View all expenses; view totals per category and overall.
- Delete an expense by number.
- Persist expenses to a file, reloading on startup.
- Handle bad input (non-numeric amounts, missing file, invalid menu
  choices) without crashing.

### Technical
- `Expense` class with `amount`, `category`, `description`.
- `ExpenseTracker` class with `add_expense()`, `total_by_category()`,
  `total_spent()`, `save_to_file()`, `load_from_file()`.
- PEP 8, standard library only.

## 4. Features
- [ ] Add an expense with amount, category, description
- [ ] View all expenses in a numbered list
- [ ] View totals by category and overall
- [ ] Delete an expense by number
- [ ] Persist and auto-reload expenses
- [ ] (Stretch) Dates and month-based filtering

## 5. Suggested Folder Structure
```
01-expense-tracker/
├── README.md
├── starter.py
├── tests/test_expense_tracker.py
└── solution/solution.py
```

## 6. Step-by-Step Milestones
1. Core data model: `Expense`, add/view (no file saving).
2. Summaries: `total_by_category()`, `total_spent()`.
3. Persistence: `save_to_file()`/`load_from_file()`.
4. Robustness: handle bad amounts, missing files, invalid choices.
5. (Stretch) Dates via `datetime` (see `15-working-with-data`) and
   month filtering.

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_expense_tracker.py`](tests/test_expense_tracker.py). Run with:
```
python -m unittest tests.test_expense_tracker
```

## 9. Expected Behavior
```
No existing expense file found. Starting fresh.

1. Add expense
2. View expenses
3. Category summary
4. Delete expense
5. Save & Quit
Choose an option: 1
Amount: 45.50
Category: Food
Description: Weekly groceries
Expense added.
```

## 10. Extension Challenges
- Export a summary report to `report.txt`.
- Add a monthly budget per category and warn when exceeded.
- Sort expenses by amount or category.

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`13-oop`](../../../13-oop/README.md),
[`10-file-handling`](../../../10-file-handling/README.md),
[`15-working-with-data`](../../../15-working-with-data/README.md).
