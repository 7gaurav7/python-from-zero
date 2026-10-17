# Decorators

## Learning Objectives
- Explain what a decorator is and why functions can be passed around like
  any other value
- Write a simple decorator using `*args`/`**kwargs`
- Apply a decorator with `@decorator_name` syntax
- Recognize decorators in other people's code (e.g. `@staticmethod`)

## Concept Explanation
Functions in Python are just values -- you can pass them into other
functions and return them from other functions. A **decorator** is a
function that takes another function, wraps it with extra behavior, and
returns the wrapped version.
```python
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"hello, {name}"

print(greet("alice"))   # HELLO, ALICE
```
`@shout` is shorthand for `greet = shout(greet)`. This is why `*args`/
`**kwargs` and iterators/generators came first: `wrapper` needs
`*args`/`**kwargs` to accept whatever arguments the original function
needs, without knowing them in advance.

## Syntax
```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator_name
def some_function(...):
    ...
```

## Examples

**Example 1 - A timing decorator**
```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.6f} seconds")
        return result
    return wrapper

@time_it
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

print(slow_add(2, 3))
```
Sample output (timing varies):
```
slow_add took 0.100xxx seconds
5
```

**Example 2 - A logging decorator**
```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(3, 4))
```
Expected output:
```
Calling add with (3, 4), {}
7
```

**Example 3 - A decorator without `@` syntax**
```python
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def greet(name):
    return f"hello, {name}"

greet = shout(greet)   # exactly what @shout does
print(greet("alice"))
```
Expected output: `HELLO, ALICE`

**Example 4 - A decorator that repeats a function call**
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
```
Expected output:
```
Hi!
Hi!
Hi!
```

## Common Mistakes
- Forgetting to `return wrapper` from the decorator.
- Forgetting `*args`/`**kwargs` in `wrapper`, breaking any function with
  parameters.
- Forgetting to call/return `func(*args, **kwargs)` inside `wrapper` --
  silently losing the original behavior.
- Overusing decorators where a plain function call would be clearer.

## Practice
1. Write `log_calls` printing a function's name every time it's called.
2. Write `time_it` printing how long a function took (Example 1).
3. Write `uppercase_result` uppercasing whatever string a function returns.
4. Stack two decorators on one function and observe the order they run in.

## Challenge
Write a parameterized decorator `retry(times)` that retries the decorated
function up to `times` times if it raises an exception, only letting the
exception propagate if every attempt fails.

## Mini Project
Add a `@log_calls`-style wrapper around the `19-projects` Expense
Tracker's `add_expense()` that prints a line every time an expense is
added, without modifying the method's internal code.

## Summary
A decorator wraps a function to add behavior before/after/around its
call, using `*args`/`**kwargs` for any signature. `@decorator_name` above
a function is shorthand for reassigning it to `decorator_name(function)`.
You'll see decorators throughout real-world Python (`@staticmethod`,
`@property`, web framework routes).

## Next Step
You've completed `14-intermediate-python`. Continue to
[`15-working-with-data`](../15-working-with-data/README.md).
