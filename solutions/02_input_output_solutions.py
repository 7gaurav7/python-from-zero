"""
Solutions for 02 - Input and Output
Try the exercises yourself first! (exercises/02_input_output_exercises.py)
These use input(), so run interactively to see them work.
"""

# 1. personalized greeting
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

# 2. product of two numbers
a = float(input("First number: "))
b = float(input("Second number: "))
print(f"Product: {a * b}")

# 3. approximate age from birth year
birth_year = int(input("Birth year: "))
print(f"You are approximately {2026 - birth_year} years old.")

# 4. Celsius to Fahrenheit
celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"That's {fahrenheit} Fahrenheit.")

# 5. first/last name combined as "Last, First"
first = input("First name: ")
last = input("Last name: ")
print(f"{last}, {first}")

# Challenge 1: rectangle area/perimeter formatted to 2 decimals
length = float(input("Length: "))
width = float(input("Width: "))
print(f"Area: {length * width:.2f}")
print(f"Perimeter: {2 * (length + width):.2f}")

# Challenge 2: seconds to hours/minutes/seconds
total_seconds = int(input("Total seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours}h {minutes}m {seconds}s")
