# 07 — Lists, Tuples, and Sets

## 1. Beginner-Friendly Explanation

So far each variable holds one value. Real programs usually need to hold
**collections** of values — a shopping list, a list of students, a set of
unique tags. Python gives you three key collection types:

- **List** — an ordered, changeable collection: `[1, 2, 3]`. Use this most
  of the time.
- **Tuple** — an ordered, *unchangeable* collection: `(1, 2, 3)`. Use it for
  data that shouldn't change (like coordinates).
- **Set** — an unordered collection of **unique** values: `{1, 2, 3}`. Use
  it when you need to eliminate duplicates or check membership fast.

## 2. Important Concepts

- **Ordered vs. unordered** — lists/tuples keep the order you put items in;
  sets do not guarantee any order.
- **Mutable vs. immutable** — lists and sets can be changed after creation
  (mutable); tuples cannot (immutable).
- **Indexing/slicing** — works on lists and tuples the same way as strings.
- **Duplicates** — lists and tuples allow duplicates; sets automatically
  remove them.
- **Common list methods** — `.append()`, `.remove()`, `.pop()`, `.sort()`,
  `.insert()`, `.index()`, `.count()`.
- **`in` operator** — checks membership: `"a" in my_list`.
- **`len()`** — works on all three collection types.

## 3. Syntax

```python
# List
my_list = [1, 2, 3]
my_list.append(4)          # add to the end
my_list.remove(2)          # remove first matching value
my_list.pop()               # remove and return the last item
my_list.sort()               # sort in place
my_list[0]                  # access by index
my_list[0:2]                # slicing

# Tuple
my_tuple = (1, 2, 3)        # cannot be changed after creation

# Set
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)

# Common to all
len(collection)
value in collection
for item in collection:
    ...
```

## 4. Simple Examples

**Example 1 — Lists: create, access, modify**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("date")
print(fruits)
fruits.remove("banana")
print(fruits)
```
Expected output:
```
apple
['apple', 'banana', 'cherry', 'date']
['apple', 'cherry', 'date']
```

**Example 2 — Looping over a list**
```python
scores = [85, 90, 78]
for score in scores:
    print(f"Score: {score}")
```
Expected output:
```
Score: 85
Score: 90
Score: 78
```

**Example 3 — Tuples are immutable**
```python
point = (3, 4)
print(point[0], point[1])
# point[0] = 10   # this would raise: TypeError: 'tuple' object does not support item assignment
```
Expected output:
```
3 4
```

**Example 4 — Sets remove duplicates**
```python
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)
print(4 in unique_numbers)
```
Expected output:
```
{1, 2, 3}
False
```

## 5. Practice Problems

1. Create a list of 5 favorite foods, print the whole list, then print just
   the first and last items.
2. Add two more items to that list, remove one, then print the final list.
3. Given a list of numbers, use a loop to compute and print their total and
   average.
4. Create a tuple representing a `(latitude, longitude)` pair and print both
   values.
5. Given a list with duplicate values, convert it to a set to print only the
   unique values, then print how many unique values there are.

## 6. Challenge Problems

1. Write a program that takes a list of numbers and prints the largest and
   smallest values **without using** the built-in `max()`/`min()` functions
   (use a loop and comparisons instead).
2. Given two lists of numbers, use sets to print the values common to both
   lists (hint: `set1 & set2` gives the intersection).

## 7. Common Mistakes

- **Trying to modify a tuple:** `point[0] = 5` → `TypeError`.
- **Expecting a set to preserve order** — sets do not guarantee the order
  you added items in, and printing one may show items in a different order
  than you typed them.
- **Using `.append()` on the wrong thing** — `.append()` adds one item; to
  add multiple items from another list use `.extend()`.
- **Modifying a list while looping over it with indices**, causing skipped
  items — this is a subtle bug and best avoided by looping over a copy if
  you need to remove items.
- **Confusing `[]` (list), `()` (tuple), and `{}` (set/dict)** — `{}` alone
  actually creates an empty **dictionary**, not an empty set (use `set()`
  for an empty set).

## 8. Mini Quiz

1. Which collection type does not allow duplicate values?
2. Which collection type cannot be changed after creation?
3. What method adds an item to the end of a list?
4. How do you check if `"x"` is in a list called `items`?
5. What does `set([1, 1, 2, 2, 3])` return?

*(Answers: 1. Set  2. Tuple  3. `.append()`  4. `"x" in items`  5. `{1, 2, 3}`)*

## 9. Practical Exercise

Create `grade_book.py` that stores a list of 5 student scores, then prints:
the highest score, the lowest score, the average, and the scores sorted
from highest to lowest.

➡️ Matching files: [`exercises/07_lists_tuples_sets_exercises.py`](../exercises/07_lists_tuples_sets_exercises.py) ·
[`solutions/07_lists_tuples_sets_solutions.py`](../solutions/07_lists_tuples_sets_solutions.py)

**Previous:** [`06-strings`](../06-strings/README.md) | **Next:** [`08-dictionaries`](../08-dictionaries/README.md)
