"""
statistics.py

This file contains simple statistical operations that can be used by the
calculator or any future tools in the project. These functions focus on
basic descriptive statistics and are written to be easy to understand
and reliable for general use.
"""

def mean(values):
    """
    Return the average of a list of numbers.
    If the list is empty, return a message instead of raising an error.
    """
    if not values:
        return "Cannot compute the mean of an empty list"
    return sum(values) / len(values)


def median(values):
    """
    Return the median of a list of numbers.
    If the list is empty, return a message instead of raising an error.
    """
    if not values:
        return "Cannot compute the median of an empty list"

    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def minimum(values):
    """
    Return the smallest number in a list.
    If the list is empty, return a message instead of raising an error.
    """
    if not values:
        return "Cannot compute the minimum of an empty list"
    return min(values)


def maximum(values):
    """
    Return the largest number in a list.
    If the list is empty, return a message instead of raising an error.
    """
    if not values:
        return "Cannot compute the maximum of an empty list"
    return max(values)
