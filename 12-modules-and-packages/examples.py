"""
Topic 12 - Modules and Packages
Runnable examples matching the README.
"""

import math
import random
from datetime import date

# Example 1: using the math module
print(math.sqrt(25))
print(math.pi)
print(math.ceil(4.1))
print(math.floor(4.9))
# Expected output:
# 5.0
# 3.141592653589793
# 5
# 4

# Example 2: using the random module (output varies each run)
dice_roll = random.randint(1, 6)
print("You rolled:", dice_roll)

# Example 3: from ... import ...  (output varies by date)
today = date.today()
print("Today is:", today)

# Example 4: creating and importing your own module
# See helpers.py in this same folder, then run helpers_demo.py
