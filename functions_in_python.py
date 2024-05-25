# Functions in python 

# We basically label a block of code under a name 
# Using that name, we can use this block of code 
# This increases reusability, also it makes it easier to edit a piece of code
# It makes code look nicer 

def hcf(a,b):
    if a > b:
        while(b!=0):
            a,b = b,a % b
        return a 
    else:
        while(a != 0):
            b, a = a, b % a
        return b 
    
print(hcf(21,21))

def lcm():
    pass 
# pass is used to define function later without having error in code 

# Python provides a lot of built in functions 

## Arguments in Python 

# Parameters with default arguments come after parameters without arguments 

def asf (a, b):
    pass 

asf(b = 1, a = 2)

# You may use parameters as keys  in case you do not want to pass arguments in order

# * - to pass variable number of arguments as a list 

def total(*numbers):
    sum = 0
    for i in numbers:
        sum += i 
    return sum 
# Returns a value to call of function and function call is closed 
print(total(1,2,3,4,5))

# You can also pass arguments as a dictionary i.e key value pair arguments 

def intro(**val):
    print("Hi I am", val["name"], ". I am", val["age"], "years old.")

intro(name = "John", age = 31)