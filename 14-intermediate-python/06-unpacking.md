# Unpacking

## Learning Objectives
- Assign multiple variables from a list/tuple in one line
- Use `*` to capture "the rest" of a sequence while unpacking
- Swap variables and unpack function return values idiomatically

## Concept Explanation
**Unpacking** assigns a sequence's items to multiple variables by
position:
```python
point = (3, 4)
x, y = point
```
You've used this already -- `for name, score in zip(...)` and the
variable-swap challenge in `01-variables-and-data-types`. This lesson
makes the pattern explicit.

## Syntax
```python
a, b = (1, 2)
a, b = b, a                    # swap, no temp variable
first, *rest = [1, 2, 3, 4]     # first=1, rest=[2, 3, 4]
*rest, last = [1, 2, 3, 4]      # rest=[1, 2, 3], last=4
first, *middle, last = [1, 2, 3, 4, 5]

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5])
```

## Examples

**Example 1 - Basic unpacking**
```python
point = (3, 4)
x, y = point
print(x, y)
```
Expected output: `3 4`

**Example 2 - Swapping without a temp variable**
```python
a, b = 1, 2
a, b = b, a
print(a, b)
```
Expected output: `2 1`

**Example 3 - `*` to capture the rest**
```python
scores = [100, 90, 85, 70, 60]
highest, *others = scores
print(highest)
print(others)
```
Expected output:
```
100
[90, 85, 70, 60]
```

**Example 4 - Unpacking a function's multiple return values**
```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([4, 8, 15, 16, 23, 42])
print(lowest, highest)
```
Expected output: `4 42`

## Common Mistakes
- Mismatched counts: `a, b = [1, 2, 3]` raises `ValueError`.
- Using more than one `*name` target in a single unpacking (only one allowed).
- Forgetting `*rest` is always a list, even if empty.

## Practice
1. Unpack `(name, age, city)` into three variables and print them.
2. Rotate three variables `a, b, c` so `a` gets `b`, `b` gets `c`, `c` gets `a`.
3. Unpack the first item, last item, and "the rest" of a list using `*`.
4. Write a function returning three values and unpack all three.

## Challenge
Given a list of `(name, score)` tuples, unpack each directly in a `for`
loop to print a formatted leaderboard.

## Mini Project
In the `19-projects` Student Management System, use unpacking to extract
`low, high` from a helper returning a student's lowest/highest grade.

## Summary
Unpacking assigns a sequence's elements to multiple variables by position
in one statement, including the swap idiom and `*` for capturing a
variable-length remainder. Used constantly with `zip()`, `enumerate()`,
and multi-value returns.

## Next Step
Continue to [`07-iterators.md`](07-iterators.md).
