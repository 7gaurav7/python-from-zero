# 12 — Modules and Packages

## 1. Beginner-Friendly Explanation

As programs grow, keeping everything in one giant file becomes messy. A
**module** is simply a `.py` file whose code you can reuse in other files by
**importing** it. A **package** is a folder of related modules.

Python also ships with a huge **standard library** — modules that come
built in, so you don't have to write everything from scratch. You've
already been using one without realizing it (`print` and friends are part
of Python's built-ins, always available).

## 2. Important Concepts

- **Module** — a single `.py` file containing code you can import elsewhere.
- **`import`** — brings a module's contents into your current file.
- **`from module import name`** — imports one specific thing from a module,
  so you can use it without the module prefix.
- **`as`** — gives an imported module or name a shorter alias.
- **Standard library** — modules that ship with Python, e.g. `math`,
  `random`, `datetime`. No installation needed.
- **Your own modules** — any `.py` file can be imported by another `.py`
  file in the same folder.
- **`__name__ == "__main__"`** — a common pattern that lets a file be both
  run directly *and* imported by other files without immediately running
  its top-level code.

## 3. Syntax

```python
import math
math.sqrt(16)          # 4.0

from math import sqrt
sqrt(16)                # 4.0, no prefix needed

import random as rnd
rnd.randint(1, 6)       # random int 1-6, inclusive

# Importing your own module (a file named helpers.py in the same folder)
import helpers
helpers.some_function()

# The __main__ guard, used in a standalone script
if __name__ == "__main__":
    main()
```

## 4. Simple Examples

**Example 1 — Using the `math` module**
```python
import math

print(math.sqrt(25))
print(math.pi)
print(math.ceil(4.1))
print(math.floor(4.9))
```
Expected output:
```
5.0
3.141592653589793
5
4
```

**Example 2 — Using the `random` module**
```python
import random

dice_roll = random.randint(1, 6)   # a random whole number from 1 to 6
print("You rolled:", dice_roll)    # output varies each run
```
Sample output (varies each run):
```
You rolled: 4
```

**Example 3 — `from ... import ...`**
```python
from datetime import date

today = date.today()
print("Today is:", today)
```
Sample output (varies by date):
```
Today is: 2026-09-05
```

**Example 4 — Creating and importing your own module**

`helpers.py`:
```python
def shout(text):
    return text.upper() + "!"
```

`main.py` (in the same folder):
```python
import helpers

print(helpers.shout("hello"))
```
Expected output:
```
HELLO!
```

## 5. Practice Problems

1. Use the `math` module to compute the area of a circle given its radius.
2. Use the `random` module to simulate flipping a coin 5 times, printing
   "Heads" or "Tails" each time (hint: `random.choice(["Heads", "Tails"])`).
3. Use the `datetime` module to print the current year only.
4. Create your own module `string_helpers.py` with a function
   `is_palindrome(s)`, then import and use it from another file.
5. Use `random.shuffle()` on a list of 5 names and print the shuffled list.

## 6. Challenge Problems

1. Create a small personal module `calculator.py` with functions `add`,
   `subtract`, `multiply`, `divide` (handling division by zero), then
   write a separate `main.py` that imports and uses it, including a
   `if __name__ == "__main__":` guard.
2. Use the `random` and `time` (or just `random`) modules together to
   simulate a simple "lottery number generator" that picks 6 unique
   numbers between 1 and 49 (hint: `random.sample()`).

## 7. Common Mistakes

- **Re-typing the whole module name unnecessarily** — if you use `math.sqrt`
  a lot, `from math import sqrt` can save typing, but don't overdo `from
  module import *` — it makes it unclear where a name came from.
- **Naming your own file the same as a standard module**, e.g. saving your
  practice file as `random.py` — this will conflict with the real `random`
  module and cause confusing errors.
- **Forgetting that `import` only runs a module's top-level code once** —
  if you need fresh behavior each import, functions are the way to do that,
  not relying on re-importing.
- **Confusing `import module` with `from module import name`** — with the
  first, you always need the `module.` prefix; with the second, you don't.

## 8. Mini Quiz

1. What is a module?
2. What Python module would you use to generate random numbers?
3. What does `from math import sqrt` let you do differently than
   `import math`?
4. Why shouldn't you name your file `random.py`?
5. What does the `__name__ == "__main__"` check let you do?

*(Answers: 1. A `.py` file whose code can be reused elsewhere via `import`  2. `random`  3. Call `sqrt(x)` directly instead of `math.sqrt(x)`  4. It would conflict with Python's real `random` module  5. Let a file work both as a standalone script and as an importable module)*

## 9. Practical Exercise

Create a module `math_helpers.py` with functions `is_prime(n)` and
`factorial(n)`. Then create `main.py` that imports `math_helpers` and uses
both functions on a few test numbers, printing the results.

➡️ Matching files: [`exercises/12_modules_and_packages_exercises.py`](../exercises/12_modules_and_packages_exercises.py) ·
[`solutions/12_modules_and_packages_solutions.py`](../solutions/12_modules_and_packages_solutions.py)

**Previous:** [`11-exceptions`](../11-exceptions/README.md) | **Next:** [`13-oop`](../13-oop/README.md)
