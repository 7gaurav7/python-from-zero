# Math Foundations for ML

## Learning Objectives
By the end of this lesson you can:
- Explain, in plain language, what a vector and a matrix are
- Compute mean, variance, and standard deviation, and explain what each
  tells you
- Explain what a linear equation looks like and why ML models are often
  described as "finding the best line/equation"
- Recognize these terms confidently when they appear in an ML course,
  without needing to have mastered them mathematically yet

## Concept Explanation

You do **not** need to be a mathematician to start learning ML — but a
handful of terms appear so constantly that recognizing them immediately,
rather than being blocked by unfamiliar vocabulary, makes a real
difference. This lesson explains each one at the level you need *right
now*, connecting it back to Python you already know.

**Vectors and matrices** — a vector is just a list of numbers (you've been
using these as Python lists / NumPy arrays this whole time); a matrix is a
2D grid of numbers (a list of lists / a 2D NumPy array). ML almost always
represents data this way: one row per example, one column per feature.

**Mean, variance, and standard deviation** — you already know the mean
(`sum / count`, from `07-lists-tuples-sets`'s practice problems).
*Variance* measures how spread out the values are — computed as the
average of each value's squared distance from the mean. *Standard
deviation* is simply the square root of the variance, expressed in the
same units as the original data (which is why it's used more often than
variance for describing spread in an intuitive way).

**Linear equations** — you know `y = mx + b` from school: a straight line,
where `m` is the slope and `b` is where it crosses the y-axis. An
enormous amount of ML (starting with "linear regression," one of the very
first models you'll meet in any ML course) is, at its core, about finding
the best `m` and `b` (or their higher-dimensional equivalents) that fit a
set of data points.

## Syntax

```python
import numpy as np

# Mean, variance, standard deviation -- pure Python and NumPy versions
values = [10, 12, 23, 23, 16, 23, 21, 16]

mean = sum(values) / len(values)
variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = variance ** 0.5

# NumPy does all of this in one call each:
arr = np.array(values)
arr.mean()
arr.var()
arr.std()

# A simple linear equation as a Python function
def linear_equation(x, slope, intercept):
    return slope * x + intercept
```

## Examples

**Example 1 — Mean, variance, and standard deviation, by hand**
```python
values = [10, 12, 23, 23, 16, 23, 21, 16]

mean = sum(values) / len(values)
variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = variance ** 0.5

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard deviation: {std_dev:.2f}")
```
Expected output:
```
Mean: 18.0
Variance: 24.0
Standard deviation: 4.90
```

**Example 2 — The same calculation using NumPy**
```python
import numpy as np

values = np.array([10, 12, 23, 23, 16, 23, 21, 16])
print(values.mean())
print(values.var())
print(values.std())
```
Expected output:
```
18.0
24.0
4.898979485566356
```

**Example 3 — A linear equation as a Python function**
```python
def linear_equation(x, slope, intercept):
    return slope * x + intercept

for x in range(5):
    print(x, "->", linear_equation(x, slope=2, intercept=1))
```
Expected output:
```
0 -> 1
1 -> 3
2 -> 5
3 -> 7
4 -> 9
```
(This is literally `y = 2x + 1`. An ML "linear regression" model is a
program that automatically discovers a slope and intercept like these
directly from data, rather than you choosing them by hand.)

**Example 4 — Representing tabular data as vectors (rows)**
```python
import numpy as np

# Each row is one "example": [hours_studied, practice_tests_taken]
# This is exactly the "one row per example" idea mentioned above.
students = np.array([
    [2, 1],
    [5, 3],
    [8, 5],
])
print(students.shape)      # (3 students, 2 features each)
print(students[:, 0])      # every student's hours_studied (the first column)
```
Expected output:
```
(3, 2)
[2 5 8]
```

## Common Mistakes

- **Assuming you need to master calculus/linear algebra before starting
  ML.** You need to *recognize* these terms and be comfortable computing
  the basics shown here — deep mathematical mastery can come later, and
  often comes more easily once you've seen the concepts used in real code
  first.
- **Confusing variance and standard deviation** — variance is in *squared*
  units (hard to interpret directly); standard deviation undoes that
  squaring, giving you a number in the original units, which is why it's
  usually the more intuitive one to report.
- **Forgetting a "linear" relationship means a straight line** — many
  real-world relationships aren't linear at all, which is exactly why ML
  has many models beyond linear regression; it's simply the clearest
  starting point for understanding "fitting a model to data."
- **Mixing up rows and columns in a matrix** — get comfortable with "rows
  are examples, columns are features" (Example 4) now; almost every ML
  library assumes this shape.

## Practice

1. Compute the mean, variance, and standard deviation of a list of 6
   numbers of your choice, first by hand (with a comprehension, as in
   Example 1) and then with NumPy — confirm they match.
2. Write `linear_equation(x, slope, intercept)` and use it to generate 10
   points of your own choosing.
3. Given a small NumPy 2D array representing (rows = people, columns =
   [age, height]), extract just the `age` column using slicing.
4. In your own words (a code comment is fine), explain why standard
   deviation is usually reported instead of variance.

## Challenge

Given a list of `(x, y)` data points that roughly follow a line, try a few
different `slope`/`intercept` values in `linear_equation()` and compute the
total squared difference between your predicted `y` values and the actual
`y` values for each guess (`sum((predicted - actual) ** 2)`). Whichever
guess gives the smallest total is your best fit "by hand" — this is
exactly the quantity (called "loss" or "error") that real linear
regression algorithms minimize automatically.

## Mini Project

Using the sales data from `15-working-with-data`, compute the mean and
standard deviation of the `amount` column (with NumPy) and use them to
flag any transaction more than 1 standard deviation above the mean as
"high spending" — a simple, real technique used constantly in practice for
spotting outliers.

## Summary

Vectors and matrices are just Python lists/2D arrays, viewed through an
ML lens (rows = examples, columns = features). Mean/variance/standard
deviation describe a dataset's center and spread. A linear equation
(`y = mx + b`) is the simplest example of "fitting a model to data" — the
core idea behind a huge portion of machine learning. None of this requires
new math beyond what's shown here to get started.

## Next Step

Continue to [`06-python-habits-for-ai-ml.md`](06-python-habits-for-ai-ml.md).
