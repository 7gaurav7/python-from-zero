# 11 — Exceptions

## 1. Beginner-Friendly Explanation

When something goes wrong while a program runs — dividing by zero, opening
a missing file, converting invalid text to a number — Python raises an
**exception** (an error) and, by default, crashes the program.

Instead of letting your program crash ungracefully, you can **catch**
exceptions using `try`/`except` and respond sensibly — show a friendly
message, ask the user to try again, or use a fallback value.

## 2. Important Concepts

- **Exception** — an error that occurs during program execution.
- **`try` block** — code that might raise an exception.
- **`except` block** — code that runs if a specific exception occurs.
- **Catching specific exceptions** — always prefer `except ValueError:` over
  a bare `except:`, so you don't accidentally hide unrelated bugs.
- **`else` (with try)** — runs only if the `try` block succeeded (no
  exception).
- **`finally`** — runs no matter what (success or failure) — good for
  cleanup code.
- **Common built-in exceptions:**
  - `ValueError` — invalid value, e.g. `int("abc")`
  - `ZeroDivisionError` — dividing by zero
  - `FileNotFoundError` — file doesn't exist
  - `TypeError` — wrong type used in an operation
  - `KeyError` — missing dictionary key
  - `IndexError` — list index out of range

## 3. Syntax

```python
try:
    risky_code()
except SpecificError:
    handle_it()
except AnotherError as e:
    print("Something went wrong:", e)
else:
    print("This runs only if no exception occurred")
finally:
    print("This always runs")
```

## 4. Simple Examples

**Example 1 — Catching a `ValueError`**
```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("That's not a valid number!")
```
Sample run (user types `abc`):
```
Enter your age: abc
That's not a valid number!
```

**Example 2 — Catching a `ZeroDivisionError`**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```
Expected output:
```
You can't divide by zero!
```

**Example 3 — Multiple except blocks**
```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("That index doesn't exist.")
except ValueError:
    print("Invalid value.")
```
Expected output:
```
That index doesn't exist.
```

**Example 4 — `else` and `finally`**
```python
try:
    number = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion succeeded:", number)
finally:
    print("Done trying.")
```
Expected output:
```
Conversion succeeded: 42
Done trying.
```

## 5. Practice Problems

1. Write a program that asks the user for a number and safely handles the
   case where they type something that isn't a number.
2. Write a program that safely divides two user-provided numbers, handling
   both `ValueError` and `ZeroDivisionError`.
3. Write a program that tries to open a file that may not exist, printing
   a friendly message if it's missing (`FileNotFoundError`).
4. Write a program that accesses a dictionary key that might not exist,
   handling the `KeyError`.
5. Write a loop that keeps asking the user for a number until they provide
   a valid one (combine `try`/`except` with `while True` and `break`).

## 6. Challenge Problems

1. Write a simple calculator function that takes two numbers and an
   operator (`+ - * /`) and handles every error that could reasonably
   occur (bad operator, division by zero, non-numeric input).
2. Write a function that reads a list of strings meant to be numbers,
   converts each to an `int`, and returns a list of only the ones that
   converted successfully, silently skipping (or logging) the ones that
   failed.

## 7. Common Mistakes

- **Using a bare `except:`** — this catches *everything*, including typos
  in your own code, making bugs hard to find. Always name the exception
  type when you can.
- **Catching an exception and doing nothing (silently swallowing errors)**
  — at minimum, print something so you know it happened.
- **Putting too much code inside `try`** — only wrap the specific line(s)
  that might fail, so you know exactly what triggered the exception.
- **Forgetting that `finally` always runs**, even after a `return` inside
  `try` — useful for cleanup, but can surprise you if not expected.

## 8. Mini Quiz

1. What block do you put "risky" code in?
2. What's wrong with `except:` (no exception type)?
3. What exception is raised by `int("abc")`?
4. What exception is raised by dividing by zero?
5. Does `finally` run even if an exception occurred?

*(Answers: 1. `try`  2. It catches everything, hiding unrelated bugs  3. `ValueError`  4. `ZeroDivisionError`  5. Yes, always)*

## 9. Practical Exercise

Create `safe_calculator.py` that repeatedly asks the user for two numbers
and an operator, performs the calculation, and handles all realistic
errors gracefully (invalid numbers, division by zero, unknown operator),
letting the user try again instead of crashing.

➡️ Matching files: [`exercises/11_exceptions_exercises.py`](../exercises/11_exceptions_exercises.py) ·
[`solutions/11_exceptions_solutions.py`](../solutions/11_exceptions_solutions.py)

**Previous:** [`10-file-handling`](../10-file-handling/README.md) | **Next:** [`12-modules-and-packages`](../12-modules-and-packages/README.md)
