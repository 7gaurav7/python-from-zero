"""
20 - AI/ML Preparation: Math Foundations for ML
Runnable examples matching the lesson.
Requires: pip install numpy
"""
import numpy as np

# Example 1: mean, variance, and standard deviation, by hand
values = [10, 12, 23, 23, 16, 23, 21, 16]

mean = sum(values) / len(values)
variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = variance ** 0.5

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard deviation: {std_dev:.2f}")
# Expected output:
# Mean: 18.0
# Variance: 27.5
# Standard deviation: 5.24

# Example 2: the same calculation using NumPy
values_arr = np.array(values)
print(values_arr.mean())
print(values_arr.var())
print(values_arr.std())
# Expected output:
# 18.0
# 27.5
# 5.244044240850758


# Example 3: a linear equation as a Python function
def linear_equation(x, slope, intercept):
    return slope * x + intercept


for x in range(5):
    print(x, "->", linear_equation(x, slope=2, intercept=1))
# Expected output:
# 0 -> 1
# 1 -> 3
# 2 -> 5
# 3 -> 7
# 4 -> 9

# Example 4: representing tabular data as vectors (rows)
students = np.array([
    [2, 1],
    [5, 3],
    [8, 5],
])
print(students.shape)
print(students[:, 0])
# Expected output:
# (3, 2)
# [2 5 8]
