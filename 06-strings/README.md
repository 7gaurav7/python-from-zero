# 06 — Strings

## 1. Beginner-Friendly Explanation

A **string** (`str`) is text: a sequence of characters. You've already been
using strings since Topic 01. Now we'll go deeper: strings support
**indexing** (getting one character), **slicing** (getting a chunk), and a
large set of built-in **methods** for transforming text — a huge part of
real-world programming (cleaning user input, formatting reports, parsing
files, etc.).

## 2. Important Concepts

- **Indexing** — each character in a string has a position, starting at `0`.
  Negative indices count from the end (`-1` is the last character).
- **Slicing** — extracting a substring using `string[start:stop]`.
- **Immutability** — strings can't be changed in place; string methods
  always return a *new* string.
- **String methods** — built-in functions attached to strings, e.g.
  `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`.
- **String formatting** — f-strings (from Topic 02) are the recommended way
  to build strings with variables.
- **Concatenation** — joining strings with `+`.

## 3. Syntax

```python
s = "Hello, World"

s[0]              # first character
s[-1]             # last character
s[0:5]            # slice: characters at index 0 up to (not incl.) 5
s[:5]             # same as above, start defaults to 0
s[7:]             # from index 7 to the end
len(s)            # length of the string

s.upper()         # "HELLO, WORLD"
s.lower()         # "hello, world"
s.strip()         # removes leading/trailing whitespace
s.replace("a", "b")  # replaces all "a" with "b"
s.split(",")      # splits into a list by a separator
"-".join(["a", "b", "c"])  # "a-b-c"
s.startswith("Hello")   # True
s.endswith("World")     # True
str(value)        # convert value to a string
```

## 4. Simple Examples

**Example 1 — Indexing and slicing**
```python
word = "Python"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[3:])
```
Expected output:
```
P
n
Pyt
hon
```

**Example 2 — Common string methods**
```python
text = "  Hello, World  "
print(text.strip())
print(text.strip().upper())
print(text.strip().lower())
```
Expected output:
```
Hello, World
HELLO, WORLD
hello, world
```

**Example 3 — Splitting and joining**
```python
sentence = "Python is fun"
words = sentence.split(" ")
print(words)
print("-".join(words))
```
Expected output:
```
['Python', 'is', 'fun']
Python-is-fun
```

**Example 4 — Length and concatenation**
```python
first = "Ada"
last = "Lovelace"
full = first + " " + last
print(full)
print(len(full))
```
Expected output:
```
Ada Lovelace
12
```

## 5. Practice Problems

1. Given a string, print its first and last characters.
2. Given a full name string, split it into first and last name.
3. Take a sentence and count how many words it has (hint: `.split()` then
   `len()`).
4. Given a string, print it in reverse (hint: slicing with a step of `-1`:
   `s[::-1]`).
5. Given a messy user input like `"  JOHN@Email.com  "`, clean it up to
   `"john@email.com"` using `.strip()` and `.lower()`.

## 6. Challenge Problems

1. Write a program that checks whether a given string is a **palindrome**
   (reads the same forwards and backwards), ignoring case and spaces.
2. Write a program that takes a sentence and capitalizes the first letter of
   every word (without using `.title()` — build it manually with `.split()`,
   a loop, and `.join()`, then compare your result to `.title()`).

## 7. Common Mistakes

- **Trying to modify a string in place**, e.g. `word[0] = "J"` → error;
  strings are immutable. Build a new string instead.
- **Off-by-one slicing confusion** — `s[0:3]` gives 3 characters (indices
  0, 1, 2), not 4.
- **Forgetting that indexing starts at 0**, not 1.
- **Forgetting to reassign after a method call** — `text.strip()` doesn't
  change `text`; you need `text = text.strip()` to keep the result.
- **Comparing strings with different cases** and expecting equality:
  `"Hello" == "hello"` is `False`.

## 8. Mini Quiz

1. What index is the first character of a string?
2. What does `s[-1]` return?
3. Do string methods change the original string?
4. What does `"a,b,c".split(",")` return?
5. What does `"-".join(["x", "y"])` return?

*(Answers: 1. `0`  2. The last character  3. No — they return a new string  4. `['a', 'b', 'c']`  5. `"x-y"`)*

## 9. Practical Exercise

Create `text_analyzer.py` that asks the user for a sentence and prints: the
number of characters, the number of words, the sentence in uppercase, and
the sentence reversed.

➡️ Matching files: [`exercises/06_strings_exercises.py`](../exercises/06_strings_exercises.py) ·
[`solutions/06_strings_solutions.py`](../solutions/06_strings_solutions.py)

**Previous:** [`05-loops`](../05-loops/README.md) | **Next:** [`07-lists-tuples-sets`](../07-lists-tuples-sets/README.md)
