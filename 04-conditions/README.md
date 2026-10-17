# 04 — Conditions

## 1. Beginner-Friendly Explanation

So far, every line of your program always runs. Real programs need to make
**decisions**: "if it's raining, bring an umbrella; otherwise, don't."
Python does this with `if`, `elif` (short for "else if"), and `else`.

This is also where **indentation** starts to matter. Python uses spaces at
the start of a line to know which code belongs "inside" a decision.

## 2. Important Concepts

- **`if` statement** — runs a block of code only if a condition is `True`.
- **`elif`** — checks another condition if the previous ones were `False`.
- **`else`** — runs if none of the previous conditions were `True`.
- **Indentation** — Python requires consistent indentation (4 spaces is the
  PEP 8 standard) to define which lines belong to a block.
- **Truthy / Falsy** — values that count as `False` in a condition include
  `0`, `""` (empty string), `None`, and empty collections; everything else
  counts as `True`.
- **Nested conditions** — an `if` statement inside another `if` statement.

## 3. Syntax

```python
if condition:
    # runs only if condition is True
    ...
elif another_condition:
    # runs only if the first condition was False and this one is True
    ...
else:
    # runs if none of the above were True
    ...
```

## 4. Simple Examples

**Example 1 — Basic `if`**
```python
age = 20
if age >= 18:
    print("You are an adult.")
```
Expected output:
```
You are an adult.
```

**Example 2 — `if` / `else`**
```python
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
Expected output:
```
You are a minor.
```

**Example 3 — `if` / `elif` / `else`**
```python
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```
Expected output:
```
Grade: B
```

**Example 4 — Nested conditions**
```python
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Bring your ID next time.")
else:
    print("Entry denied: too young.")
```
Expected output:
```
Entry allowed.
```

## 5. Practice Problems

1. Write a program that checks if a number is positive, negative, or zero.
2. Write a program that checks if a year is a leap year (divisible by 4,
   except centuries unless divisible by 400).
3. Write a program that takes a user's age and prints a message for
   "child" (0–12), "teenager" (13–19), or "adult" (20+).
4. Write a program that checks if a password (a string) is at least 8
   characters long, printing "Strong enough" or "Too short".
5. Write a program that takes three numbers and prints the largest one.

## 6. Challenge Problems

1. Write a simple grading program that takes a numeric score and prints a
   letter grade A/B/C/D/F using at least 4 `elif` branches.
2. Write a program that takes a triangle's three side lengths and
   determines whether it's equilateral, isosceles, or scalene.

## 7. Common Mistakes

- **Forgetting the colon `:`** at the end of `if`/`elif`/`else` lines.
- **Inconsistent indentation** — mixing tabs and spaces, or using different
  amounts of indentation for the same block, causes an `IndentationError`.
- **Using `=` instead of `==`** inside a condition.
- **Writing `elif` after an unrelated `if`** — remember `elif`/`else` only
  attach to the `if` directly above them at the same indentation level.
- **Over-nesting** — too many nested `if`s become hard to read; often an
  `elif` chain is clearer.

## 8. Mini Quiz

1. What keyword checks a second condition after an `if` fails?
2. What symbol must end every `if`, `elif`, and `else` line?
3. What error do you get for inconsistent indentation?
4. True or False: an `else` block always needs its own condition.
5. What does `if 0:` do — does the block run?

*(Answers: 1. `elif`  2. `:`  3. `IndentationError`  4. False — `else` has no condition, it's the "everything else" case  5. No, the block doesn't run because `0` is falsy)*

## 9. Practical Exercise

Create `ticket_price.py` that asks for a person's age and prints a ticket
price: free for under 5, $10 for ages 5–17, $15 for ages 18–64, and $8 for
65+.

➡️ Matching files: [`exercises/04_conditions_exercises.py`](../exercises/04_conditions_exercises.py) ·
[`solutions/04_conditions_solutions.py`](../solutions/04_conditions_solutions.py)

**Previous:** [`03-operators`](../03-operators/README.md) | **Next:** [`05-loops`](../05-loops/README.md)
