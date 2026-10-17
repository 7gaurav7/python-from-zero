"""
Topic 03 - Operators
Runnable examples matching the README.
"""

# Example 1: arithmetic operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 2)
# Expected output:
# 13
# 7
# 30
# 3.3333333333333335
# 3
# 1
# 100

# Example 2: comparison operators
print(5 == 5)
print(5 != 3)
print(5 > 10)
# Expected output:
# True
# True
# False

# Example 3: logical operators
age = 20
has_id = True
print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
# Expected output:
# True
# True
# False

# Example 4: assignment shortcuts
score = 10
score += 5
print(score)
score *= 2
print(score)
# Expected output:
# 15
# 30
