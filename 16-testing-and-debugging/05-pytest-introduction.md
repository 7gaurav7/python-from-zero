# Introduction to pytest

## Learning Objectives
By the end of this lesson you can:
- Explain how `pytest` differs from `unittest` (and why it's popular)
- Install `pytest` and run a test file with it
- Write a plain-function `pytest` test using simple `assert` statements
- Use a `pytest` fixture for shared setup

## Concept Explanation

`pytest` is not part of the standard library — it's a third-party package
(installed with `pip`, see `18-real-world-python`) that has become the
most widely used Python testing tool in the real world. Its main appeal:
**you don't need a class, and you don't need special `assertX` methods —
plain `assert` statements work**, and `pytest` produces very readable
failure output automatically.

```python
# unittest version
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# pytest version -- no class needed
def test_add():
    assert add(2, 3) == 5
```

Every `unittest` test file (including all the ones in `19-projects`) can
actually also be run *with* `pytest` — `pytest` understands `unittest`
style tests too. But when writing new tests from scratch, most Python
developers today reach for plain `pytest`-style functions, as shown here.

## Syntax

```python
# Install (once, in your environment -- see 18-real-world-python):
#   pip install pytest

# test_example.py
def test_something():
    assert some_condition

def test_raises_error():
    import pytest
    with pytest.raises(SomeException):
        risky_code()

# A fixture: shared setup, reused across multiple test functions
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_uses_fixture(sample_data):
    assert sum(sample_data) == 6
```

Run all tests in a folder with:
```
pytest
```
or a specific file:
```
pytest test_example.py
```

## Examples

**Example 1 — A basic pytest test (no class needed)**
```python
def add(a, b):
    return a + b

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2
```
Running `pytest` on this file prints something like:
```
====================== test session starts =======================
collected 2 items

test_example.py ..                                            [100%]

======================= 2 passed in 0.01s =========================
```

**Example 2 — Testing that an exception is raised**
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

**Example 3 — A fixture for shared setup**
```python
import pytest

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

@pytest.fixture
def counter():
    return Counter()   # a fresh Counter is created for each test that uses it

def test_starts_at_zero(counter):
    assert counter.value == 0

def test_increment(counter):
    counter.increment()
    assert counter.value == 1
```

**Example 4 — pytest's readable failure output**

If `square(5)` incorrectly returned `10`:
```python
def square(n):
    return n + n  # bug: should be n * n

def test_square_of_five():
    assert square(5) == 25
```
`pytest` shows exactly where and why it failed:
```
    def test_square_of_five():
>       assert square(5) == 25
E       assert 10 == 25
E        +  where 10 = square(5)

test_example.py:4: AssertionError
```
Notice `pytest` shows the actual computed value (`10`) automatically,
without needing a custom `assertEqual` call — this is one of the biggest
reasons developers prefer it.

## Common Mistakes

- **Forgetting `pytest` needs installing** — unlike `unittest`, it isn't
  built in; you need `pip install pytest` in your environment first (see
  `18-real-world-python`).
- **Naming test files/functions incorrectly** — `pytest` automatically
  discovers files named `test_*.py` or `*_test.py`, and functions/methods
  named `test_*`; anything else won't be picked up.
- **Forgetting fixtures are passed in as parameters** — a test function
  that wants to use a fixture must name it as a parameter (as `counter` is
  in Example 3), not call it directly.
- **Mixing up when to use `pytest.raises` vs. `unittest`'s
  `assertRaises`** — they do the same job; use whichever matches the
  style of the rest of the file you're working in.

## Practice

1. Install `pytest` (`pip install pytest`) and write a `test_math.py` file
   with two plain `assert`-based test functions for a simple function of
   your choice.
2. Rewrite one of your `unittest` tests from the previous lesson as a
   plain `pytest`-style function.
3. Write a `pytest.raises` test for a function that should raise
   `ValueError` on invalid input.
4. Write a fixture that returns a list of sample data, and two test
   functions that use it.

## Challenge

Pick any project's `tests/test_*.py` file in `19-projects` (written in
`unittest` style) and rewrite its tests as plain `pytest`-style functions.
Run both versions with `pytest` and confirm they produce equivalent
results.

## Mini Project

Add a `tests/` folder with `pytest`-style tests (instead of `unittest`) for
a new function you write yourself — for example, a `word_frequency(text)`
function that returns a dictionary of word counts (reusing ideas from
`08-dictionaries` and `06-strings`).

## Summary

`pytest` is a third-party testing tool that lets you write tests as plain
functions with ordinary `assert` statements, and produces detailed,
readable failure output automatically. It also understands `unittest`
style tests, so you can run everything in `19-projects/*/tests/` with
`pytest` today, and choose whichever style you prefer for your own new
tests going forward.

## Next Step

You've completed `16-testing-and-debugging`. Continue to
[`17-git-and-github`](../17-git-and-github/README.md).
