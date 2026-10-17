"""
16 - Testing and Debugging: unittest Basics
Runnable examples matching the lesson.

Each example builds its test suite explicitly with TestLoader/TextTestRunner
so several independent examples can run back-to-back in one script. In your
own test files, the simpler `unittest.main()` at the bottom (see the lesson)
is all you need.
"""
import unittest


def run(test_case_class, label):
    print(f"--- {label} ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    unittest.TextTestRunner(verbosity=1).run(suite)


# Example 1: a basic passing test
def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_adds_two_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)


run(TestAdd, "Example 1")


# Example 2: multiple test methods in one class
def is_even(n):
    return n % 2 == 0


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(5))


run(TestIsEven, "Example 2")


# Example 3: testing that an exception is raised
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


class TestDivide(unittest.TestCase):
    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


run(TestDivide, "Example 3")


# Example 4: using setUp for shared setup
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        self.items.append(name)


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()  # fresh cart before every test

    def test_starts_empty(self):
        self.assertEqual(len(self.cart.items), 0)

    def test_add_item(self):
        self.cart.add_item("Apple")
        self.assertIn("Apple", self.cart.items)


run(TestShoppingCart, "Example 4")
