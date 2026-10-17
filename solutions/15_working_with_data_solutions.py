"""
Solutions for 15 - Working with Data
Try the exercises yourself first! (exercises/15_working_with_data_exercises.py)
Running this script creates/modifies a few small files in this folder.
"""
import csv
import json
from pathlib import Path
from datetime import date, datetime

# --- 01: JSON ---
book = {"title": "Dune", "author": "Frank Herbert", "year": 1965}
print(json.dumps(book))

my_data = {"favorite_language": "Python", "years_learning": 1}
with open("my_data.json", "w") as file:
    json.dump(my_data, file)
with open("my_data.json", "r") as file:
    reloaded = json.load(file)
print(reloaded["favorite_language"])

# --- 02: CSV ---
with open("practice.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "quantity"])
    writer.writerow(["Pens", 10])
    writer.writerow(["Notebooks", 5])

with open("practice.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["item"])

# --- 03: datetime ---
today = date.today()
print(today.strftime("%d/%m/%Y"))

parsed = datetime.strptime("2026-07-04", "%Y-%m-%d")
print(parsed.month)

# --- 04: pathlib ---
report_path = Path("output") / "report.txt"
print(report_path)

python_files = list(Path(".").glob("*.py"))
print(python_files)

# --- 05: Basic Data Processing ---
raw_scores = ["90", "oops", "75", "", "60"]
clean_scores = []
for score in raw_scores:
    try:
        clean_scores.append(float(score))
    except ValueError:
        continue
print(clean_scores)

transactions = [
    {"category": "Food", "amount": 12},
    {"category": "Fun", "amount": 30},
    {"category": "Food", "amount": 8},
]
totals = {}
for t in transactions:
    totals[t["category"]] = totals.get(t["category"], 0) + t["amount"]
with open("totals.json", "w") as file:
    json.dump(totals, file)
print(totals)


# --- Challenges ---
def save_students(students, filename):
    with open(filename, "w") as file:
        json.dump(students, file)


def load_students(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


save_students([{"name": "Alice"}, {"name": "Bob"}], "students_challenge.json")
print(load_students("students_challenge.json"))
print(load_students("does_not_exist.json"))


def average_column(filename, column_name):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        values = [float(row[column_name]) for row in reader]
    return sum(values) / len(values)


print(average_column("practice.csv", "quantity"))


def age_in_days(birth_date_text):
    birth_date = datetime.strptime(birth_date_text, "%Y-%m-%d").date()
    return (date.today() - birth_date).days


print(age_in_days("2000-01-01"))
