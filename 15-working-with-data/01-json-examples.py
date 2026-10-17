"""
15 - Working with Data: JSON
Runnable examples matching the lesson.
Running this script creates/modifies 'student.json' in this folder.
"""
import json

# Example 1: converting a Python dict to a JSON string
student = {"name": "Alice", "age": 25, "active": True}
json_text = json.dumps(student)
print(json_text)
print(type(json_text))
# Expected output:
# {"name": "Alice", "age": 25, "active": true}
# <class 'str'>

# Example 2: converting a JSON string back to Python
json_text = '{"name": "Bob", "age": 30}'
data = json.loads(json_text)
print(data["name"])
print(type(data))
# Expected output:
# Bob
# <class 'dict'>

# Example 3: writing to and reading from a .json file
data = {"name": "Alice", "scores": [90, 85, 95]}

with open("student.json", "w") as file:
    json.dump(data, file, indent=2)

with open("student.json", "r") as file:
    loaded = json.load(file)

print(loaded["scores"])
# Expected output: [90, 85, 95]

# Example 4: pretty-printing with indent
data = {"name": "Alice", "age": 25}
print(json.dumps(data, indent=2))
# Expected output:
# {
#   "name": "Alice",
#   "age": 25
# }
