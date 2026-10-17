"""
Solutions for 01 - Variables and Data Types
Try the exercises yourself first! (exercises/01_variables_exercises.py)
"""

# 1. name, age, height
name = "Alice"
age = 25
height = 1.68
print(name)
print(age)
print(height)

# 2. sum of two numbers
a = 10
b = 15
print(a + b)

# 3. is_raining
is_raining = False
print(is_raining, type(is_raining))

# 4. reassign to a different type
value = 5
print(type(value))
value = "five"
print(type(value))

# 5. total price of three items
item1 = 9.99
item2 = 4.50
item3 = 12.25
print(item1 + item2 + item3)

# Challenge 1: swap using a temp variable
a = 1
b = 2
print("Before:", a, b)
temp = a
a = b
b = temp
print("After:", a, b)

# Challenge 2: rectangle area/perimeter
width = 4
height = 6
area = width * height
perimeter = 2 * (width + height)
print("Area:", area)
print("Perimeter:", perimeter)
