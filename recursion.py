# Recursion 

# factorial(6) = 6*5*4*3*2*1 
# factorial(0) = 1

# n > 0 -> factorial(n) = n*n-1*....*1 

## factorial(n) = n*factorial(n-1) 
# Using above info, We can recursively calculate factorials 

def factorial(n):
    if n < 0:
        return "Not Defined"
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
print(factorial(6))
print(factorial(7))

# This program works like this 

# say calculating factorial(5)
# it will go 5*factorial(4)
# which leads to 5*4*factorial(3)
# which leads to 5*4*3*factorial(2)
# which leads to 5*4*3*2*factorial(1)
# which leads to 5*4*3*2*1 
# giving us 120.

# We can basically do recursion for any program where 
# return value for parameter n is dependent on any value from 0 to n-1. 

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))