# Docstring 
# String literal that appear just after declaration of function 
# basically, they help us in understanding the function 

def square(n):
    '''Takes a number n and returns it's square'''
    return n*n 
print(square(6))
print(square.__doc__)

# Docstring must be written immediately after function declaration else it is ignored as a comment 

# PEP - 8 
# Python Enhancement Proposal 

import this 
# Use this commmand and read it once you do few peojects 
# import this gives you Zen of Python