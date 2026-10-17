# Iterators

## Learning Objectives
- Explain what makes an object "iterable"
- Explain the difference between an iterable and an iterator
- Use `iter()` and `next()` directly
- Understand what a `for` loop is actually doing behind the scenes

## Concept Explanation
Every `for item in my_list:` relies on a protocol working quietly behind
the scenes.
- An **iterable** is anything loopable: lists, tuples, strings, dicts, sets, files.
- An **iterator** is the object that produces values one at a time when
  you call `next()` on it.
- `iter()` on an iterable gives you an iterator; a `for` loop does this
  automatically.
```python
numbers = [10, 20, 30]
iterator = iter(numbers)
next(iterator)   # 10
next(iterator)   # 20
next(iterator)   # 30
next(iterator)   # raises StopIteration
```

## Syntax
```python
iter(iterable)     # returns an iterator
next(iterator)      # returns the next value, or raises StopIteration
```

## Examples

**Example 1 - Manually iterating a list**
```python
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
```
Expected output:
```
10
20
30
```

**Example 2 - `StopIteration` when exhausted**
```python
numbers = [1, 2]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("No more items!")
```
Expected output:
```
1
2
No more items!
```

**Example 3 - Strings are iterable too**
```python
iterator = iter("abc")
print(next(iterator))
print(next(iterator))
print(next(iterator))
```
Expected output:
```
a
b
c
```

**Example 4 - What a `for` loop does, spelled out**
```python
def manual_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        print(item)

manual_for_loop([100, 200, 300])
```
Expected output:
```
100
200
300
```

## Common Mistakes
- Confusing "iterable" with "iterator" -- every iterator is iterable, but
  a list can produce a fresh iterator each time you call `iter()` on it,
  while an iterator, once exhausted, stays exhausted.
- Calling `next()` directly on an iterable -- you need `next(iter(x))`.
- Assuming you'll manually call `iter()`/`next()` in everyday code -- in
  practice you'll write `for` loops; this protocol matters for
  understanding generators next.

## Practice
1. Manually `iter()`/`next()` a 4-item list to print items one at a time.
2. Catch `StopIteration` after exhausting a 2-item list's iterator.
3. Use `iter()`/`next()` on a string to print its first 3 characters.
4. Write `manual_for_loop(iterable)` and test it on a list and a string.

## Challenge
Write `nth_item(iterable, n)` returning the `n`th item (0-indexed) using
only `iter()`/`next()` -- no indexing allowed.

## Mini Project
No dedicated project here -- this lesson sets up the next one, generators.

## Summary
An iterable is anything loopable; an iterator is what a `for` loop uses
internally, produced by `iter()` and advanced with `next()` until
`StopIteration`. You'll rarely call these directly, but they're the key
to understanding generators.

## Next Step
Continue to [`08-generators.md`](08-generators.md).
