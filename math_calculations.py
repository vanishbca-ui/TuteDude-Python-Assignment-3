"""
Task 2: Using the Math Module for Calculations

This program asks the user for a number and calculates
square root, natural logarithm, and sine using the math module.
"""

import math

try:
    num = float(input("Enter a number: "))

    if num <= 0:
        print("Please enter a positive number.")
    else:
        print("Square root:", math.sqrt(num))
        print("Natural logarithm (log base e):", math.log(num))
        print("Sine of the number:", math.sin(num))

except ValueError:
    print("Invalid input! Please enter a numeric value.")