# *args and **kwargs

## Learning Objectives
- Write a function accepting any number of positional arguments (`*args`)
- Write a function accepting any number of keyword arguments (`**kwargs`)
- Explain what `*args`/`**kwargs` actually are inside the function
- Use `*`/`**` to unpack a list/dict into a function call

## Concept Explanation
`*args` collects extra **positional** arguments into a tuple; `**kwargs`
collects extra **keyword** arguments into a dictionary. The names `args`/
`kwargs` are convention -- the `*`/`**` is what matters.

## Syntax
```python
def function_name(*args):
    ...   # args is a tuple

def function_name(**kwargs):
    ...   # kwargs is a dictionary

def function_name(required, *args, **kwargs):
    ...

my_list = [1, 2, 3]
function_name(*my_list)        # unpack into positional args

my_dict = {"name": "Alice", "age": 25}
function_name(**my_dict)        # unpack into keyword args
```

## Examples

**Example 1 - `*args` collects extra positional arguments**
```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20))
```
Expected output:
```
6
30
```

**Example 2 - `**kwargs` collects extra keyword arguments**
```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25, city="Paris")
```
Expected output:
```
name: Alice
age: 25
city: Paris
```

**Example 3 - mixing required parameters with `*args`**
```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Carla")
```
Expected output:
```
Hello, Alice!
Hello, Bob!
Hello, Carla!
```

**Example 4 - unpacking a list/dict into a function call**
```python
def add(a, b, c):
    return a + b + c

print(add(*[1, 2, 3]))
print(add(**{"a": 10, "b": 20, "c": 30}))
```
Expected output:
```
6
60
```

## Common Mistakes
- Confusing `*args`/`**kwargs` (gathering, in a definition) with `*`/`**`
  unpacking (spreading, at a call) -- same symbols, opposite direction.
- Wrong parameter order -- normal params, then `*args`, then keyword-only
  params, then `**kwargs`.
- Accessing `kwargs` with dot notation instead of `kwargs["key"]` or
  `.items()` -- it's a plain dictionary.
- Overusing `*args`/`**kwargs` when parameters are well known in advance
  -- explicit named parameters are more readable and catch typos.

## Practice
1. Write `total(*args)` returning the sum of any number of numbers.
2. Write `print_all(**kwargs)` printing every key-value pair.
3. Write `largest(*args)` returning the largest value (no `max()`).
4. Call a 3-parameter function by unpacking a list of 3 items with `*`.

## Challenge
Write `build_profile(name, **kwargs)` returning a dict combining the
required `name` with however many optional keyword details are provided.

## Mini Project
Extend the `19-projects` Contact Book's `add_contact()` to accept
`**kwargs` for optional fields beyond name/phone/email.

## Summary
`*args` gathers extra positional arguments into a tuple; `**kwargs`
gathers extra keyword arguments into a dict, letting a function accept a
flexible number of inputs. The same symbols, used when *calling* a
function, unpack a list/dict into separate arguments.

## Next Step
Continue to [`05-enumerate-and-zip.md`](05-enumerate-and-zip.md).
