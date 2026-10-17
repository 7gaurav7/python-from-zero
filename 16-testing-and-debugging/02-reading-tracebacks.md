# Reading Tracebacks

## Learning Objectives
By the end of this lesson you can:
- Read a Python traceback from bottom to top with confidence
- Identify the error type, the error message, and the exact line that
  failed
- Trace a multi-level traceback back through several function calls to
  find the original cause

## Concept Explanation

When an unhandled exception occurs, Python prints a **traceback** — a
report showing exactly what was happening when the program crashed. It
looks intimidating at first, but it's built the same way every time, and
reading it correctly is one of the highest-leverage beginner skills.

```
Traceback (most recent call last):
  File "shop.py", line 12, in <module>
    print(calculate_total(cart))
  File "shop.py", line 7, in calculate_total
    return price * quantity
TypeError: can't multiply sequence by non-int of type 'float'
```

Read it in this order:
1. **The last line** — the error type and message: what went wrong.
   `TypeError: can't multiply sequence by non-int of type 'float'`
2. **The frame right above it** — where exactly it happened:
   `File "shop.py", line 7, in calculate_total` — line 7, inside the
   function `calculate_total`.
3. **Each frame above that**, reading upward, shows the chain of calls
   that led there: `calculate_total` was called from line 12, at the
   top/`<module>` level of `shop.py`.

For a multi-level traceback (several functions calling each other), the
**bottommost frame is where the error actually occurred**; the frames
above it show the path of calls that got you there — useful when the bug's
root cause is a few calls away from the crash site.

## Syntax

There's no new Python syntax here — this lesson is about *reading* output
Python already produces whenever an exception isn't caught. See
`11-exceptions` for `try`/`except`, which is how you'd handle an exception
instead of letting it crash the program.

## Examples

**Example 1 — A simple one-level traceback**
```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```
This raises:
```
Traceback (most recent call last):
  File "example.py", line 4, in <module>
    print(divide(10, 0))
  File "example.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```
Reading bottom-up: `ZeroDivisionError: division by zero` happened on line
2, inside `divide`, which was called from line 4.

**Example 2 — A traceback through multiple function calls**
```python
def get_first_item(items):
    return items[0]

def process(data):
    return get_first_item(data)

print(process([]))
```
This raises:
```
Traceback (most recent call last):
  File "example.py", line 6, in <module>
    print(process([]))
  File "example.py", line 4, in process
    return get_first_item(data)
  File "example.py", line 2, in get_first_item
    return items[0]
IndexError: list index out of range
```
The actual failure (`items[0]` on an empty list) is in `get_first_item`,
called by `process`, called from the top level — three frames, read from
bottom (where it broke) to top (how we got there).

**Example 3 — A `KeyError` traceback**
```python
student = {"name": "Alice"}
print(student["age"])
```
This raises:
```
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    print(student["age"])
KeyError: 'age'
```
`KeyError: 'age'` tells you exactly which key was missing — no guessing
needed.

**Example 4 — Using the traceback to decide the fix**
```python
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([]))
```
This raises `ZeroDivisionError: division by zero` on the `return` line —
telling you directly that `average()` needs to handle an empty list before
dividing, e.g.:
```python
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

## Common Mistakes

- **Reading a traceback top-to-bottom** and getting lost in the frames —
  always find the error type/message at the very bottom first, then work
  upward only as far as you need to understand the *path* to the bug.
- **Panicking at a long traceback** — a traceback that spans many frames
  (common when using libraries) is not necessarily a "worse" bug; the
  bottom line and the frame directly above it are still where to start.
- **Ignoring the file and line number** — they tell you exactly where to
  look; don't guess when the traceback already points at the spot.
- **Assuming the error is always in *your* code** — sometimes a traceback
  ends inside a library file; when that happens, look at the frame just
  above it, in your own code, to see what you passed in that caused it.

## Practice

1. Deliberately write code that raises a `TypeError` (e.g. adding a string
   and a number), run it, and identify the error type, message, file, and
   line from the traceback.
2. Write a 3-function call chain (function A calls B calls C) where C
   raises an error, and practice tracing the full path through the
   traceback.
3. Take one of the Common Mistakes error types from
   [`resources/debugging-tips.md`](../resources/debugging-tips.md) and
   deliberately trigger it, then read the resulting traceback.

## Challenge

Write a function that reads a file and processes its lines assuming
they're all numbers. Run it on a file containing at least one non-numeric
line, and use the resulting traceback to precisely identify (in a comment)
which line and value caused the failure.

## Mini Project

No dedicated mini project — this lesson feeds directly into
`03-assertions` and `04-unittest-basics`, where you'll write code that
proactively catches these kinds of problems.

## Summary

A traceback tells you the error type and message (bottom line), where it
happened (the frame above), and the chain of calls that led there (each
frame above that). Reading bottom-to-top, rather than top-to-bottom, is
the key habit — it gets you to the useful information immediately.

## Next Step

Continue to [`03-assertions.md`](03-assertions.md).
