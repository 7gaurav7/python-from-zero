"""
16 - Testing and Debugging: Introduction to pytest

This file is written in pytest style (plain functions, bare `assert`,
`pytest.raises`, fixtures, and parametrize). It requires `pytest` to be
installed:

    pip install pytest

Then run it with:

    pytest 05-pytest-introduction-examples.py

It will NOT run correctly with plain `python3 05-pytest-introduction-examples.py`
or with unittest, since pytest provides the `pytest` module, the fixture
mechanism, and the test discovery/runner itself.
"""
import pytest


# Example 1: a plain pytest-style test
def add(a, b):
    return a + b


def test_adds_two_positive_numbers():
    assert add(2, 3) == 5


# Example 2: testing an exception with pytest.raises
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# Example 3: a fixture for shared setup
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        self.items.append(name)


@pytest.fixture
def sample_cart():
    return ShoppingCart()


def test_starts_empty(sample_cart):
    assert len(sample_cart.items) == 0


def test_add_item(sample_cart):
    sample_cart.add_item("Apple")
    assert "Apple" in sample_cart.items


# Example 4: parametrizing a test to check multiple inputs at once
def square(n):
    return n ** 2


@pytest.mark.parametrize("n, expected", [(2, 4), (3, 9), (-4, 16), (0, 0)])
def test_square(n, expected):
    assert square(n) == expected
