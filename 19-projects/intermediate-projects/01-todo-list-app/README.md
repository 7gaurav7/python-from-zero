# Intermediate Project 01 — To-Do List App

## 1. Problem Statement
Build a menu-driven, command-line to-do list. The user can add tasks, view
them, mark them complete, and remove them while the program is running.

## 2. Learning Objectives
- Separating data/logic (`TaskManager`) from input/output (menu functions)
- Representing structured records with dictionaries inside a list
- Writing a menu loop driven by a dictionary of actions
- Raising/catching exceptions for invalid operations instead of special
  "error" return values

## 3. Requirements
- Store tasks as a list of dictionaries: `{"text": ..., "done": False}`.
- Menu: Add task, View tasks, Mark complete, Remove task, Quit.
- Display completed tasks differently (`[x]` vs `[ ]`).
- Handle invalid menu choices and invalid task numbers gracefully.

## 4. Features
- [ ] Add a task with a non-empty description
- [ ] View all tasks with clear complete/incomplete markers
- [ ] Mark any task complete by its number
- [ ] Remove any task by its number
- [ ] Menu loop that only exits on "Quit"
- [ ] (Stretch) Persist tasks to a file between runs

## 5. Suggested Folder Structure
```
01-todo-list-app/
├── README.md
├── starter.py
├── tests/test_todo.py
└── solution/solution.py
```

## 6. Step-by-Step Milestones
1. Build `TaskManager` with `add_task()`, `list_tasks()`,
   `complete_task()`, `remove_task()` — no `input()`/`print()` inside.
2. Write "prompt" functions that call `input()` and use `TaskManager`.
3. Tie it together with a menu loop.
4. Handle bad input everywhere realistic.
5. (Stretch) Save/load tasks to/from a file (see `10-file-handling`).

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_todo.py`](tests/test_todo.py). Run with:
```
python -m unittest tests.test_todo
```

## 9. Expected Behavior
```
1. Add task
2. View tasks
3. Mark complete
4. Remove task
5. Quit
Choose an option: 1
Task description: Buy milk
Task added.
```

## 10. Extension Challenges
- Save/load the to-do list to/from a file.
- Add due dates (pairs well with `15-working-with-data`'s datetime lesson).
- Sort so incomplete tasks show first.
- Add priority levels and sort by priority.

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`07-lists-tuples-sets`](../../../07-lists-tuples-sets/README.md),
[`08-dictionaries`](../../../08-dictionaries/README.md),
[`09-functions`](../../../09-functions/README.md).
