# map() and filter()

## Learning Objectives
- Use `map()` to apply a function to every item in an iterable
- Use `filter()` to keep only items matching a condition
- Convert `map()`/`filter()` results to a list
- Choose between `map()`/`filter()` and an equivalent comprehension

## Concept Explanation
- `map(function, iterable)` -- applies `function` to every item.
- `filter(function, iterable)` -- keeps items where `function` returns `True`.

Both are commonly paired with `lambda`, and both return a **lazy
iterator** (see `07-iterators`), so wrap the result in `list()` to see or
use the values.

## Syntax
```python
map(function, iterable)
filter(function, iterable)
list(map(function, iterable))
list(filter(function, iterable))
```

## Examples

**Example 1 - `map()` to transform every item**
```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)
```
Expected output: `[2, 4, 6, 8, 10]`

**Example 2 - `filter()` to keep matching items**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)
```
Expected output: `[2, 4, 6, 8]`

**Example 3 - `map()` with a named function**
```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

temps_f = list(map(celsius_to_fahrenheit, [0, 20, 37, 100]))
print(temps_f)
```
Expected output: `[32.0, 68.0, 98.6, 212.0]`

**Example 4 - the comprehension equivalent**
```python
numbers = [1, 2, 3, 4, 5]
print([n * 2 for n in numbers])
print([n for n in numbers if n % 2 == 0])
```
Expected output:
```
[2, 4, 6, 8, 10]
[2, 4]
```

## Common Mistakes
- Forgetting to wrap the result in `list()` -- printing a bare `map(...)`
  shows `<map object at 0x...>`, not the values.
- Using `map()`/`filter()` where a comprehension is clearer -- most style
  guides prefer comprehensions for simple cases; know both.
- Passing a function that returns `None` to `filter()` -- `None` is
  falsy, so everything gets dropped.

## Practice
1. Use `map()` to square every number in a list.
2. Use `filter()` to keep only words longer than 3 letters.
3. Use `map()` with a named function to uppercase a list of names.
4. Rewrite 1 and 2 as list comprehensions.

## Challenge
Given a list of product dicts, use `filter()` for products under $20, then
`map()` to extract just their names.

## Mini Project
In the `19-projects` Expense Tracker, use `filter()` to build a
"filter by category" feature.

## Summary
`map()` transforms every item; `filter()` keeps only matching items. Both
return lazy iterators. In modern Python, comprehensions are often more
readable for simple cases, but you'll see `map()`/`filter()` constantly in
other code.

## Next Step
Continue to [`04-args-and-kwargs.md`](04-args-and-kwargs.md).
