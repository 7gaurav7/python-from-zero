"""
20 - AI/ML Preparation: NumPy Fundamentals
Runnable examples matching the lesson.
Requires: pip install numpy
"""
import numpy as np

# Example 1: creating an array and inspecting it
numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.shape)
print(numbers.dtype)

# Example 2: element-wise arithmetic (no loop needed)
numbers = np.array([1, 2, 3, 4])
print(numbers * 2)
print(numbers + 10)
print(numbers ** 2)
# Expected output:
# [2 4 6 8]
# [11 12 13 14]
# [ 1  4  9 16]

# Example 3: indexing, slicing, and boolean filtering
scores = np.array([55, 90, 72, 88, 40])
print(scores[1])
print(scores[1:3])
print(scores[scores >= 70])
# Expected output:
# 90
# [90 72]
# [90 72 88]

# Example 4: quick statistics
print(scores.sum())
print(scores.mean())
print(scores.max())
print(scores.min())
# Expected output:
# 345
# 69.0
# 90
# 40
