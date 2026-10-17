# Basic Data Processing

## Learning Objectives
By the end of this lesson you can:
- Combine CSV/JSON/datetime/pathlib into a single small workflow
- Load tabular data, clean it, compute summary statistics, and save the
  result
- Recognize the shape of a typical "read → process → write" data script

## Concept Explanation

Most real-world "data processing" scripts follow the same shape:

1. **Read** raw data from a file (CSV, JSON, or similar).
2. **Clean/transform** it (fix types, filter bad rows, compute new
   values) — this is where comprehensions and loops from earlier lessons
   get used constantly.
3. **Summarize** it (totals, averages, counts).
4. **Write** the result somewhere (a new file, or printed output).

This lesson doesn't introduce new syntax — it's about combining
`15-working-with-data`'s tools (and `14-intermediate-python`'s
comprehensions) into one realistic pipeline.

## Syntax

No new syntax — this lesson recombines:
```python
import csv
import json
from pathlib import Path
from datetime import date
```

## Examples

**Example 1 — Read a CSV, compute a summary, print it**
```python
import csv

with open("sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

total_sales = sum(float(row["amount"]) for row in rows)
print(f"Total sales: ${total_sales:.2f}")
```
(Assumes a `sales.csv` with an `amount` column — see the runnable
`examples.py` in this folder, which creates one first.)

**Example 2 — Clean and filter data with a comprehension**
```python
raw_scores = ["85", "92", "not available", "78", ""]

valid_scores = []
for score in raw_scores:
    try:
        valid_scores.append(float(score))
    except ValueError:
        continue   # skip anything that isn't a valid number

print(valid_scores)
print(f"Average: {sum(valid_scores) / len(valid_scores):.1f}")
```
Expected output:
```
[85.0, 92.0, 78.0]
Average: 85.0
```

**Example 3 — Group and summarize with a dictionary**
```python
transactions = [
    {"category": "Food", "amount": 20},
    {"category": "Food", "amount": 15},
    {"category": "Transport", "amount": 50},
]

totals_by_category = {}
for transaction in transactions:
    category = transaction["category"]
    totals_by_category[category] = (
        totals_by_category.get(category, 0) + transaction["amount"]
    )

print(totals_by_category)
```
Expected output:
```
{'Food': 35, 'Transport': 50}
```

**Example 4 — Save a processed summary as JSON, tagged with today's date**
```python
import json
from datetime import date

summary = {
    "generated_on": date.today().isoformat(),
    "total_sales": 1234.56,
    "transaction_count": 42,
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=2)

print("Summary saved.")
```
Expected output:
```
Summary saved.
```

## Common Mistakes

- **Not validating/cleaning data before computing with it** — real data
  almost always has missing or malformed values; always expect to filter
  or convert before summarizing (see Example 2).
- **Loading an entire huge file into memory with `list(reader)`** when a
  generator-style loop (processing one row at a time) would do — fine for
  small files, worth reconsidering for very large ones (revisit
  `14-intermediate-python`'s generators lesson).
- **Mixing up what's a string vs. a number after reading CSV** — always
  convert explicitly (`float(row["amount"])`), don't assume.
- **Forgetting to close over the file before trying to read the output
  file you just wrote** — a `with` block handles this automatically; don't
  try to read a file from inside the same `with` block you're still
  writing it in.

## Practice

1. Given a CSV of product names and prices, compute and print the average
   price.
2. Given a list of raw strings representing numbers (with some invalid
   entries mixed in), clean it into a list of valid floats.
3. Given a list of transaction dictionaries, group and sum them by
   category (as in Example 3), then save the result as JSON.
4. Read a CSV of student scores and print only the students who scored
   above the class average.

## Challenge

Write a small pipeline: read a CSV of orders (`product`, `quantity`,
`price`), compute each order's total (`quantity * price`), find the
single most valuable order, and save a JSON summary containing the total
revenue and the top order's details.

## Mini Project

Add a "monthly report" feature to the `19-projects` **Expense Tracker**:
read all saved expenses, group them by category, and write a JSON summary
file tagged with the date it was generated (`date.today().isoformat()`).

## Summary

Real data processing is rarely about one clever trick — it's the
combination of reading data, cleaning/validating it, computing summaries
with the collection tools you already know, and saving the result in a
useful format. This "read → process → write" shape will come up constantly,
including as a bridge into the data-analysis libraries in
`20-ai-ml-preparation`.

## Next Step

You've completed `15-working-with-data`. Continue to
[`16-testing-and-debugging`](../16-testing-and-debugging/README.md).
