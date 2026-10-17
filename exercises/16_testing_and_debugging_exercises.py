"""
Exercises for 16 - Testing and Debugging
Each section matches one lesson file in 16-testing-and-debugging/.
Write your code below each numbered comment.
"""

# --- 01: Debugging Fundamentals ---
# 1. Write a function with a deliberate bug (e.g. an off-by-one loop), and
#    use print() statements to locate the exact line responsible. Leave
#    your debug prints in as comments once you've found it.


# --- 02: Reading Tracebacks ---
# 2. Write code that deliberately raises a TypeError (e.g. adding a string
#    and a number). Run it and, in a comment, write down the error type,
#    message, file, and line number from the traceback.


# 3. Write a 3-function call chain (A calls B calls C) where C raises an
#    error. Practice tracing the full path through the traceback.


# --- 03: Assertions ---
# 4. Write calculate_discount(price, percent) with an assert checking
#    percent is between 0 and 100.


# 5. Write three assert statements checking a multiply(a, b) function
#    against known correct results.


# --- 04: unittest Basics ---
# 6. Write a unittest test class for an is_even(n) function, covering an
#    even number, an odd number, and zero.


# 7. Write a test using assertRaises for a function that should raise
#    ValueError on invalid input.


# --- 05: Introduction to pytest ---
# 8. Write a test_math.py-style set of two plain assert-based pytest test
#    functions for a function of your choice (you can write them in this
#    file; just don't wrap them in a class).


# 9. Write a pytest fixture that returns a list of sample data, and two
#    test functions that use it.


# --- Challenges (pick a few) ---
# C1. Write a full unittest test class (5+ methods) for the Student class
#     from 13-oop, covering average() and letter_grade() at boundaries.
# C2. Rewrite one of your unittest tests as a plain pytest-style function.
