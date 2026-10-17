"""
15 - Working with Data: Basic Data Processing
Runnable examples matching the lesson.
Running this script creates 'sales.csv' and 'summary.json' in this folder.
"""
import csv
import json
from datetime import date

# --- Setup: create a small sales.csv so Example 1 has something to read ---
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "amount"])
    writer.writerow(["Widget", "19.99"])
    writer.writerow(["Gadget", "45.00"])
    writer.writerow(["Gizmo", "9.50"])

# Example 1: read a CSV, compute a summary, print it
with open("sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

total_sales = sum(float(row["amount"]) for row in rows)
print(f"Total sales: ${total_sales:.2f}")
# Expected output: Total sales: $74.49

# Example 2: clean and filter data with a comprehension-friendly loop
raw_scores = ["85", "92", "not available", "78", ""]

valid_scores = []
for score in raw_scores:
    try:
        valid_scores.append(float(score))
    except ValueError:
        continue

print(valid_scores)
print(f"Average: {sum(valid_scores) / len(valid_scores):.1f}")
# Expected output:
# [85.0, 92.0, 78.0]
# Average: 85.0

# Example 3: group and summarize with a dictionary
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
# Expected output: {'Food': 35, 'Transport': 50}

# Example 4: save a processed summary as JSON, tagged with today's date
summary = {
    "generated_on": date.today().isoformat(),
    "total_sales": total_sales,
    "transaction_count": len(rows),
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=2)

print("Summary saved.")
# Expected output: Summary saved.
