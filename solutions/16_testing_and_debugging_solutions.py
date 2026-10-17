"""
Solutions for 16 - Testing and Debugging
Try the exercises yourself first!
(exercises/16_testing_and_debugging_exercises.py)
"""
import unittest

# --- 01: Debugging Fundamentals ---


def sum_up_to(n):
    # Originally buggy version used range(1, n) which skips n itself.
    # Debug print (kept as a comment once the bug was found):
    # print("DEBUG: looping through", list(range(1, n + 1)))
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_up_to(5))  # 15


# --- 02: Reading Tracebacks ---
# "abc" + 5 raises:
#   TypeError: can't concatenate str (not "int") to str
# at the line "abc" + 5, in <module>, in this file.
# (Left commented out so this file still runs top to bottom.)
# result = "abc" + 5


def level_c():
    return 1 / 0


def level_b():
    return level_c()


def level_a():
    return level_b()


try:
    level_a()
except ZeroDivisionError:
    print("Caught the error from level_c(), three calls deep.")


# --- 03: Assertions ---
def calculate_discount(price, percent):
    assert 0 <= percent <= 100, "percent must be between 0 and 100"
    return price * (1 - percent / 100)


print(calculate_discount(100, 25))


def multiply(a, b):
    return a * b


assert multiply(2, 3) == 6
assert multiply(-1, 5) == -5
assert multiply(0, 100) == 0
print("All multiply checks passed!")


# --- 04: unittest Basics ---
def is_even(n):
    return n % 2 == 0


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_zero(self):
        self.assertTrue(is_even(0))


def parse_positive_int(text):
    value = int(text)
    if value < 0:
        raise ValueError("Value must be positive")
    return value


class TestParsePositiveInt(unittest.TestCase):
    def test_raises_on_negative(self):
        with self.assertRaises(ValueError):
            parse_positive_int("-5")


# --- 05: Introduction to pytest ---
# (pytest-style: plain functions, plain assert -- no class, no self.)


def add(a, b):
    return a + b


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def sample_data():
    return [1, 2, 3, 4, 5]


def test_sample_data_sum():
    assert sum(sample_data()) == 15


def test_sample_data_length():
    assert len(sample_data()) == 5


if __name__ == "__main__":
    unittest.main(argv=["ignored", "-v"], exit=False)
