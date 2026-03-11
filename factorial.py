"""
Task 1: Calculate Factorial Using Recursion

This program asks the user to enter a number and calculates
its factorial using a recursive function.
"""

def factorial(n):
    """
    Calculates the factorial of a number using recursion.

    Parameters:
    n (int): The number whose factorial will be calculated

    Returns:
    int: Factorial of the number
    """

    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)


try:
    # Ask the user for input
    num = int(input("Enter a number to calculate factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print("Factorial of", num, "is:", result)

except ValueError:
    print("Invalid input! Please enter an integer.")