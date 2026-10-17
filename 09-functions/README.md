# 09 — Functions

## 1. Beginner-Friendly Explanation

A **function** is a named, reusable block of code that performs a specific
task. You've already been using functions (`print()`, `len()`, `input()`)
— now you'll learn to write your own.

Functions let you avoid repeating yourself: write the logic once, then
**call** it as many times as you need, optionally with different inputs.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```

## 2. Important Concepts

- **Function definition** — `def function_name(parameters):` followed by an
  indented block.
- **Parameters** — variables listed in the function definition; they're
  placeholders for the values the function will receive.
- **Arguments** — the actual values you pass in when *calling* the function.
- **Return value** — the result a function sends back using `return`. A
  function without `return` implicitly returns `None`.
- **Default parameter values** — `def greet(name="friend"):` lets you call
  `greet()` without an argument.
- **Scope** — variables created inside a function only exist inside that
  function (**local scope**), unless declared otherwise.
- **Calling a function** — using its name followed by parentheses:
  `greet("Alice")`.

## 3. Syntax

```python
def function_name(parameter1, parameter2):
    # function body
    result = parameter1 + parameter2
    return result

# Calling it
output = function_name(3, 4)

# Default parameters
def greet(name="friend"):
    print(f"Hello, {name}!")

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5])
```

## 4. Simple Examples

**Example 1 — A simple function**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```
Expected output:
```
Hello, Alice!
Hello, Bob!
```

**Example 2 — Returning a value**
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```
Expected output:
```
7
```

**Example 3 — Default parameters**
```python
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()
greet("Charlie")
```
Expected output:
```
Hello, friend!
Hello, Charlie!
```

**Example 4 — Scope**
```python
def set_score():
    score = 100    # local variable, only exists inside this function
    print("Inside function:", score)

set_score()
# print(score)   # this would raise: NameError: name 'score' is not defined
```
Expected output:
```
Inside function: 100
```

## 5. Practice Problems

1. Write a function `square(n)` that returns `n` squared, then print the
   result for a few different numbers.
2. Write a function `is_even(n)` that returns `True` or `False`.
3. Write a function `greet(name, greeting="Hello")` that prints a
   customizable greeting, and call it both with and without the second
   argument.
4. Write a function `average(numbers)` that takes a list and returns the
   average.
5. Write a function `celsius_to_fahrenheit(c)` that returns the converted
   temperature.

## 6. Challenge Problems

1. Write a function `is_prime(n)` that returns `True` if `n` is a prime
   number, `False` otherwise.
2. Write a function `find_duplicates(items)` that takes a list and returns
   a list of values that appear more than once (no duplicates in the
   result itself).

## 7. Common Mistakes

- **Forgetting `return`** — a function that only `print()`s doesn't give you
  a usable value back; `result = my_function()` would be `None`.
- **Confusing parameters and arguments** — parameters are the names in the
  `def` line; arguments are the actual values passed when calling.
- **Trying to use a local variable outside its function** — causes a
  `NameError`.
- **Forgetting parentheses when calling** — `greet` refers to the function
  itself, `greet()` actually calls it.
- **Mutable default arguments** (an intermediate pitfall) — avoid
  `def f(items=[]):`; use `def f(items=None): items = items or []` instead.

## 8. Mini Quiz

1. What keyword defines a function?
2. What's the difference between a parameter and an argument?
3. What does a function return if it has no `return` statement?
4. Can a variable defined inside a function be used outside it?
5. What does `def greet(name="friend"):` allow you to do?

*(Answers: 1. `def`  2. Parameters are placeholders in the definition; arguments are the actual values passed in  3. `None`  4. No, it's local to the function  5. Call the function without providing a `name` argument)*

## 9. Practical Exercise

Create `temperature_tools.py` with two functions: `celsius_to_fahrenheit(c)`
and `fahrenheit_to_celsius(f)`. Ask the user which conversion they want and
a value, then call the right function and print the result.

➡️ Matching files: [`exercises/09_functions_exercises.py`](../exercises/09_functions_exercises.py) ·
[`solutions/09_functions_solutions.py`](../solutions/09_functions_solutions.py)

**Previous:** [`08-dictionaries`](../08-dictionaries/README.md) | **Next:** [`10-file-handling`](../10-file-handling/README.md)
