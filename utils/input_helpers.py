"""
input_helpers.py

This module contains a set of helper functions that make it easier to collect
and validate user input. The goal is to keep the main calculator code simple
while giving you a reliable place for all input related logic.

The file includes:
- number parsing
- integer parsing
- menu selection helpers
- yes or no prompts
- range validation
- formatted error messages
- internal parsing helpers
- general purpose input utilities
"""


# ------------------------------------------------------------
# Number input helpers
# ------------------------------------------------------------

def get_number(prompt):
    """
    Ask the user for a number and keep asking until the input is valid.
    Returns a float.
    """
    while True:
        raw = input(prompt)
        parsed = _try_parse_float(raw)

        if parsed is not None:
            return parsed

        print("Please enter a valid number.")


def get_integer(prompt):
    """
    Ask the user for an integer and keep asking until the input is valid.
    Returns an int.
    """
    while True:
        raw = input(prompt)
        parsed = _try_parse_int(raw)

        if parsed is not None:
            return parsed

        print("Please enter a valid integer.")


# ------------------------------------------------------------
# Menu helpers
# ------------------------------------------------------------

def get_choice(prompt, valid_choices):
    """
    Ask the user to pick from a list of valid string choices.
    Returns the chosen string.
    """
    valid_set = set(valid_choices)

    while True:
        choice = input(prompt).strip()
        if choice in valid_set:
            return choice

        print("Invalid choice. Try again.")


def get_indexed_choice(prompt, options):
    """
    Show a numbered list of options and return the index the user selects.
    """
    if not options:
        raise ValueError("Options list cannot be empty.")

    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        raw = input("Enter a number: ")
        parsed = _try_parse_int(raw)

        if parsed is None or not (1 <= parsed <= len(options)):
            print("Invalid selection. Try again.")
            continue

        return parsed - 1


# ------------------------------------------------------------
# Yes or no helpers
# ------------------------------------------------------------

def get_yes_no(prompt):
    """
    Ask the user a yes or no question.
    Returns True for yes and False for no.
    """
    yes = {"y", "yes", "yeah", "yep", "ok", "sure"}
    no = {"n", "no", "nope", "nah"}

    while True:
        raw = input(prompt).strip().lower()

        if raw in yes:
            return True
        if raw in no:
            return False

        print("Please answer yes or no.")


# ------------------------------------------------------------
# Range validation
# ------------------------------------------------------------

def validate_range(value, min_value=None, max_value=None):
    """
    Check if a number falls within a given range.
    Returns True if valid.
    """
    if min_value is not None and value < min_value:
        return False
    if max_value is not None and value > max_value:
        return False
    return True


def get_number_in_range(prompt, min_value=None, max_value=None):
    """
    Ask the user for a number that must fall within a specific range.
    """
    while True:
        value = get_number(prompt)

        if validate_range(value, min_value, max_value):
            return value

        if min_value is not None and max_value is not None:
            print(f"Please enter a number between {min_value} and {max_value}.")
        elif min_value is not None:
            print(f"Please enter a number greater than or equal to {min_value}.")
        elif max_value is not None:
            print(f"Please enter a number less than or equal to {max_value}.")
        else:
            print("Invalid number.")


# ------------------------------------------------------------
# Message helpers
# ------------------------------------------------------------

def print_error(message):
    """Print a simple error message."""
    print(f"[ERROR] {message}")


def print_warning(message):
    """Print a simple warning message."""
    print(f"[WARNING] {message}")


def print_info(message):
    """Print a simple informational message."""
    print(f"[INFO] {message}")


# ------------------------------------------------------------
# Internal parsing helpers
# ------------------------------------------------------------

def _try_parse_float(value):
    """Try to convert a string to a float. Returns None if it fails."""
    try:
        return float(value)
    except ValueError:
        return None


def _try_parse_int(value):
    """Try to convert a string to an int. Returns None if it fails."""
    try:
        return int(value)
    except ValueError:
        return None


# ------------------------------------------------------------
# General purpose helpers
# ------------------------------------------------------------

def get_non_empty_string(prompt):
    """
    Ask the user for a non empty string.
    Keeps asking until the input is not blank.
    """
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


def confirm_action(action_name):
    """
    Ask the user to confirm an action by name.
    Returns True if confirmed.
    """
    return get_yes_no(f"Are you sure you want to {action_name}? ")


def pause(message="Press Enter to continue..."):
    """
    Pause the program until the user presses Enter.
    """
    input(message)
