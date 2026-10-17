# Comprehensions

## Learning Objectives
- Rewrite a "build a new list from a loop" pattern as a list comprehension
- Filter items with a comprehension's `if` clause
- Build dictionary and set comprehensions
- Recognize when a comprehension helps readability -- and when a plain
  loop is clearer

## Concept Explanation
You've written this pattern many times since `05-loops`:
```python
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
```
A **comprehension** builds the same list in one line:
```python
squares = [n ** 2 for n in range(1, 6)]
```
Read it as: "give me `n ** 2`, for each `n` in `range(1, 6)`."
Comprehensions exist for lists (`[]`), dicts (`{k: v}`), and sets (`{}`).

## Syntax
```python
[expression for item in iterable]
[expression for item in iterable if condition]
{key_expr: value_expr for item in iterable}
{expression for item in iterable}
```

## Examples

**Example 1 - Basic list comprehension**
```python
squares = [n ** 2 for n in range(1, 6)]
print(squares)
```
Expected output: `[1, 4, 9, 16, 25]`

**Example 2 - Filtering with `if`**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```
Expected output: `[2, 4, 6, 8, 10]`

**Example 3 - Dictionary comprehension**
```python
names = ["Alice", "Bob", "Carla"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)
```
Expected output: `{'Alice': 5, 'Bob': 3, 'Carla': 5}`

**Example 4 - Set comprehension**
```python
words = ["Hi", "hi", "HELLO", "hello"]
unique_lower = {word.lower() for word in words}
print(unique_lower)
```
Expected output: `{'hi', 'hello'}`

## Common Mistakes
- Cramming too much logic into one comprehension -- more than one `if` or
  a nested loop is often harder to read than a plain `for` loop.
- Forgetting comprehensions build a *new* collection, not modify in place.
- Confusing `{}` set vs dict comprehensions (colon = dict, no colon = set).
- Using a comprehension purely for side effects like `print()` -- use a
  regular loop instead.

## Practice
1. Build a list of cubes (`n ** 3`) for `n` from 1 to 10.
2. Given a list of words, keep only words longer than 4 characters.
3. Convert a list of Celsius temperatures to Fahrenheit.
4. Build a dictionary mapping 1-5 to their squares.
5. Given a sentence, build a set of its unique lowercase words.

## Challenge
Given a list of strings, build a dict mapping each to `True`/`False` for
whether it's a palindrome, using one dictionary comprehension.

## Mini Project
In the `19-projects` Quiz Game, use a list comprehension to collect only
the questions the player got wrong, and print them as a review list.

## Summary
Comprehensions build a new list/dict/set in one readable expression
instead of a multi-line loop with `.append()`. Use them for straightforward
transform/filter operations; use a plain loop once logic gets complex.

## Next Step
Continue to [`02-lambda-functions.md`](02-lambda-functions.md).
