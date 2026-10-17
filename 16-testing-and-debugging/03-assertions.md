# Assertions

## Learning Objectives
By the end of this lesson you can:
- Use `assert` to check that a condition holds true at a specific point in
  your code
- Explain the difference between an assertion and a handled exception
  (`try`/`except`)
- Recognize when assertions are (and aren't) the right tool

## Concept Explanation

An **assertion** is a statement that says "I believe this is true at this
point in the program — if it isn't, something has gone seriously wrong,
and the program should stop immediately." It's a debugging and
sanity-checking tool, not a replacement for `try`/`except` (`11-exceptions`).

```python
def calculate_discount(price, percent):
    assert 0 <= percent <= 100, "percent must be between 0 and 100"
    return price * (1 - percent / 100)
```

If `percent` is out of range, the `assert` immediately raises an
`AssertionError` with your message — catching a bug at the exact point it
was introduced, rather than letting it silently produce a wrong answer
somewhere much later in the program.

**Assertions vs. exceptions:** use `try`/`except` for problems you
*expect could happen* and want to handle gracefully (bad user input, a
missing file). Use `assert` for conditions that should be **impossible**
if your code is correct — a way of documenting and checking your own
assumptions, mainly during development and testing.

## Syntax

```python
assert condition
assert condition, "error message shown if the condition is False"
```

If `condition` is `True`, nothing happens — execution continues normally.
If `condition` is `False`, Python raises `AssertionError` (with your
message, if you gave one).

## Examples

**Example 1 — A passing assertion (no visible effect)**
```python
def square(n):
    result = n ** 2
    assert result >= 0, "a square should never be negative"
    return result

print(square(5))
```
Expected output:
```
25
```

**Example 2 — A failing assertion**
```python
def get_first(items):
    assert len(items) > 0, "items must not be empty"
    return items[0]

print(get_first([]))
```
This raises:
```
Traceback (most recent call last):
  ...
AssertionError: items must not be empty
```

**Example 3 — Using assertions to check a function's own logic during
development**
```python
def average(numbers):
    result = sum(numbers) / len(numbers)
    assert isinstance(result, float), "average should always be a float"
    return result

print(average([1, 2, 3]))
```
Expected output:
```
2.0
```

**Example 4 — Assertions as lightweight tests (a preview of `unittest`)**
```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
print("All checks passed!")
```
Expected output:
```
All checks passed!
```

## Common Mistakes

- **Using `assert` to validate user input.** Assertions can be disabled
  entirely when Python is run with the `-O` (optimize) flag — never rely
  on `assert` for anything your program *must* check in production (like
  validating what a user typed). Use `if`/`raise` or `try`/`except`
  instead for that.
- **Writing an `assert` with no message** — `assert x > 0` fails with a
  bare `AssertionError` and no explanation; `assert x > 0, "x must be positive"`
  tells you (and future you) exactly what was expected.
- **Confusing an assertion failing with a "normal," expected error** — an
  `AssertionError` should mean "this should never happen if the code is
  correct," not "the user typed something odd."
- **Asserting something that isn't actually always true** — e.g. asserting
  a list is never empty when, in fact, an empty list is a valid input your
  code should handle; that's a case for `if`, not `assert`.

## Practice

1. Write a function `calculate_discount(price, percent)` with an `assert`
   checking that `percent` is between 0 and 100.
2. Write a function `get_middle_item(items)` with an `assert` checking the
   list has an odd number of items before returning the middle one.
3. Write three `assert` statements checking a `multiply(a, b)` function
   against known correct results, then print `"All checks passed!"` if none
   fail.
4. Explain in a comment: why would `assert` be a poor choice for checking
   whether a file the user provided actually exists?

## Challenge

Write a function `safe_divide(a, b)` that uses `assert` to document the
precondition that `b != 0` is expected never to happen from *your own*
code's usage — but also uses proper `try`/`except` around the actual
division in case it's called in a context where that assumption could be
violated. Explain in a comment why both are present.

## Mini Project

Add a handful of `assert`-based sanity checks to your
`19-projects` **Student Management System** solution's `average()` method
— e.g., asserting the returned average is never negative and never greater
than 100 (given valid grade inputs) — as a lightweight safety net while you
continue developing it.

## Summary

`assert condition, message` checks an assumption that should always be
true if your code is correct, raising `AssertionError` immediately if
it's violated. It's a development/debugging and lightweight-testing tool
— not a substitute for proper input validation or exception handling,
since assertions can be disabled entirely in optimized runs.

## Next Step

Continue to [`04-unittest-basics.md`](04-unittest-basics.md).
