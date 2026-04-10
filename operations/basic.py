"""
basic.py

This file contains the core math operations used by the calculator.
These functions are simple and reliable and form the foundation of
the calculator's behavior.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Return the result of dividing a by b.
    If b is zero, return a message instead of raising an error.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b
