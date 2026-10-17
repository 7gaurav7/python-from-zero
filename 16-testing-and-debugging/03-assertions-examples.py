"""
16 - Testing and Debugging: Assertions
Runnable examples matching the lesson.
Example 2 is wrapped in try/except so the whole file can run top to
bottom without stopping -- try removing the try/except to see the raw
AssertionError.
"""


# Example 1: a passing assertion (nothing visible happens)
def calculate_average(numbers):
    assert len(numbers) > 0, "Cannot average an empty list"
    return sum(numbers) / len(numbers)


print(calculate_average([10, 20, 30]))
# Expected output: 20.0

# Example 2: a failing assertion
try:
    print(calculate_average([]))
except AssertionError as e:
    print("AssertionError caught:", e)


# Example 3: asserting an internal invariant while developing
def apply_discount(price, discount_percent):
    new_price = price * (1 - discount_percent / 100)
    assert new_price >= 0, "Discount made the price negative -- logic bug!"
    return new_price


print(apply_discount(100, 20))
# Expected output: 80.0


# Example 4: using assertions to check a function's behavior
def square(n):
    return n ** 2


assert square(3) == 9
assert square(-4) == 16
assert square(0) == 0
print("All assertions passed!")
