"""
Solutions for 05 - Loops
Try the exercises yourself first! (exercises/05_loops_exercises.py)
"""

# 1. print 1 to 10
for i in range(1, 11):
    print(i)

# 2. even numbers 1 to 20
for i in range(2, 21, 2):
    print(i)

# 3. countdown from 10 to 1, then Liftoff!
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")

# 4. sum of 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# 5. guess a fixed secret number
secret = 7
guess = None
while guess != secret:
    guess = int(input("Guess the number: "))
print("Correct!")

# Challenge 1: multiplication table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Challenge 2: triangle pattern
size = 5
for row in range(1, size + 1):
    print("*" * row)
