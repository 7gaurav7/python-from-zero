"""
Solutions for 12 - Modules and Packages
Try the exercises yourself first! (exercises/12_modules_and_packages_exercises.py)
"""
import math
import random
from datetime import date

# 1. circle area
radius = 5
area = math.pi * radius ** 2
print(area)

# 2. simulate 5 coin flips
for _ in range(5):
    print(random.choice(["Heads", "Tails"]))

# 3. current year only
print(date.today().year)

# 4. see string_helpers.py and string_helpers_demo.py in this folder
# for the palindrome-module exercise.

# 5. shuffle a list of names
names = ["Alice", "Bob", "Carla", "Dan", "Ema"]
random.shuffle(names)
print(names)

# Challenge 1: see calculator_module.py and calculator_module_demo.py
# in this folder for the reusable calculator module exercise.

# Challenge 2: lottery number generator
lottery_numbers = random.sample(range(1, 50), 6)
print(sorted(lottery_numbers))
