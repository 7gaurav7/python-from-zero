"""
Topic 04 - Conditions
Runnable examples matching the README.
"""

# Example 1: basic if
age = 20
if age >= 18:
    print("You are an adult.")
# Expected output: You are an adult.

# Example 2: if / else
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Expected output: You are a minor.

# Example 3: if / elif / else
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
# Expected output: Grade: B

# Example 4: nested conditions
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Bring your ID next time.")
else:
    print("Entry denied: too young.")
# Expected output: Entry allowed.
