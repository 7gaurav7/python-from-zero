# 05 — Loops

## 1. Beginner-Friendly Explanation

Loops let you repeat an action multiple times without writing the same code
over and over. Python has two kinds:

- **`for` loop** — repeats a fixed, known number of times (or once per item
  in a collection).
- **`while` loop** — repeats *as long as* a condition stays `True` (used
  when you don't know in advance how many times you'll need to repeat).

## 2. Important Concepts

- **`for` loop** — iterates over a sequence (like `range()` or a list).
- **`range(n)`** — generates numbers from `0` up to (not including) `n`.
- **`while` loop** — keeps running while its condition is `True`.
- **Infinite loop** — a `while` loop whose condition never becomes `False`
  (a common bug — always make sure something inside the loop can end it).
- **`break`** — immediately exits a loop.
- **`continue`** — skips the rest of the current iteration and moves to the
  next one.
- **Loop variable** — the variable that takes on each value during a `for`
  loop.

## 3. Syntax

```python
for variable in range(n):
    ...                     # runs n times, variable = 0, 1, ..., n-1

for variable in range(start, stop):
    ...

for variable in range(start, stop, step):
    ...

while condition:
    ...                     # runs as long as condition is True

break        # exit the loop immediately
continue     # skip to the next iteration
```

## 4. Simple Examples

**Example 1 — Counting with `for` and `range`**
```python
for i in range(5):
    print(i)
```
Expected output:
```
0
1
2
3
4
```

**Example 2 — `range` with start, stop, step**
```python
for i in range(2, 10, 2):
    print(i)
```
Expected output:
```
2
4
6
8
```

**Example 3 — `while` loop**
```python
count = 0
while count < 3:
    print("Count is", count)
    count += 1
```
Expected output:
```
Count is 0
Count is 1
Count is 2
```

**Example 4 — `break` and `continue`**
```python
for i in range(10):
    if i == 5:
        break          # stop the loop entirely
    if i % 2 == 0:
        continue       # skip even numbers, go to next i
    print(i)
```
Expected output:
```
1
3
```

## 5. Practice Problems

1. Print the numbers from 1 to 10 using a `for` loop.
2. Print all even numbers from 1 to 20 using `range` with a step.
3. Use a `while` loop to print a countdown from 10 to 1, then print "Liftoff!".
4. Write a loop that adds up all numbers from 1 to 100 and prints the total.
5. Write a loop that asks the user to guess a secret number (fixed in the
   code) and keeps asking until they guess correctly.

## 6. Challenge Problems

1. Print a multiplication table (1 to 10) for a number the user provides,
   using a `for` loop.
2. Write a program using nested `for` loops that prints a triangle pattern
   of `*`, e.g. for size 5:
   ```
   *
   **
   ***
   ****
   *****
   ```

## 7. Common Mistakes

- **Forgetting to update the loop variable in a `while` loop**, causing an
  infinite loop (e.g. forgetting `count += 1`).
- **Off-by-one errors** — remember `range(5)` gives `0, 1, 2, 3, 4`, not
  `1, 2, 3, 4, 5`.
- **Using `break` when you meant `continue`** (or vice versa) — `break`
  exits the whole loop, `continue` only skips the current iteration.
- **Modifying a list while looping over it** (covered more in `07`) — this
  can cause confusing bugs; make a copy first if you need to.

## 8. Mini Quiz

1. What does `range(3)` produce?
2. Which loop do you use when you don't know in advance how many times to repeat?
3. What does `break` do?
4. What does `continue` do?
5. What common bug happens if you forget to update a `while` loop's
   condition variable?

*(Answers: 1. `0, 1, 2`  2. `while`  3. Exits the loop entirely  4. Skips to the next iteration  5. An infinite loop)*

## 9. Practical Exercise

Create `number_facts.py` that loops through numbers 1 to 20 and, for each
one, prints whether it's even or odd, and additionally prints "Fizz" if the
number is divisible by 3, "Buzz" if divisible by 5 (the classic "FizzBuzz").

➡️ Matching files: [`exercises/05_loops_exercises.py`](../exercises/05_loops_exercises.py) ·
[`solutions/05_loops_solutions.py`](../solutions/05_loops_solutions.py)

**Previous:** [`04-conditions`](../04-conditions/README.md) | **Next:** [`06-strings`](../06-strings/README.md)
