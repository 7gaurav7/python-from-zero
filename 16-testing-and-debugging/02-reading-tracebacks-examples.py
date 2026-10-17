"""
16 - Testing and Debugging: Reading Tracebacks
Runnable examples matching the lesson.
Examples 1 and 2 are wrapped in try/except here so the whole file can run
top to bottom -- try commenting out the try/except to see the raw
traceback Python produces.
"""

# Example 1: a simple, single-frame traceback
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print("IndexError caught:", e)


# Example 2: a multi-function call chain
def total(numbers):
    return sum(numbers)


def get_average(numbers):
    return total(numbers) / len(numbers)


try:
    print(get_average([]))
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)

# Example 3: catching and inspecting an exception's message
try:
    age = int("abc")
except ValueError as e:
    print("Caught an error:", e)
# Expected output: Caught an error: invalid literal for int() with base 10: 'abc'


# Example 4: identifying "my bug" vs. "bad input"
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero -- that's expected user-input territory,")
        print("not a bug in the code itself.")
        return None


print(safe_divide(10, 0))
