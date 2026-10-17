"""
Solutions for 03 - Operators
Try the exercises yourself first! (exercises/03_operators_exercises.py)
"""

# 1. 17 % 5 -- the remainder after dividing 17 by 5
print(17 % 5)  # 2, because 17 = 3*5 + 2

# 2. all arithmetic operators on a=7, b=2
a, b = 7, 2
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# 3. check if a number is even
number = 8
print(number % 2 == 0)

# 4. concert entry check
age = 20
has_ticket = True
print(age >= 16 and has_ticket)

# 5. total with -=, +=, *=
total = 100
total -= 20
print(total)
total += 5
print(total)
total *= 2
print(total)

# Challenge 1: minutes to hours and leftover minutes
total_minutes = 135
hours = total_minutes // 60
leftover_minutes = total_minutes % 60
print(f"{hours}h {leftover_minutes}m")

# Challenge 2: loan eligibility
age = 25
income = 28000
has_good_credit = True
eligible = age >= 21 and (income >= 30000 or has_good_credit)
print(eligible)
