# Intermediate Project 02 — Contact Book

## 1. Problem Statement
Build a menu-driven contact book that stores contacts (name, phone, email)
and saves/loads them to a text file so they persist between runs.

## 2. Learning Objectives
- Modeling records with a dictionary of dictionaries
- Separating data/logic from file I/O and from menu I/O
- Reading and writing a simple custom text file format
- Handling a missing file gracefully on first run

## 3. Requirements
- Store contacts as `{name: {"phone": ..., "email": ...}}`.
- Menu: Add, View all, Search, Delete, Save & Quit.
- Load `contacts.txt` on startup if it exists; save on quit.
- Handle a missing file and a missing contact gracefully.

## 4. Features
- [ ] Add a contact with name, phone, email
- [ ] View all saved contacts
- [ ] Search for a contact by exact name
- [ ] Delete a contact by name
- [ ] Persist contacts between runs
- [ ] (Stretch) Prevent duplicate names / support partial-name search

## 5. Suggested Folder Structure
```
02-contact-book/
├── README.md
├── starter.py
├── tests/test_contacts.py
└── solution/solution.py
```
File format: one contact per line, `name,phone,email`.

## 6. Step-by-Step Milestones
1. Build `ContactBook` with `add_contact()`, `search_contact()`,
   `delete_contact()` — no I/O inside the class.
2. Add `to_lines()`/`load_from_lines()` for testable serialization.
3. Add `save_to_file()`/`load_from_file()` using real file I/O.
4. Build the menu loop and prompt functions.

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_contacts.py`](tests/test_contacts.py) — includes a round
trip serialization test. Run with:
```
python -m unittest tests.test_contacts
```

## 9. Expected Behavior
```
No existing contact file found. Starting fresh.

1. Add  2. View all  3. Search  4. Delete  5. Save & Quit
Choose an option: 1
Name: Alice
Phone: 555-1234
Email: alice@example.com
Contact added.
```

## 10. Extension Challenges
- Prevent duplicate names (or confirm before overwriting).
- Support partial-name search.
- Store data as JSON instead (see `15-working-with-data`).

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`08-dictionaries`](../../../08-dictionaries/README.md),
[`10-file-handling`](../../../10-file-handling/README.md),
[`11-exceptions`](../../../11-exceptions/README.md).
