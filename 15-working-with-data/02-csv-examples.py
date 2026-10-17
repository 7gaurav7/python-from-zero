"""15 - Working with Data: CSV
Creates 'students.csv' and 'more_students.csv' when run."""
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])
print("File written.")

with open("students.csv", "r", newline="") as file:
    for row in csv.reader(file):
        print(row)

with open("students.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        print(row["name"], "scored", row["score"])

students = [{"name": "Carla", "score": 78}, {"name": "Dan", "score": 92}]
with open("more_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)
print("File written.")
