"""
Exercises for 15 - Working with Data
Each section matches one lesson file in 15-working-with-data/.
Write your code below each numbered comment.
"""

# --- 01: JSON ---
# 1. Convert a Python dictionary representing a book (title, author, year)
#    to a JSON string and print it.


# 2. Save a dictionary of your own data to my_data.json, then reload it
#    and print one of its values.


# --- 02: CSV ---
# 3. Write a CSV file with 3 rows of your own data using csv.writer.


# 4. Read that file back using csv.DictReader and print one column per row.


# --- 03: datetime ---
# 5. Print today's date formatted as "DD/MM/YYYY".


# 6. Parse the string "2026-07-04" into a date and print just the month.


# --- 04: pathlib ---
# 7. Create a Path for "report.txt" inside a folder called "output", and
#    print the joined path.


# 8. List all .py files in the current directory using .glob("*.py").


# --- 05: Basic Data Processing ---
# 9. Given a list of raw strings representing numbers (with some invalid
#    entries mixed in), clean it into a list of valid floats.


# 10. Given a list of transaction dictionaries, group and sum them by
#     category, then save the result as JSON.


# --- Challenges ---
# C1. Write save_students(students, filename) / load_students(filename)
#     functions using JSON, handling a missing file gracefully.
# C2. Write average_column(filename, column_name) that reads a CSV with
#     csv.DictReader and returns the average of a numeric column.
# C3. Write age_in_days(birth_date_text) that returns how many days old
#     someone is, given a "YYYY-MM-DD" birth date string.
