"""
Solutions for 04 - Conditions
Try the exercises yourself first! (exercises/04_conditions_exercises.py)
"""

# 1. positive, negative, or zero
number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 2. leap year check
year = 2024
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 3. child/teenager/adult
age = 16
if age <= 12:
    print("child")
elif age <= 19:
    print("teenager")
else:
    print("adult")

# 4. password strength
password = "abc123"
if len(password) >= 8:
    print("Strong enough")
else:
    print("Too short")

# 5. largest of three numbers
x, y, z = 4, 9, 7
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print(largest)

# Challenge 1: grading program
score = 82
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Challenge 2: triangle type
a, b, c = 5, 5, 8
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
