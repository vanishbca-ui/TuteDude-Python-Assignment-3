import math
num = float(input("Enter a number: "))

if num <= 0:
    print("Square root and logarithm only work for positive numbers.")
else:
    sqrt_value = math.sqrt(num)
    
    log_value = math.log(num)
    
    sine_value = math.sin(num)
    
    print("Square root:", sqrt_value)
    print("Natural logarithm:", log_value)
    print("Sine value:", sine_value)