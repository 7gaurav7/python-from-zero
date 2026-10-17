# 00 — Getting Started

## 1. Beginner-Friendly Explanation

A computer only understands very precise, low-level instructions. Writing
those instructions directly is painful for humans, so we use **programming
languages** — a way of writing instructions in a form that's readable by
people, which then gets translated into something the computer understands.

**Python** is one such language. It's known for reading almost like plain
English, which is why it's one of the best languages to learn first.

When you write Python code, you save it in a file ending in `.py`. Then you
run that file using a program called the **Python interpreter**, which reads
your instructions line by line and carries them out.

Think of it like a recipe: your `.py` file is the recipe, and the Python
interpreter is the chef who follows it exactly, step by step, in order.

## 2. Important Concepts

- **Program** — a sequence of instructions that tells a computer what to do.
- **Interpreter** — the program that reads and runs your Python code.
- **Script** — a file containing Python code (a `.py` file).
- **Source code** — the actual text you write (your instructions).
- **Syntax** — the grammar rules of a language. Get the syntax wrong and
  Python won't understand you (it will raise an error).
- **Comment** — a note in your code that Python ignores, meant for humans to
  read.
- **REPL** — "Read-Eval-Print Loop" — an interactive mode where you type one
  line of Python at a time and see the result immediately. You get this by
  typing `python` (or `python3`) with no filename in your terminal.

## 3. Syntax

Two ways to run Python:

**1. Interactive mode (REPL)** — good for quick experiments:
```
$ python3
>>> print("Hello")
Hello
>>> exit()
```

**2. Script mode** — write code in a file, then run the file:
```
$ python3 hello.py
```

Comments in Python start with `#`:
```python
# This is a comment. Python ignores this line entirely.
print("This line actually runs.")
```

## 4. Simple Examples

**Example 1 — Your first program**
```python
# hello.py
print("Hello, World!")
```
Expected output:
```
Hello, World!
```

**Example 2 — Multiple lines run in order, top to bottom**
```python
print("Line 1")
print("Line 2")
print("Line 3")
```
Expected output:
```
Line 1
Line 2
Line 3
```

**Example 3 — Comments don't affect the program**
```python
# Print a greeting
print("Good morning!")   # this comment is ignored too
```
Expected output:
```
Good morning!
```

**Example 4 — Python does math for you**
```python
print(2 + 3)
print(10 - 4)
```
Expected output:
```
5
6
```

## 5. Practice Problems

1. Write a program that prints your name.
2. Write a program that prints your name, age, and favorite hobby on three
   separate lines.
3. Write a program with a comment above each `print()` explaining what it does.
4. Write a program that prints the result of `7 * 6`.
5. Write a program that prints a small ASCII picture (e.g., a smiley face)
   using a single `print()` call.

## 6. Challenge Problems

1. Print a 5-line "banner" made of `*` characters that frames a message, e.g.:
   ```
   *****************
   * WELCOME PYTHON *
   *****************
   ```
   (You're allowed multiple `print()` calls — loops come later!)
2. Using only `print()` and arithmetic, print the result of converting
   100 degrees Fahrenheit to Celsius. (Formula: `(F - 32) * 5 / 9`.)

## 7. Common Mistakes

- **Forgetting quotes around text:** `print(Hello)` → error. Text (called a
  *string*) must be wrapped in quotes: `print("Hello")`.
- **Mismatched quotes:** `print("Hello')` → error. Opening and closing quotes
  must match (`"..."` or `'...'`, not mixed).
- **Wrong file extension:** saving as `hello.txt` instead of `hello.py` — the
  interpreter and your editor won't treat it as Python code.
- **Using `python` when your system needs `python3`** (common on macOS/Linux).
- **Indentation confusion:** Python cares about spaces at the start of a
  line (you'll see why starting in `04-conditions`) — don't add spaces before
  a line unless you mean to.

## 8. Mini Quiz

1. What file extension do Python files use?
2. What symbol starts a comment in Python?
3. What is the name of the program that runs your `.py` file?
4. True or False: Python code runs from top to bottom, in order.
5. What function do you use to display text on the screen?

*(Answers: 1. `.py`  2. `#`  3. The Python interpreter  4. True  5. `print()`)*

## 9. Practical Exercise

Create a file called `about_me.py` that prints at least 5 lines of
information about yourself (name, age, city, a hobby, and a goal for
learning Python), with a comment above each line explaining what it prints.
Run it and confirm the output looks correct.

➡️ Matching files: [`exercises/00_getting_started_exercises.py`](../exercises/00_getting_started_exercises.py) ·
[`solutions/00_getting_started_solutions.py`](../solutions/00_getting_started_solutions.py)

**Next up:** [`01-variables-and-data-types`](../01-variables-and-data-types/README.md)
