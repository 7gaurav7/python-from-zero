# Working with JSON

## Learning Objectives
- Explain what JSON is and why it's used to exchange data
- Convert between Python objects and JSON with `json.dumps()`/`json.loads()`
- Read/write `.json` files with `json.dump()`/`json.load()`
- Map Python types to their JSON equivalents

## Concept Explanation
**JSON** ("JavaScript Object Notation") is a lightweight, text-based
format for structured data, looking almost exactly like a Python
dictionary/list combined -- which is why converting between them is so
direct. JSON is the most common format for web APIs, config files, and
saving structured application data.
```json
{"name": "Alice", "age": 25, "hobbies": ["reading", "chess"]}
```
Python's `json` module converts between this text format and native
Python objects.

## Syntax
```python
import json
json.dumps(python_object)     # Python -> JSON string
json.loads(json_string)        # JSON string -> Python
json.dump(python_object, file) # Python -> write to a file
json.load(file)                 # read a file -> Python
```
| Python | JSON |
|---|---|
| `dict` | object `{}` |
| `list` | array `[]` |
| `str` | string |
| `int`/`float` | number |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

## Examples

**Example 1 - Python dict to JSON string**
```python
import json
student = {"name": "Alice", "age": 25, "active": True}
print(json.dumps(student))
```
Expected output: `{"name": "Alice", "age": 25, "active": true}`

**Example 2 - JSON string back to Python**
```python
import json
data = json.loads('{"name": "Bob", "age": 30}')
print(data["name"], type(data))
```
Expected output: `Bob <class 'dict'>`

**Example 3 - Writing/reading a `.json` file**
```python
import json
data = {"name": "Alice", "scores": [90, 85, 95]}
with open("student.json", "w") as file:
    json.dump(data, file, indent=2)
with open("student.json", "r") as file:
    loaded = json.load(file)
print(loaded["scores"])
```
Expected output: `[90, 85, 95]`

**Example 4 - Pretty-printing with `indent`**
```python
import json
print(json.dumps({"name": "Alice", "age": 25}, indent=2))
```
Expected output:
```
{
  "name": "Alice",
  "age": 25
}
```

## Common Mistakes
- Confusing `.dump`/`.load` (files) with `.dumps`/`.loads` (strings).
- Trying to `json.dumps()` something JSON can't represent (a `set`, a
  custom class) -- raises `TypeError`; convert to list/dict first.
- Forgetting JSON `true`/`false`/`null` map to Python `True`/`False`/`None`.
- Assuming a tuple round-trips as a tuple -- it becomes a JSON array and
  reads back as a `list`.

## Practice
1. Convert a book dict (title, author, year) to a JSON string.
2. Convert a JSON string list of numbers back to Python and sum it.
3. Save a dict to `my_data.json`, then reload and print one value.
4. Pretty-print a nested dictionary with `indent=2`.

## Challenge
Write `save_students(students, filename)` and `load_students(filename)`
(returning `[]` if the file doesn't exist yet) for a list of student dicts.

## Mini Project
Update the `19-projects` Contact Book to save/load contacts as JSON
instead of comma-separated text.

## Summary
JSON maps almost directly onto Python dicts/lists. `dumps`/`loads` work
with strings; `dump`/`load` work directly with files. It's the standard
format for structured data and web APIs.

## Next Step
Continue to [`02-csv.md`](02-csv.md).
