#include <stdio.h>

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

int main() {
    int choice;
    double a, b;

    printf("Simple C Calculator\n");

    while (1) {
        printf("\nChoose an operation:\n");
        printf("1. Add\n");
        printf("2. Subtract\n");
        printf("3. Multiply\n");
        printf("4. Divide\n");
        printf("5. Exit\n");
        printf("Enter a number (1-5): ");

        if (scanf("%d", &choice) != 1) {
            printf("Invalid input\n");
            return 1;
        }

        if (choice == 5) {
            printf("Goodbye.\n");
            break;
        }

        if (choice < 1 || choice > 5) {
            printf("Invalid choice\n");
            continue;
        }

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
        }
    }

    return 0;
}
