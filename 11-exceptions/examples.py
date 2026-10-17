"""
Topic 11 - Exceptions
Runnable examples matching the README.
"""

# Example 1: catching a ValueError
try:
    age_text = "abc"  # normally this would come from input()
    age = int(age_text)
    print(f"You are {age} years old.")
except ValueError:
    print("That's not a valid number!")
# Expected output: That's not a valid number!

# Example 2: catching a ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
# Expected output: You can't divide by zero!

# Example 3: multiple except blocks
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("That index doesn't exist.")
except ValueError:
    print("Invalid value.")
# Expected output: That index doesn't exist.

# Example 4: else and finally
try:
    number = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion succeeded:", number)
finally:
    print("Done trying.")
# Expected output:
# Conversion succeeded: 42
# Done trying.
