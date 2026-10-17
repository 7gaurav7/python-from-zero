"""
Solutions for 11 - Exceptions
Try the exercises yourself first! (exercises/11_exceptions_exercises.py)
"""

# 1. safely ask for a number
try:
    value = int(input("Enter a number: "))
    print(f"You entered {value}")
except ValueError:
    print("That's not a valid number!")

# 2. safe division
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print(a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 3. handle a missing file
try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file doesn't exist.")

# 4. handle a missing dictionary key
person = {"name": "Sam"}
try:
    print(person["age"])
except KeyError:
    print("That key doesn't exist.")

# 5. keep asking until a valid number is given
while True:
    try:
        number = int(input("Enter a whole number: "))
        break
    except ValueError:
        print("Invalid input, try again.")
print(f"Got it: {number}")

# Challenge 1: robust calculator function
def calculate(a, b, operator):
    try:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        else:
            print("Unknown operator.")
            return None
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

print(calculate(10, 0, "/"))

# Challenge 2: convert strings to ints, skipping failures
def safe_convert_all(strings):
    result = []
    for s in strings:
        try:
            result.append(int(s))
        except ValueError:
            continue
    return result

print(safe_convert_all(["1", "two", "3", "4x", "5"]))
