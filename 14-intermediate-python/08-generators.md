# Generators

## Learning Objectives
- Write a generator function using `yield`
- Explain why generators are memory-efficient versus building a full list
- Use a generator expression
- Know when to reach for a generator instead of a list

## Concept Explanation
A **generator** produces values **lazily** -- one at a time, on demand --
instead of building the whole sequence in memory. It's an iterator you
write yourself using `yield` instead of `return`.
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```
Each `yield` pauses the function, hands back one value, and resumes
exactly where it left off next time. This matters for huge or infinite
sequences -- a generator never holds everything in memory at once.

## Syntax
```python
def generator_function():
    yield value1
    yield value2

gen = (expression for item in iterable)   # generator expression
```

## Examples

**Example 1 - A basic generator function**
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(number)
```
Expected output:
```
3
2
1
```

**Example 2 - Generators are lazy**
```python
def numbers_generator():
    print("Starting...")
    yield 1
    print("About to yield 2...")
    yield 2

gen = numbers_generator()   # nothing printed yet!
print("Generator created.")
for n in gen:
    print(n)
```
Expected output:
```
Generator created.
Starting...
1
About to yield 2...
2
```

**Example 3 - A generator expression**
```python
squares = (n ** 2 for n in range(1, 6))
print(list(squares))
```
Expected output: `[1, 4, 9, 16, 25]`

**Example 4 - An "infinite" generator, used with a limit**
```python
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

gen = even_numbers()
print([next(gen) for _ in range(5)])
```
Expected output: `[0, 2, 4, 6, 8]`

## Common Mistakes
- Trying to reuse an exhausted generator -- call the generator function
  again for a fresh one.
- Trying to index into a generator (`gen[0]`) -- unsupported; use `next()`
  or iteration only.
- Using a list when a generator would be far more memory-efficient (large
  files), or the reverse when you need multiple passes or a length.
- Confusing `yield` with `return` -- `return` inside a generator ends it
  (raises `StopIteration`), it does not hand back a value the normal way.

## Practice
1. Write a generator `count_up_to(n)` yielding `1, 2, ..., n`.
2. Write a generator expression for squares of 1-10; convert to a list.
3. Write `even_numbers_up_to(n)` yielding even numbers 0 to `n`.
4. Explain (a comment is fine) why summing a generator expression uses
   less memory than summing an equivalent list comprehension.

## Challenge
Write `fibonacci(n)` yielding the first `n` Fibonacci numbers.

## Mini Project
Rewrite "read a huge file line by line" from `10-file-handling` as a
generator `read_large_file(filename)` yielding one stripped line at a
time.

## Summary
A generator function uses `yield` to produce values one at a time, lazily
-- memory-efficient for large/unbounded sequences. Generator expressions
offer the same laziness with `()` instead of `[]`. Use a generator when
you only need to iterate once, in order, without holding every value in
memory.

## Next Step
Continue to [`09-decorators.md`](09-decorators.md).
