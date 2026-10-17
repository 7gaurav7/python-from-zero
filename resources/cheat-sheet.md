# 🧾 Python Cheat Sheet

A quick reference for everything covered in this course. Use `Ctrl+F` /
`Cmd+F` to jump to what you need.

## Output & Input
```python
print("text")
print(a, b, c)               # space-separated
print(f"{variable}")         # f-string
input("Prompt: ")             # always returns a str
```

## Variables & Types
```python
x = 5            # int
y = 3.14         # float
name = "Alice"    # str
flag = True       # bool
type(x)           # check type
int(x); float(x); str(x)   # convert types
```

## Operators
```python
+ - * / // % **        # arithmetic
== != > < >= <=        # comparison
and or not               # logical
= += -= *= /=          # assignment
```

## Conditions
```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

## Loops
```python
for i in range(5):
    ...

for i in range(2, 10, 2):
    ...

while condition:
    ...

break       # exit loop
continue    # skip to next iteration
```

## Strings
```python
s[0]; s[-1]; s[0:3]; s[::-1]
len(s)
s.upper(); s.lower(); s.strip()
s.replace("a", "b")
s.split(","); "-".join(list_of_strings)
s.startswith("x"); s.endswith("y")
```

## Lists
```python
lst = [1, 2, 3]
lst.append(4)
lst.remove(2)
lst.pop()
lst.sort()
lst[0]; lst[0:2]
len(lst)
x in lst
```

## Tuples
```python
t = (1, 2, 3)   # immutable
t[0]
```

## Sets
```python
s = {1, 2, 3}
s.add(4)
s.remove(2)
set1 & set2     # intersection
set1 | set2     # union
```

## Dictionaries
```python
d = {"key": "value"}
d["key"]
d.get("key", "default")
d["new_key"] = "value"
del d["key"]
d.keys(); d.values(); d.items()
for k, v in d.items():
    ...
```

## Functions
```python
def name(param1, param2="default"):
    return param1 + param2

result = name(1, 2)
```

## File Handling
```python
with open("file.txt", "w") as f:
    f.write("text\n")

with open("file.txt", "a") as f:
    f.write("more text\n")

with open("file.txt", "r") as f:
    content = f.read()
    # or:
    for line in f:
        ...
```

## Exceptions
```python
try:
    risky()
except ValueError:
    ...
except (TypeError, KeyError) as e:
    ...
else:
    ...
finally:
    ...
```

## Modules
```python
import math
math.sqrt(16)

from math import sqrt
sqrt(16)

import random
random.randint(1, 6)
random.choice(["a", "b"])
random.shuffle(a_list)
random.sample(range(1, 50), 6)

if __name__ == "__main__":
    main()
```

## OOP
```python
class ClassName:
    def __init__(self, param):
        self.attribute = param

    def method(self):
        return self.attribute

obj = ClassName("value")
obj.method()

class Child(ClassName):
    def __init__(self, param, extra):
        super().__init__(param)
        self.extra = extra
```

## Comprehensions, Lambda, map/filter (14)
```python
[expr for item in iterable if condition]        # list comprehension
{key: value for item in iterable}                 # dict comprehension
{expr for item in iterable}                        # set comprehension

square = lambda n: n ** 2
list(map(lambda n: n * 2, numbers))
list(filter(lambda n: n % 2 == 0, numbers))
```

## *args / **kwargs, enumerate/zip, unpacking (14)
```python
def f(*args, **kwargs):
    ...                      # args: tuple, kwargs: dict

f(*my_list)                   # unpack a list into positional args
f(**my_dict)                  # unpack a dict into keyword args

for i, value in enumerate(items, start=1):
    ...
for a, b in zip(list1, list2):
    ...

first, *rest = [1, 2, 3, 4]
```

## Iterators, Generators, Decorators (14)
```python
iterator = iter(iterable)
next(iterator)                 # raises StopIteration when exhausted

def gen():
    yield 1
    yield 2

def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def some_function():
    ...
```

## JSON, CSV, datetime, pathlib (15)
```python
import json
json.dumps(obj); json.loads(text)
json.dump(obj, file); json.load(file)

import csv
reader = csv.DictReader(file)
writer = csv.DictWriter(file, fieldnames=[...])

from datetime import date, datetime, timedelta
date.today(); datetime.now()
some_date.strftime("%Y-%m-%d")
datetime.strptime(text, "%Y-%m-%d")

from pathlib import Path
Path("folder") / "file.txt"
path.read_text(); path.write_text("...")
```

## Testing (16)
```python
assert condition, "message if False"

import unittest

class TestSomething(unittest.TestCase):
    def test_case(self):
        self.assertEqual(actual, expected)
        self.assertRaises(ValueError, func, arg)

if __name__ == "__main__":
    unittest.main()
```
```python
# pytest style (requires: pip install pytest)
def test_case():
    assert actual == expected
```

## Git (17)
```
git init
git status
git add <file>
git commit -m "message"
git log --oneline
git branch <name>
git switch <name>        # or: git checkout <name>
git merge <branch>
git remote add origin <url>
git push -u origin main
git pull
git clone <url>
```

## Real-World Project Setup (18)
```
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate          # Windows

pip install <package>
pip freeze > requirements.txt
pip install -r requirements.txt
```
```python
import os
value = os.environ.get("MY_VARIABLE", "default_value")
```

