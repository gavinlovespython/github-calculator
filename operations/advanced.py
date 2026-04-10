"""
advanced.py

This file contains more advanced math operations that go beyond the
basic functions. These are optional but useful additions that make
the calculator feel more complete.
"""

import math

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def square_root(value):
    """
    Return the square root of a number.
    If the number is negative, return a message instead of an error.
    """
    if value < 0:
        return "Cannot take the square root of a negative number"
    return math.sqrt(value)

def absolute_value(value):
    """Return the absolute value of a number."""
    return abs(value)
