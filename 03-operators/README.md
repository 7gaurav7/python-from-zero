# 03 — Operators

## 1. Beginner-Friendly Explanation

Operators are symbols that perform an action on values, like `+` for
addition. You already used one in the last topics (`=` for assignment).
Python has several families of operators: **arithmetic** (math),
**comparison** (compare two values), **logical** (combine True/False
values), and **assignment shortcuts**.

## 2. Important Concepts

- **Arithmetic operators** — do math: `+ - * / // % **`
- **Comparison operators** — compare two values and produce a `bool`:
  `== != > < >= <=`
- **Logical operators** — combine boolean values: `and`, `or`, `not`
- **Assignment operators** — shortcuts for updating a variable:
  `+= -= *= /=`
- **Operator precedence** — Python follows math order of operations
  (parentheses first, then `**`, then `* / // %`, then `+ -`).

## 3. Syntax

```python
# Arithmetic
a + b      # addition
a - b      # subtraction
a * b      # multiplication
a / b      # division (always returns a float)
a // b     # floor division (rounds down to whole number)
a % b      # modulus (remainder after division)
a ** b     # exponent (a to the power of b)

# Comparison (result is always True or False)
a == b     # equal to
a != b     # not equal to
a > b
a < b
a >= b
a <= b

# Logical
a and b
a or b
not a

# Assignment shortcuts
a += 1     # same as a = a + 1
a -= 1     # same as a = a - 1
a *= 2     # same as a = a * 2
a /= 2     # same as a = a / 2
```

## 4. Simple Examples

**Example 1 — Arithmetic operators**
```python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 2)
```
Expected output:
```
13
7
30
3.3333333333333335
3
1
100
```

**Example 2 — Comparison operators**
```python
print(5 == 5)
print(5 != 3)
print(5 > 10)
```
Expected output:
```
True
True
False
```

**Example 3 — Logical operators**
```python
age = 20
has_id = True
print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```
Expected output:
```
True
True
False
```

**Example 4 — Assignment shortcuts**
```python
score = 10
score += 5
print(score)
score *= 2
print(score)
```
Expected output:
```
15
30
```

## 5. Practice Problems

1. Print the result of `17 % 5` and explain in a comment what it represents.
2. Given `a = 7` and `b = 2`, print the result of every arithmetic operator
   applied to them.
3. Write a program that checks if a number stored in a variable is even
   (hint: use `%` and `==`).
4. Given two variables `age` and `has_ticket` (bool), print whether a
   person can enter a concert if they are 16+ **and** have a ticket.
5. Start with `total = 100`, then use `-=`, `+=`, and `*=` in sequence, and
   print `total` after each operation.

## 6. Challenge Problems

1. Write a program that takes a number of total minutes and, using `//` and
   `%`, prints how many whole hours and leftover minutes that equals.
2. Given a person's `age`, `income`, and `has_good_credit` (bool), write a
   single boolean expression (using `and`/`or`) that evaluates whether they
   qualify for a loan (e.g. age >= 21 and (income >= 30000 or has_good_credit)).

## 7. Common Mistakes

- **Confusing `=` and `==`.** `=` assigns, `==` compares. `if x = 5` is
  invalid syntax — you want `if x == 5`.
- **Expecting `/` to give a whole number.** `/` always returns a `float` in
  Python 3, even `10 / 2` gives `5.0`. Use `//` for whole-number division.
- **Forgetting operator precedence** — `2 + 3 * 4` is `14`, not `20`, because
  `*` runs before `+`. Use parentheses when unsure: `(2 + 3) * 4`.
- **Using `&`/`|` instead of `and`/`or`** — those are different (bitwise)
  operators; beginners should stick to `and`/`or`/`not` for boolean logic.

## 8. Mini Quiz

1. What does `//` do differently from `/`?
2. What does `%` return?
3. What is the result of `2 ** 3`?
4. What does `and` require to return `True`?
5. What's wrong with `if x = 10:`?

*(Answers: 1. It rounds the division result down to a whole number  2. The remainder after division  3. `8`  4. Both sides must be `True`  5. It should be `==`, not `=`, for comparison)*

## 9. Practical Exercise

Create `bmi_calculator.py` that asks the user for their weight (kg) and
height (m), calculates their BMI (`weight / height ** 2`), and prints the
result rounded to 1 decimal place using an f-string.

➡️ Matching files: [`exercises/03_operators_exercises.py`](../exercises/03_operators_exercises.py) ·
[`solutions/03_operators_solutions.py`](../solutions/03_operators_solutions.py)

**Previous:** [`02-input-output`](../02-input-output/README.md) | **Next:** [`04-conditions`](../04-conditions/README.md)
