"""
Topic 02 - Input and Output
These examples use input(), so run them yourself in a terminal
to see them interact with your typed answers.
"""

# Example 1: basic input and output
name = input("What is your name? ")
print("Hello,", name)

# Example 2: converting input to a number
age_text = input("How old are you? ")   # "25", a string
age = int(age_text)                     # 25, an integer
print("Next year you'll be", age + 1)

# Example 3: f-strings
name = "Bob"
age = 30
print(f"{name} is {age} years old.")
# Expected output: Bob is 30 years old.

# Example 4: doing math with two inputs
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"The sum is {a + b}")
