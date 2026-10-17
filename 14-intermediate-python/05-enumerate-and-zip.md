# enumerate() and zip()

## Learning Objectives
- Use `enumerate()` to loop with both an index and a value
- Use `zip()` to loop over two or more collections in parallel
- Combine `enumerate()`/`zip()` with unpacking in a `for` loop

## Concept Explanation
Two common looping needs: "I need the position *and* the value"
(`enumerate()`), and "I need to walk through two lists together"
(`zip()`). Before `enumerate()`, beginners often write
`range(len(my_list))` and index in -- `enumerate()` is clearer.

## Syntax
```python
enumerate(iterable)              # (index, value) pairs, index from 0
enumerate(iterable, start=1)     # index from 1
zip(iterable1, iterable2)        # (item1, item2) pairs, stops at shortest
```

## Examples

**Example 1 - `enumerate()` for index + value**
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
Expected output:
```
0 apple
1 banana
2 cherry
```

**Example 2 - `enumerate()` starting at 1**
```python
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")
```
Expected output:
```
1. apple
2. banana
3. cherry
```

**Example 3 - `zip()` for parallel iteration**
```python
names = ["Alice", "Bob", "Carla"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```
Expected output:
```
Alice: 85
Bob: 92
Carla: 78
```

**Example 4 - `zip()` to build a dictionary**
```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]
print(dict(zip(keys, values)))
```
Expected output: `{'name': 'Alice', 'age': 25, 'city': 'Paris'}`

## Common Mistakes
- Using `range(len(my_list))` instead of `enumerate()`.
- Forgetting `zip()` stops at the shortest iterable -- extra items in a
  longer one are silently dropped.
- Forgetting `zip()` is lazy -- wrap in `list()` to reuse or measure it.

## Practice
1. Use `enumerate()` to print each item with its 1-based position.
2. Use `zip()` to print `"name: email"` for two parallel lists.
3. Use `zip()`+`dict()` to build a dictionary from two lists.
4. Use `enumerate()` to find the index of the first negative number.

## Challenge
Given three parallel lists (`names`, `subjects`, `scores`), use `zip()`
with all three to print `"name scored score in subject"`.

## Mini Project
In the `19-projects` Quiz Game, number the questions with `enumerate()`
(starting at 1) as they're displayed.

## Summary
`enumerate()` gives the index alongside each value; `zip()` loops over
multiple collections in lockstep. Both combine naturally with tuple
unpacking directly in the `for` line.

## Next Step
Continue to [`06-unpacking.md`](06-unpacking.md).
