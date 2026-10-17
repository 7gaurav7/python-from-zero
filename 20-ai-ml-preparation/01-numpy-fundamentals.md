# NumPy Fundamentals

## Learning Objectives
By the end of this lesson you can:
- Explain why NumPy arrays are faster and more convenient than plain lists
  for numerical work
- Create NumPy arrays and inspect their shape and type
- Perform element-wise arithmetic on whole arrays at once (no loops)
- Use basic indexing, slicing, and simple statistics functions

## Concept Explanation

**NumPy** ("Numerical Python") is the foundational library for numerical
computing in Python — nearly every data science and ML library (including
pandas, in the next lesson) is built on top of it. Its core object is the
**array** (`ndarray`): a grid of numbers, all of the same type, that
supports fast, whole-array operations.

Compare the list-based approach you already know:
```python
numbers = [1, 2, 3, 4]
doubled = [n * 2 for n in numbers]   # a comprehension loop, from 14-intermediate-python
```
to the NumPy way:
```python
import numpy as np
numbers = np.array([1, 2, 3, 4])
doubled = numbers * 2                 # the whole array is doubled at once, no loop
```

This isn't just shorter — for large amounts of data, it's dramatically
faster, because NumPy performs the operation in optimized, compiled code
rather than looping in plain Python.

## Syntax

```python
import numpy as np                 # "np" is the near-universal convention

np.array([1, 2, 3])                 # create a 1D array from a list
np.array([[1, 2], [3, 4]])          # create a 2D array from a list of lists
np.zeros(5)                          # array of 5 zeros
np.arange(0, 10, 2)                  # like range(), but returns an array

arr.shape                            # dimensions, e.g. (4,) or (2, 3)
arr.dtype                             # the data type of its elements

arr * 2, arr + 1, arr ** 2           # element-wise arithmetic (no loop needed)
arr[0], arr[1:3]                      # indexing and slicing, just like a list
arr[arr > 2]                          # boolean filtering ("give me elements > 2")

arr.sum(), arr.mean(), arr.max(), arr.min()   # quick statistics
```

## Examples

**Example 1 — Creating an array and inspecting it**
```python
import numpy as np

numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.shape)
print(numbers.dtype)
```
Expected output:
```
[10 20 30 40]
(4,)
int64
```
(On some systems `dtype` may print as `int32` instead of `int64` — this
depends on the operating system, not on your code.)

**Example 2 — Element-wise arithmetic (no loop needed)**
```python
import numpy as np

numbers = np.array([1, 2, 3, 4])
print(numbers * 2)
print(numbers + 10)
print(numbers ** 2)
```
Expected output:
```
[2 4 6 8]
[11 12 13 14]
[ 1  4  9 16]
```

**Example 3 — Indexing, slicing, and boolean filtering**
```python
import numpy as np

scores = np.array([55, 90, 72, 88, 40])
print(scores[1])
print(scores[1:3])
print(scores[scores >= 70])
```
Expected output:
```
90
[90 72]
[90 72 88]
```

**Example 4 — Quick statistics**
```python
import numpy as np

scores = np.array([55, 90, 72, 88, 40])
print(scores.sum())
print(scores.mean())
print(scores.max())
print(scores.min())
```
Expected output:
```
345
69.0
90
40
```

## Common Mistakes

- **Mixing types in an array unintentionally** — a NumPy array holds one
  data type for *all* its elements; `np.array([1, 2, "3"])` silently
  converts everything to strings, which is rarely what you want.
- **Forgetting arrays support whole-array operations directly** — writing
  a `for` loop over a NumPy array to do arithmetic works, but throws away
  the speed and conciseness that's the entire point of using NumPy.
- **Confusing a NumPy array with a Python list** — they look similar when
  printed, but support different operations; `[1, 2] + [3, 4]` on plain
  lists *concatenates* them (`[1, 2, 3, 4]`), while
  `np.array([1, 2]) + np.array([3, 4])` *adds element-wise* (`[4, 6]`).
- **Not checking `.shape`** before an operation that assumes a particular
  dimensionality — a very common source of confusing errors once arrays
  become 2D or larger.

## Practice

1. Create a NumPy array of the numbers 1 through 10 using `np.arange()`,
   and print its `.sum()` and `.mean()`.
2. Given an array of temperatures in Celsius, convert the whole array to
   Fahrenheit in one line (no loop).
3. Given an array of exam scores, use boolean filtering to get only the
   scores that are failing (below 60).
4. Create a 2D array (a list of lists) and print its `.shape`.

## Challenge

Given two same-length NumPy arrays representing hours worked and hourly
rate, compute the total pay for each person (element-wise multiplication)
and then the grand total across everyone (`.sum()`), all without writing a
single explicit loop.

## Mini Project

Rewrite the `15-working-with-data` sales-total example
(`sales.csv`, from `05-basic-data-processing`) using a NumPy array for the
`amount` column instead of a Python list + `sum()`, and compare the
result.

## Summary

NumPy arrays are the foundation of numerical computing in Python: created
with `np.array()`, they support fast, whole-array arithmetic, slicing,
boolean filtering, and built-in statistics — all without explicit loops.
Nearly every library you'll meet in AI/ML builds directly on NumPy arrays.

## Next Step

Continue to [`02-pandas-fundamentals.md`](02-pandas-fundamentals.md).
