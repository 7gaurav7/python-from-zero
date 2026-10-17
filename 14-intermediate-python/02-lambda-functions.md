# Lambda Functions

## Learning Objectives
- Write a small, unnamed function using `lambda`
- Explain when a `lambda` is appropriate versus a `def` function
- Use a `lambda` as a sort key

## Concept Explanation
A **lambda function** is a tiny, unnamed function written as a single
expression -- for situations where you need a small function *briefly*,
often as an argument to another function.
```python
square = lambda n: n ** 2
print(square(4))   # 16
```
Equivalent to `def square(n): return n ** 2`. Lambdas shine as a throwaway
argument, not as a general replacement for named functions.

## Syntax
```python
lambda parameters: expression
```
No `def`, no name (unless assigned), no `return` (the expression's value
is returned automatically), and must be a single expression.

## Examples

**Example 1 - A basic lambda**
```python
add = lambda a, b: a + b
print(add(3, 4))
```
Expected output: `7`

**Example 2 - Lambda as a sort key**
```python
students = [("Alice", 85), ("Bob", 92), ("Carla", 78)]
students.sort(key=lambda student: student[1])
print(students)
```
Expected output: `[('Carla', 78), ('Alice', 85), ('Bob', 92)]`

**Example 3 - Sorting strings by length**
```python
words = ["banana", "kiwi", "apple", "fig"]
words.sort(key=lambda word: len(word))
print(words)
```
Expected output: `['kiwi', 'fig', 'apple', 'banana']`

**Example 4 - Lambda with a default value**
```python
greet = lambda name="friend": f"Hello, {name}!"
print(greet())
print(greet("Sam"))
```
Expected output:
```
Hello, friend!
Hello, Sam!
```

## Common Mistakes
- Overusing lambdas for anything beyond a single simple expression --
  write a named `def` for multi-line logic.
- Assigning a lambda to a variable just to call it later -- PEP 8
  recommends a normal `def` whenever you're naming a function.
- Forgetting a lambda can't contain statements (no `if` blocks, loops, or
  `print()`) -- a conditional *expression* is fine:
  `lambda x: "even" if x % 2 == 0 else "odd"`.

## Practice
1. Write a lambda that doubles a number.
2. Sort a list of `(name, age)` tuples by age using a lambda key.
3. Sort a list of product dicts by their `"price"` key.
4. Write a lambda that returns `True` if a number is negative.

## Challenge
Sort a list of strings by length, then alphabetically for ties, using one
lambda returning a tuple key: `lambda s: (len(s), s)`.

## Mini Project
In the `19-projects` Contact Book, use a lambda with `sorted()` to display
contacts alphabetically by name.

## Summary
`lambda` creates a small unnamed function in one expression -- ideal as a
quick `key=` argument. For anything more involved, prefer a named `def`.

## Next Step
Continue to [`03-map-and-filter.md`](03-map-and-filter.md).
