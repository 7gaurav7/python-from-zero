# 01 — Variables and Data Types

## 1. Beginner-Friendly Explanation

A **variable** is a named box where you store a piece of information so you
can use it later. Instead of typing `"Alice"` over and over, you store it
once in a box named `name`, and refer to `name` afterward.

```python
name = "Alice"
```

Here, `name` is the box, `=` means "store the following value in this box",
and `"Alice"` is what goes inside. Later, whenever you write `name`, Python
looks inside the box and gives you `"Alice"`.

Different boxes hold different **types** of information — some hold whole
numbers, some hold decimals, some hold text, and some hold True/False values.
Python figures out the type automatically based on what you store.

## 2. Important Concepts

- **Variable** — a name that refers to a stored value.
- **Assignment** — using `=` to store a value in a variable.
- **Data type** — the kind of value stored. The core beginner types:
  - `int` — whole numbers: `5`, `-3`, `1000`
  - `float` — decimal numbers: `3.14`, `-0.5`, `2.0`
  - `str` — text ("string"), always in quotes: `"hello"`, `'Python'`
  - `bool` — `True` or `False`
- **Dynamic typing** — in Python you don't have to declare a type up front;
  it's inferred from the value.
- **Naming rules** — variable names can use letters, numbers, and
  underscores, but can't start with a number, and can't be a reserved
  Python keyword (like `print` or `if`).
- **Naming convention (PEP 8)** — use `snake_case` for variable names:
  `first_name`, not `firstName` or `FirstName`.

## 3. Syntax

```python
variable_name = value          # assignment
type(variable_name)            # check the type of a variable
```

Examples of each type:
```python
age = 25          # int
price = 19.99      # float
name = "Alice"      # str
is_student = True  # bool
```

Checking a type:
```python
print(type(age))   # <class 'int'>
```

## 4. Simple Examples

**Example 1 — Creating and printing variables**
```python
name = "Alice"
age = 25
print(name)
print(age)
```
Expected output:
```
Alice
25
```

**Example 2 — Checking types**
```python
height = 5.9
is_sunny = True
print(type(height))
print(type(is_sunny))
```
Expected output:
```
<class 'float'>
<class 'bool'>
```

**Example 3 — Reassigning a variable**
```python
score = 10
print(score)
score = 20      # overwrites the old value
print(score)
```
Expected output:
```
10
20
```

**Example 4 — Combining variables in output**
```python
name = "Bob"
age = 30
print(name, "is", age, "years old")
```
Expected output:
```
Bob is 30 years old
```

## 5. Practice Problems

1. Create variables for your name, age, and height, then print all three.
2. Create two variables holding numbers and print their sum.
3. Create a variable `is_raining` set to `False` and print it along with its type.
4. Create a variable, print its type, then reassign it to a value of a
   *different* type and print the new type. (Notice Python allows this!)
5. Store the price of three items in three variables and print their total.

## 6. Challenge Problems

1. Without using addition operators directly on the variables, swap the
   values of two variables `a` and `b` using a third temporary variable.
   Print both before and after.
2. Create variables representing a rectangle's `width` and `height`, then
   compute and print its area and perimeter using only variables (no
   hard-coded numbers in the formulas).

## 7. Common Mistakes

- **Forgetting quotes for strings:** `name = Alice` → Python thinks `Alice`
  is a variable name, not text, and raises an error.
- **Using a number as the first character** of a variable name:
  `1name = "Alice"` → invalid.
- **Using spaces in variable names:** `my name = "Alice"` → invalid, use
  `my_name`.
- **Confusing `=` (assignment) with `==` (comparison)** — covered fully in
  `03-operators`, but keep in mind `=` *stores*, it doesn't *compare*.
- **Mixing types in math without meaning to,** e.g. trying to add a number
  and a string directly (`5 + "5"`) — Python will raise a `TypeError`.

## 8. Mini Quiz

1. What symbol is used to assign a value to a variable?
2. What data type would `3.14` be?
3. What data type would `"3.14"` be?
4. Is `True` a `str` or a `bool`?
5. Which of these is a valid variable name: `2total`, `total_2`, `total 2`?

*(Answers: 1. `=`  2. `float`  3. `str` (because of the quotes)  4. `bool`  5. `total_2`)*

## 9. Practical Exercise

Create a file `profile.py` that stores your name (`str`), age (`int`),
height in meters (`float`), and whether you're a student (`bool`) in four
variables. Print each variable together with its type using `type()`.

➡️ Matching files: [`exercises/01_variables_exercises.py`](../exercises/01_variables_exercises.py) ·
[`solutions/01_variables_solutions.py`](../solutions/01_variables_solutions.py)

**Previous:** [`00-getting-started`](../00-getting-started/README.md) | **Next:** [`02-input-output`](../02-input-output/README.md)
