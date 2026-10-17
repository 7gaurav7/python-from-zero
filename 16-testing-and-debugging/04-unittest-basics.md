# unittest Basics

## Learning Objectives
By the end of this lesson you can:
- Explain why automated tests are more reliable than manually re-checking
  output
- Write a test class using Python's built-in `unittest` module
- Use common assertion methods (`assertEqual`, `assertTrue`,
  `assertRaises`, and more)
- Run a test file and read its output

## Concept Explanation

Every time you've manually run a script and looked at whether the output
"looked right," you were informally testing it. The problem: manual
checking doesn't scale — you won't re-verify every function by hand every
time you change one line elsewhere. **Automated tests** are code that
checks your code, so you can re-run every check in seconds, as often as
you like.

`unittest` is Python's built-in testing framework. You've actually already
seen it in action — every project under `19-projects` has a
`tests/test_*.py` file written with exactly this module. This lesson
explains how those work, from the ground up.

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

## Syntax

```python
import unittest

class TestSomething(unittest.TestCase):
    def test_case_name(self):          # method name MUST start with "test"
        self.assertEqual(actual, expected)
        self.assertTrue(condition)
        self.assertFalse(condition)
        self.assertIsNone(value)
        self.assertIn(item, collection)
        with self.assertRaises(SomeException):
            risky_code()

    def setUp(self):
        # runs automatically before EVERY test method in this class
        ...

if __name__ == "__main__":
    unittest.main()
```

Run a test file with:
```
python -m unittest test_filename.py
```
or, as you've seen throughout `19-projects`:
```
python -m unittest tests.test_something
```

## Examples

**Example 1 — A basic test class**
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
```
Running this prints something like:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
(each `.` represents one passing test)

**Example 2 — `setUp()` for shared test data**
```python
import unittest

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()   # fresh Counter before every test

    def test_starts_at_zero(self):
        self.assertEqual(self.counter.value, 0)

    def test_increment(self):
        self.counter.increment()
        self.assertEqual(self.counter.value, 1)

if __name__ == "__main__":
    unittest.main()
```

**Example 3 — Testing that an exception is raised**
```python
import unittest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class TestDivide(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

**Example 4 — A failing test's output**
```python
import unittest

def square(n):
    return n * n  # imagine this had a bug: `return n + n`

class TestSquare(unittest.TestCase):
    def test_square_of_five(self):
        self.assertEqual(square(5), 25)

if __name__ == "__main__":
    unittest.main()
```
If `square()` had the bug shown in the comment, running this would print:
```
F
======================================================================
FAIL: test_square_of_five (__main__.TestSquare.test_square_of_five)
----------------------------------------------------------------------
AssertionError: 10 != 25

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```
This is exactly the kind of output you'd read using the
`02-reading-tracebacks` skills — `10 != 25` tells you immediately what
the function actually returned versus what was expected.

## Common Mistakes

- **Forgetting test methods must start with `test`** — `unittest`
  discovers tests by name; a method called `check_addition` will silently
  never run.
- **Testing implementation details instead of behavior** — test *what a
  function returns/does* for given inputs, not *how* it does it
  internally; that keeps tests useful even after you refactor.
- **One giant test method covering many unrelated cases** — prefer many
  small, clearly-named test methods (`test_empty_list`,
  `test_single_item`, `test_negative_numbers`) over one that tries to
  check everything at once; when one fails, you'll know exactly what
  broke.
- **Not running tests after every change** — the entire value of
  automated tests comes from running them often, not writing them once
  and forgetting about them.

## Practice

1. Write a `unittest` test class for a `is_even(n)` function, covering an
   even number, an odd number, and zero.
2. Write a test class with a `setUp()` method for a simple `Stack` class
   (with `push()`/`pop()`), testing that it starts empty and that pushing
   then popping returns the right value.
3. Write a test using `assertRaises` for a function that should raise
   `ValueError` on invalid input.
4. Open [`19-projects/beginner-projects/02-simple-calculator/tests/test_calculator.py`](../19-projects/beginner-projects/02-simple-calculator/tests/test_calculator.py)
   and identify, in a comment, what each test method is checking.

## Challenge

Write a full `unittest` test class (at least 5 test methods) for the
`Student` class from `13-oop`'s practical exercise, covering `average()`
with multiple grades, `average()` with no grades, and `letter_grade()` at
several boundary values (89 vs. 90, for example).

## Mini Project

Pick any project in `19-projects` whose tests you haven't looked at
closely yet, read its `tests/` folder, then add **one new test case** of
your own that isn't already covered (an edge case you think of yourself).

## Summary

`unittest` is Python's built-in framework for writing automated tests:
subclass `unittest.TestCase`, write methods starting with `test`, and use
`self.assertEqual()`/`assertTrue()`/`assertRaises()` (and similar) to
check expected behavior. Every project in `19-projects` includes real
`unittest` test suites you can study as working examples.

## Next Step

Continue to [`05-pytest-introduction.md`](05-pytest-introduction.md).
