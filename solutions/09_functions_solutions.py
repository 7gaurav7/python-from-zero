"""
Solutions for 09 - Functions
Try the exercises yourself first! (exercises/09_functions_exercises.py)
"""

# 1. square(n)
def square(n):
    return n ** 2

print(square(3), square(7))

# 2. is_even(n)
def is_even(n):
    return n % 2 == 0

print(is_even(4), is_even(7))

# 3. greet with default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")

# 4. average(numbers)
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))

# 5. celsius_to_fahrenheit(c)
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

print(celsius_to_fahrenheit(100))

# Challenge 1: is_prime(n)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17), is_prime(18))

# Challenge 2: find_duplicates(items)
def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))
