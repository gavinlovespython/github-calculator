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
    """Return the result of dividing a by b. Handles division by zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def main():
    """Simple command-line interface for the calculator."""
    print("Simple GitHub Calculator")

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter a number (1-5): ")

        if choice == "5":
            print("Goodbye.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers")
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))


if __name__ == "__main__":
    main()
