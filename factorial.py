
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    
    result = 1
 
    for i in range(1, n + 1):
        result = result * i
    
    return result

number = 5
fact = factorial(number)
print("Factorial of", number, "is:", fact)