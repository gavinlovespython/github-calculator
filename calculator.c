#include <stdio.h>
#include <math.h>

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    if (b == 0) {
        printf("Cannot divide by zero\n");
        return 0;
    }
    return a / b;
}

double power(double a, double b) {
    return pow(a, b);
}

double square_root(double value) {
    if (value < 0) {
        printf("Cannot take the square root of a negative number\n");
        return 0;
    }
    return sqrt(value);
}

double absolute_value(double value) {
    return value < 0 ? -value : value;
}

int main() {
    int category;

    printf("Simple C Calculator\n");

    while (1) {
        printf("\nChoose a category:\n");
        printf("1. Basic operations\n");
        printf("2. Advanced operations\n");
        printf("3. Exit\n");
        printf("Enter a number (1-3): ");

        if (scanf("%d", &category) != 1) {
            printf("Invalid input\n");
            return 1;
        }

        if (category == 3) {
            printf("Goodbye.\n");
            break;
        }

        if (category == 1) {
            int choice;
            double a, b;

            printf("\nBasic operations:\n");
            printf("1. Add\n");
            printf("2. Subtract\n");
            printf("3. Multiply\n");
            printf("4. Divide\n");
            printf("Enter a number (1-4): ");
            scanf("%d", &choice);

            printf("Enter the first number: ");
            scanf("%lf", &a);
            printf("Enter the second number: ");
            scanf("%lf", &b);

            switch (choice) {
                case 1:
                    printf("Result: %.2f\n", add(a, b));
                    break;
                case 2:
                    printf("Result: %.2f\n", subtract(a, b));
                    break;
                case 3:
                    printf("Result: %.2f\n", multiply(a, b));
                    break;
                case 4:
                    printf("Result: %.2f\n", divide(a, b));
                    break;
                default:
                    printf("Invalid choice\n");
            }
        }

        if (category == 2) {
            int choice;
            double a, b;

            printf("\nAdvanced operations:\n");
            printf("1. Power (a^b)\n");
            printf("2. Square root\n");
            printf("3. Absolute value\n");
            printf("Enter a number (1-3): ");
            scanf("%d", &choice);

            if (choice == 1) {
                printf("Enter the base: ");
                scanf("%lf", &a);
                printf("Enter the exponent: ");
                scanf("%lf", &b);
                printf("Result: %.2f\n", power(a, b));
            } else if (choice == 2) {
                printf("Enter a number: ");
                scanf("%lf", &a);
                printf("Result: %.2f\n", square_root(a));
            } else if (choice == 3) {
                printf("Enter a number: ");
                scanf("%lf", &a);
                printf("Result: %.2f\n", absolute_value(a));
            } else {
                printf("Invalid choice\n");
            }
        }
    }

    return 0;
}
