"""
16 - Testing and Debugging: Debugging Fundamentals
Runnable examples matching the lesson.
"""


# Example 1: using print() to inspect a variable's value
def calculate_total(prices):
    total = 0
    for price in prices:
        print("DEBUG: price =", price, "running total =", total)
        total += price
    return total


print(calculate_total([10, 20, 30]))
# Expected output:
# DEBUG: price = 10 running total = 0
# DEBUG: price = 20 running total = 10
# DEBUG: price = 30 running total = 30
# 60


# Example 2: narrowing down where a bug lives
def process(numbers):
    doubled = [n * 2 for n in numbers]
    print("DEBUG: doubled =", doubled)
    total = sum(doubled)
    print("DEBUG: total =", total)
    average = total / len(numbers)
    return average


print(process([1, 2, 3]))
# Expected output:
# DEBUG: doubled = [2, 4, 6]
# DEBUG: total = 12
# 4.0


# Example 3: comparing expected vs. actual directly
def add(a, b):
    return a - b  # bug: should be a + b


result = add(2, 3)
expected = 5
print(f"Expected {expected}, got {result}")
# Expected output: Expected 5, got -1


# Example 4: isolating a problem by commenting out code
def suspicious_function(x):
    step1 = x + 1
    # step2 = 1 / (x - x)   # commented out while isolating a ZeroDivisionError
    return step1


print(suspicious_function(5))
# Expected output: 6
