from operations.basic import add, subtract, multiply, divide
from operations.advanced import power, square_root, absolute_value
from operations.statistics import mean, median, minimum, maximum

from utils.input_helpers import (
    get_number,
    get_integer,
    get_choice,
    get_yes_no,
    get_non_empty_string
)

from utils.formatting import format_result, format_operation


def main():
    print("Simple GitHub Calculator")

    while True:
        print("\nChoose a category:")
        print("1. Basic operations")
        print("2. Advanced operations")
        print("3. Statistics")
        print("4. Exit")

        category = get_choice("Enter a number (1-4): ", ["1", "2", "3", "4"])

        if category == "4":
            print("Goodbye.")
            break

        if category == "1":
            handle_basic()
        elif category == "2":
            handle_advanced()
        elif category == "3":
            handle_statistics()


def handle_basic():
    print("\nBasic operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = get_choice("Enter a number (1-4): ", ["1", "2", "3", "4"])

    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    if choice == "1":
        result = add(a, b)
        print(format_operation("Addition", a, b, result))
    elif choice == "2":
        result = subtract(a, b)
        print(format_operation("Subtraction", a, b, result))
    elif choice == "3":
        result = multiply(a, b)
        print(format_operation("Multiplication", a, b, result))
    elif choice == "4":
        result = divide(a, b)
        print(format_operation("Division", a, b, result))


def handle_advanced():
    print("\nAdvanced operations:")
    print("1. Power (a^b)")
    print("2. Square root")
    print("3. Absolute value")

    choice = get_choice("Enter a number (1-3): ", ["1", "2", "3"])

    if choice == "1":
        a = get_number("Enter the base: ")
        b = get_number("Enter the exponent: ")
        result = power(a, b)
        print(format_operation("Power", a, b, result))

    elif choice == "2":
        value = get_number("Enter a number: ")
        result = square_root(value)
        print(f"Square root of {value} = {format_result(result)}")

    elif choice == "3":
        value = get_number("Enter a number: ")
        result = absolute_value(value)
        print(f"Absolute value of {value} = {format_result(result)}")


def handle_statistics():
    print("\nStatistics operations:")
    print("1. Mean")
    print("2. Median")
    print("3. Minimum")
    print("4. Maximum")

    choice = get_choice("Enter a number (1-4): ", ["1", "2", "3", "4"])

    count = get_integer("How many numbers will you enter? ")

    values = []
    for i in range(count):
        num = get_number(f"Enter number {i + 1}: ")
        values.append(num)

    if choice == "1":
        result = mean(values)
        print(f"Mean = {format_result(result)}")
    elif choice == "2":
        result = median(values)
        print(f"Median = {format_result(result)}")
    elif choice == "3":
        result = minimum(values)
        print(f"Minimum = {format_result(result)}")
    elif choice == "4":
        result = maximum(values)
        print(f"Maximum = {format_result(result)}")


if __name__ == "__main__":
    main()
