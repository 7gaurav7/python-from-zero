# 08 — Dictionaries

## 1. Beginner-Friendly Explanation

A **dictionary** stores data as **key-value pairs** — instead of accessing
items by position (like a list), you access them by a meaningful name (the
key). Think of a real dictionary: you look up a *word* (the key) to find its
*definition* (the value).

```python
student = {"name": "Alice", "age": 25, "grade": "A"}
print(student["name"])   # Alice
```

Dictionaries are one of the most-used data structures in real Python code —
representing a JSON object from a web API, a database row, configuration
settings, and more.

## 2. Important Concepts

- **Key** — the "label" used to look up a value. Keys must be unique and
  unchangeable (usually strings or numbers).
- **Value** — the data associated with a key. Values can be anything,
  including lists or other dictionaries.
- **Key-value pair** — one entry in the dictionary: `"name": "Alice"`.
- **Accessing values** — `dictionary[key]` or the safer `dictionary.get(key)`.
- **Adding/updating** — `dictionary[key] = value` (adds if the key doesn't
  exist, updates if it does).
- **Common methods** — `.keys()`, `.values()`, `.items()`, `.get()`, `.pop()`.
- **Looping over a dictionary** — usually with `.items()` to get both key
  and value at once.

## 3. Syntax

```python
d = {"key1": "value1", "key2": "value2"}

d["key1"]                 # access a value (error if key missing)
d.get("key1")              # access safely (returns None if missing)
d.get("key1", "default")  # access safely with a fallback value

d["key3"] = "value3"       # add a new key-value pair
d["key1"] = "new value"    # update an existing key

del d["key2"]              # remove a key
d.pop("key2")               # remove and return a key's value

d.keys()                    # all keys
d.values()                  # all values
d.items()                   # all (key, value) pairs

for key, value in d.items():
    ...
```

## 4. Simple Examples

**Example 1 — Creating and accessing a dictionary**
```python
student = {"name": "Alice", "age": 25, "grade": "A"}
print(student["name"])
print(student["age"])
```
Expected output:
```
Alice
25
```

**Example 2 — Adding and updating**
```python
student = {"name": "Alice", "age": 25}
student["grade"] = "A"       # add
student["age"] = 26          # update
print(student)
```
Expected output:
```
{'name': 'Alice', 'age': 26, 'grade': 'A'}
```

**Example 3 — Looping over a dictionary**
```python
prices = {"apple": 1.5, "banana": 0.5, "cherry": 3.0}
for item, price in prices.items():
    print(f"{item}: ${price}")
```
Expected output:
```
apple: $1.5
banana: $0.5
cherry: $3.0
```

**Example 4 — Safe access with `.get()`**
```python
student = {"name": "Alice"}
print(student.get("age"))
print(student.get("age", "Unknown"))
```
Expected output:
```
None
Unknown
```

## 5. Practice Problems

1. Create a dictionary representing a book (title, author, year) and print
   each value.
2. Add a new key `"pages"` to that dictionary, then update the `"year"`.
3. Given a dictionary of student names to scores, loop through and print
   each student with their score.
4. Given a dictionary, safely check for a key that might not exist using
   `.get()` with a default value of `"N/A"`.
5. Write a program that counts how many times each word appears in a
   sentence, storing the result in a dictionary (hint: `.split()` + a loop).

## 6. Challenge Problems

1. Build a simple phone book: a dictionary mapping names to phone numbers.
   Let the "program" (hard-coded for now, no input needed) add, look up,
   and delete an entry, printing the dictionary after each step.
2. Given a dictionary of `{"student": [scores]}` (a dictionary of lists),
   compute and print the average score for each student.

## 7. Common Mistakes

- **Accessing a missing key with `[]`** — raises a `KeyError`. Use `.get()`
  when a key might not exist.
- **Assuming dictionaries keep insertion order incorrectly** — modern
  Python (3.7+) *does* preserve insertion order, but don't rely on any
  particular order for logic that needs sorting; sort explicitly instead.
- **Using a mutable type (like a list) as a key** — dictionary keys must be
  immutable (strings, numbers, tuples are fine; lists are not).
- **Confusing `.values()` and `.items()`** when looping — `.items()` gives
  you both the key and value, `.values()` only the value.

## 8. Mini Quiz

1. What are the two parts of every dictionary entry called?
2. What happens if you access a missing key with `d["missing"]`?
3. What method lets you access a key safely without an error?
4. What does `.items()` give you when looping?
5. Can a list be used as a dictionary key?

*(Answers: 1. Key and value  2. It raises a `KeyError`  3. `.get()`  4. Both the key and the value, as a pair  5. No — dictionary keys must be immutable)*

## 9. Practical Exercise

Create `contact_lookup.py` that stores a dictionary of 3 contacts (name →
phone number), asks the user to type a name, and prints that contact's
number, or `"Contact not found"` if the name isn't in the dictionary.

➡️ Matching files: [`exercises/08_dictionaries_exercises.py`](../exercises/08_dictionaries_exercises.py) ·
[`solutions/08_dictionaries_solutions.py`](../solutions/08_dictionaries_solutions.py)

**Previous:** [`07-lists-tuples-sets`](../07-lists-tuples-sets/README.md) | **Next:** [`09-functions`](../09-functions/README.md)
