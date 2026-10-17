# Debugging Fundamentals

## Learning Objectives
By the end of this lesson you can:
- Describe a repeatable process for finding and fixing a bug
- Use `print()` statements strategically to inspect program state
- Isolate a bug by narrowing down which part of the code causes it
- Use Python's built-in debugger, `pdb`, for a closer look when needed

## Concept Explanation

A **bug** is any behavior your program has that you didn't intend. Every
programmer encounters them constantly — debugging is a normal, expected
part of writing code, not a sign something went wrong with *you*.

> For a full reference table of common error types and what causes each
> one, see [`resources/debugging-tips.md`](../resources/debugging-tips.md)
> — this lesson focuses on the *process*, not the catalog of error types.

A reliable debugging process:

1. **Reproduce it.** Find the smallest, most reliable way to trigger the
   bug. A bug you can't consistently reproduce is very hard to fix.
2. **Read the error message fully** (see the next lesson,
   `02-reading-tracebacks`, for how).
3. **Form a hypothesis.** Based on the error and the code, guess *where*
   and *why* it's happening.
4. **Inspect state with `print()`.** Print the values of variables right
   before the failure to check whether your hypothesis is correct.
5. **Narrow the search.** Comment out or isolate sections of code until
   you find the exact line responsible.
6. **Fix the root cause, not the symptom.** Avoid patches that hide an
   error without addressing why it happened.
7. **Verify the fix**, ideally by re-running a test (topics 4 and 5 in
   this section) rather than just eyeballing the output once.

## Syntax

```python
print("DEBUG:", variable_name)     # the simplest, most-used debugging tool

import pdb
pdb.set_trace()    # pauses execution here; drops you into an interactive
                     # debugger where you can inspect variables live
```

Inside `pdb`, common commands: `n` (next line), `s` (step into a function
call), `c` (continue running), `p variable_name` (print a variable),
`q` (quit).

## Examples

**Example 1 — Using `print()` to inspect state**
```python
def calculate_discount(price, percent):
    print("DEBUG: price =", price, "percent =", percent)
    discount = price * percent / 100
    print("DEBUG: discount =", discount)
    return price - discount

print(calculate_discount(100, 20))
```
Expected output:
```
DEBUG: price = 100 percent = 20
DEBUG: discount = 20.0
80.0
```

**Example 2 — Narrowing down a bug by isolating code**
```python
def buggy_average(numbers):
    total = 0
    for n in numbers:
        total = n          # BUG: should be total += n
    return total / len(numbers)

# Isolate: print total after the loop, before dividing, to see it's wrong
numbers = [10, 20, 30]
total = 0
for n in numbers:
    total = n
print("total after loop:", total)   # reveals total is 30, not 60 -- found it!
```
Expected output:
```
total after loop: 30
```

**Example 3 — The fixed version**
```python
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(average([10, 20, 30]))
```
Expected output:
```
20.0
```

**Example 4 — Using `pdb` to pause and inspect**
```python
import pdb

def mystery_function(x):
    y = x * 2
    pdb.set_trace()   # execution pauses here when you run this script
    z = y + 10
    return z

# When you run this normally (not inside this course's automated checks),
# you'd get an interactive (Pdb) prompt where you could type "p y" to see
# y's value, then "c" to continue.
```

## Common Mistakes

- **Guessing randomly instead of forming a hypothesis** — changing code
  without a clear theory of what's wrong wastes time and can introduce new
  bugs.
- **Removing `print()` debug statements... and forgetting one** — leaving
  stray debug output in "finished" code is a common and easily avoidable
  mistake; search for `"DEBUG:"` before considering a fix complete.
  before calling a fix "done".
- **Fixing the first error and assuming everything is fine** — sometimes
  one bug hides another; re-run and re-check after every fix.
- **Not testing the actual failing case after a fix** — always re-run
  whatever originally exposed the bug, not just a "looks fine" glance at
  the code.

## Practice

1. Take a function with a deliberate bug (write one yourself, e.g. an
   off-by-one loop) and use `print()` statements to locate the exact line
   responsible.
2. Add `import pdb; pdb.set_trace()` to a small script, run it, and
   practice `n`, `p variable_name`, and `c`.
3. Write a small function with two potential problems, and practice
   commenting out sections to isolate which one is triggering an error.

## Challenge

Take one of your own `19-projects` solutions, temporarily introduce a bug
on purpose, and write down (in a comment) the exact reasoning process you'd
use to find it without knowing where you put it — then verify by actually
finding it.

## Mini Project

No dedicated mini project here — reading tracebacks (next lesson) and
writing automated tests (lessons 4–5) are the natural, more concrete
follow-ups to this lesson's process.

## Summary

Debugging is a repeatable process: reproduce the bug, read the error
carefully, form a hypothesis, inspect state (usually with `print()`),
narrow down the exact cause, and fix the root cause — then verify. `pdb`
offers a more powerful, interactive way to inspect a program's state when
`print()` alone isn't enough.

## Next Step

Continue to [`02-reading-tracebacks.md`](02-reading-tracebacks.md).
