#include <stdio.h>

int main() {
    int a, b, temp;

    // Input values
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    // Print before swapping
    printf("Before swapping: a = %d, b = %d\n", a, b);

    // Swapping logic
    temp = a;
    a = b;
    b = temp;

    // Print after swapping
    printf("After swapping: a = %d, b = %d\n", a, b);

    return 0;
}
