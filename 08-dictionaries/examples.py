"""
Topic 08 - Dictionaries
Runnable examples matching the README.
"""

# Example 1: creating and accessing a dictionary
student = {"name": "Alice", "age": 25, "grade": "A"}
print(student["name"])
print(student["age"])
# Expected output:
# Alice
# 25

# Example 2: adding and updating
student = {"name": "Alice", "age": 25}
student["grade"] = "A"       # add
student["age"] = 26          # update
print(student)
# Expected output: {'name': 'Alice', 'age': 26, 'grade': 'A'}

# Example 3: looping over a dictionary
prices = {"apple": 1.5, "banana": 0.5, "cherry": 3.0}
for item, price in prices.items():
    print(f"{item}: ${price}")
# Expected output:
# apple: $1.5
# banana: $0.5
# cherry: $3.0

# Example 4: safe access with .get()
student = {"name": "Alice"}
print(student.get("age"))
print(student.get("age", "Unknown"))
# Expected output:
# None
# Unknown
