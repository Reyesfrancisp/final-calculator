# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide, exponentiation, modulus  # Import the calculator functions

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.
    """
    result = subtract(a, b)
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.
    """
    result = multiply(a, b)
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.
    """
    result = divide(a, b)
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'exponentiation' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),           # Test positive exponent
        (-2, 3, -8),         # Test negative base with odd exponent
        (2, 0, 1),           # Test zero exponent
        (9, 0.5, 3.0),       # Test fractional exponent (square root)
        (2, -1, 0.5),        # Test negative exponent
    ],
    ids=[
        "positive_exponent",
        "negative_base_odd_exponent",
        "zero_exponent",
        "fractional_exponent",
        "negative_exponent",
    ]
)
def test_exponentiation(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'exponentiation' function with various combinations of integers and floats.
    """
    result = exponentiation(a, b)
    assert result == expected, f"Expected exponentiation({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'modulus' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 1),          # Test regular modulus
        (10, 5, 0),          # Test perfect multiple (zero remainder)
        (3, 10, 3),          # Test smaller dividend than divisor
        (5.5, 2, 1.5),       # Test float modulus
    ],
    ids=[
        "regular_modulus",
        "perfect_multiple",
        "smaller_dividend",
        "float_modulus",
    ]
)
def test_modulus(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'modulus' function with various combinations of integers and floats.
    """
    result = modulus(a, b)
    assert result == expected, f"Expected modulus({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Cases
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.
    """
    with pytest.raises(ValueError) as excinfo:
        divide(6, 0)
    assert "Cannot divide by zero" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero', but got '{excinfo.value}'"


def test_modulus_by_zero() -> None:
    """
    Test the 'modulus' function with modulo by zero.
    """
    with pytest.raises(ValueError) as excinfo:
        modulus(6, 0)
    assert "Cannot modulo by zero" in str(excinfo.value), \
        f"Expected error message 'Cannot modulo by zero', but got '{excinfo.value}'"