def format_result(value):
    """Format a calculation result for display."""
    if isinstance(value, str):
        return value  # error messages stay as-is

    # Remove trailing .0 for whole numbers
    if value == int(value):
        return str(int(value))

    # Otherwise return a clean float
    return f"{value:.2f}"


def format_operation(name, a, b, result):
    """Return a clean string describing the operation performed."""
    return f"{name} of {a} and {b} = {format_result(result)}"
