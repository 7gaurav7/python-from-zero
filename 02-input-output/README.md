# 02 — Input and Output

## 1. Beginner-Friendly Explanation

So far your programs only ever do the same thing every time they run. To
make programs interactive, they need to be able to **ask the user a
question** and **use the answer**. In Python:

- `print()` sends output **to** the screen.
- `input()` receives input **from** the user (typed at the keyboard).

`input()` always gives you back a **string** — even if the user types a
number — so if you need it as a number for math, you must convert it.

## 2. Important Concepts

- **Output** — information your program displays.
- **Input** — information the user provides while the program runs.
- **`input()` always returns a `str`.** You must convert it using `int()` or
  `float()` if you want to do math with it.
- **Type conversion / casting** — turning one type into another:
  `int("5")` → `5`, `str(5)` → `"5"`, `float("3.14")` → `3.14`.
- **f-strings** — the modern, readable way to build strings that include
  variables.

## 3. Syntax

```python
input("Prompt shown to the user: ")   # returns a str
int(x)                                # convert x to an integer
float(x)                              # convert x to a float
str(x)                                # convert x to a string

print(value1, value2, ...)            # print one or more values
print(f"Text {variable} more text")   # f-string formatting
```

## 4. Simple Examples

**Example 1 — Basic input and output**
```python
name = input("What is your name? ")
print("Hello,", name)
```
Sample run (user types `Alice`):
```
What is your name? Alice
Hello, Alice
```

**Example 2 — Converting input to a number**
```python
age_text = input("How old are you? ")   # "25", a string
age = int(age_text)                     # 25, an integer
print("Next year you'll be", age + 1)
```
Sample run (user types `25`):
```
How old are you? 25
Next year you'll be 26
```

**Example 3 — f-strings**
```python
name = "Bob"
age = 30
print(f"{name} is {age} years old.")
```
Expected output:
```
Bob is 30 years old.
```

**Example 4 — Doing math with two inputs**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"The sum is {a + b}")
```
Sample run (user types `4` then `5.5`):
```
Enter first number: 4
Enter second number: 5.5
The sum is 9.5
```

## 5. Practice Problems

1. Ask the user for their name and print a personalized greeting.
2. Ask the user for two numbers and print their product.
3. Ask the user for their birth year and print their approximate age
   (assume the current year is 2026).
4. Ask the user for a temperature in Celsius and convert it to Fahrenheit
   (`F = C * 9/5 + 32`).
5. Ask the user for their first and last name separately, then print them
   combined as `"Last, First"`.

## 6. Challenge Problems

1. Ask the user for the length and width of a rectangle (as floats) and
   print both the area and the perimeter, formatted to 2 decimal places
   using an f-string (`f"{value:.2f}"`).
2. Ask the user for a number of seconds and convert/print it as
   hours, minutes, and remaining seconds.

## 7. Common Mistakes

- **Forgetting to convert `input()` before doing math:**
  ```python
  age = input("Age: ")
  print(age + 1)   # TypeError: can't add str and int
  ```
  Fix: `age = int(input("Age: "))`
- **Converting text that isn't a valid number:** `int("abc")` crashes with a
  `ValueError`. (You'll learn to handle this safely in `11-exceptions`.)
- **Forgetting the `f` before an f-string:** `print("{name}")` prints the
  literal text `{name}` instead of the variable's value.
- **Confusing `print()`'s comma-separated values** (which auto-add spaces)
  with string concatenation using `+` (which does not).

## 8. Mini Quiz

1. What data type does `input()` always return?
2. How do you convert `"42"` into the integer `42`?
3. What letter do you put before a string's opening quote to make it an
   f-string?
4. What will `print("Age:", 5 + 5)` output?
5. True or False: `input()` can only be used once per program.

*(Answers: 1. `str`  2. `int("42")`  3. `f`  4. `Age: 10`  5. False — you can call it as many times as you like)*

## 9. Practical Exercise

Create `mini_form.py` that asks the user for their name, age, and city, then
prints a nicely formatted summary sentence using an f-string, e.g.:
`"Alice is 25 years old and lives in Paris."`

➡️ Matching files: [`exercises/02_input_output_exercises.py`](../exercises/02_input_output_exercises.py) ·
[`solutions/02_input_output_solutions.py`](../solutions/02_input_output_solutions.py)

**Previous:** [`01-variables-and-data-types`](../01-variables-and-data-types/README.md) | **Next:** [`03-operators`](../03-operators/README.md)
