"""
Topic 09 - Functions
Runnable examples matching the README.
"""

# Example 1: a simple function
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")
# Expected output:
# Hello, Alice!
# Hello, Bob!


# Example 2: returning a value
def add(a, b):
    return a + b


result = add(3, 4)
print(result)
# Expected output: 7


# Example 3: default parameters
def greet_with_default(name="friend"):
    print(f"Hello, {name}!")


greet_with_default()
greet_with_default("Charlie")
# Expected output:
# Hello, friend!
# Hello, Charlie!


# Example 4: scope
def set_score():
    score = 100  # local variable, only exists inside this function
    print("Inside function:", score)


set_score()
# print(score)  # this would raise: NameError: name 'score' is not defined
# Expected output: Inside function: 100
