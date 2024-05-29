x = 5
print(x)

def jake():
    # x = 10 - without global x it creates a new local variable x 
    global x 
    x = 10 
    print("The value of local x is", x)
    print("Jake called")

print("The value of global x is", x)
jake()
print("The value of global x is", x)
# Local variables - variables created within a function and only accessible within that function 
# created when function is called and destroyed when function returns 

# global variable defined outside function and is accessible within any function in code 


## global keyword 
# you are using global variable in the function 

# You have to use global variable in python to change value of a global variable 
# otherwise it just creates a new local variable 


# Just a reminder, arguments to python are passed by copying 
