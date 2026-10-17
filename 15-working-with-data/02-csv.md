# Working with CSV

## Learning Objectives
- Explain what a CSV file is and where you'll encounter one
- Read a CSV file with the `csv` module
- Write Python data out to a CSV file
- Use `csv.DictReader`/`csv.DictWriter` for rows as dictionaries

## Concept Explanation
**CSV** ("Comma-Separated Values") is plain-text tabular data -- the kind
you'd see in a spreadsheet.
```
name,age,city
Alice,25,Paris
Bob,30,London
```
You *could* parse this with `.split(",")`, but real CSV has edge cases
(commas inside quoted text) the `csv` module already handles correctly.

## Syntax
```python
import csv

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)          # rows as lists
    reader = csv.DictReader(file)       # rows as dicts (first row = headers)

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25})
```

## Examples

**Example 1 - Writing with `csv.writer`**
```python
import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])
print("File written.")
```
Expected output: `File written.`

**Example 2 - Reading with `csv.reader`**
```python
import csv
with open("students.csv", "r", newline="") as file:
    for row in csv.reader(file):
        print(row)
```
Expected output:
```
['name', 'score']
['Alice', '90']
['Bob', '85']
```
(Every value is a **string** -- convert numbers yourself.)

**Example 3 - Reading with `csv.DictReader`**
```python
import csv
with open("students.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        print(row["name"], "scored", row["score"])
```
Expected output:
```
Alice scored 90
Bob scored 85
```

**Example 4 - Writing with `csv.DictWriter`**
```python
import csv
students = [{"name": "Carla", "score": 78}, {"name": "Dan", "score": 92}]
with open("more_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)
print("File written.")
```
Expected output: `File written.`

## Common Mistakes
- Forgetting `newline=""` when opening a CSV file (can cause blank lines).
- Forgetting every value read is a string -- convert with `int()`/`float()`.
- Mismatched `fieldnames` in `DictWriter`.
- Using `.split(",")` instead of `csv` for anything beyond the simplest data.

## Practice
1. Write a CSV file with 3 rows of your own data using `csv.writer`.
2. Read it back with `csv.reader` and print each row.
3. Reread it with `csv.DictReader`, printing one column per row.
4. Write a list of dicts to CSV using `csv.DictWriter`.

## Challenge
Write `average_column(filename, column_name)` that reads a CSV with
`csv.DictReader` and returns the average of a numeric column.

## Mini Project
Add a CSV export option (`csv.DictWriter`) to the `19-projects` Expense
Tracker, alongside its existing plain-text save format.

## Summary
CSV is the standard plain-text tabular format. `reader`/`writer` work with
plain lists; `DictReader`/`DictWriter` work with dictionaries by column
name. Every value read is a string -- convert types yourself.

## Next Step
Continue to [`03-datetime.md`](03-datetime.md).
