## Exception Handling 

# Normally, If we get an error, Our program terminates. 
# But Do we want our program to get terminated due to a trivial error ?

# Say you dont get info from web once and your program with a huge trade terminates 
# Now you had to sell that, if you sold that after 2-3 sec lag you wont be in much trouble 
# but if it terminated lol, you may suffer loss for millions in an hour 

# Or say if amazon shut down due to an error 

# Also, you dont want your game to shut down if you press wrong key on your laptop

# Therefore it is important for us the programmers to handle errors 
ui = None
while True:
    try:
        ui = int(input("Enter a valid integer : "))
        break
    except Exception as e:
        print(e)
print(ui)

# You can also check for specific type of errors 
l = [1, 2, 3, 4, 5, 6]
try:
    print(l[9])
except IndexError:
    print("Index Out Of Bound")

# Zero Division Error, NameError, KeyError ... etc

# Finally clause 

try:
    l = [2,3,4,5,5]
    i = int(input("Enter the index of element you want to access : "))
    print(l[i])
except:
    print("An error occured")
# finally:
    # print("I am always executed")
print("I am always executed")

def func1():
    try:
        l = [2,3,4,5,5]
        i = int(input("Enter the index of element you want to access : "))
        print(l[i])
        return 1
    except:
        print("An error occured")
        return 0
    finally:
        print("I am always executed")
    #print("I am always executed")
print(func1())

# Statements under finally block are always executed before returning

# Finally is used in functions. Block of code under it is executed before returning the function call. 


## Custom Errors 

# Using raise statements, We can raise errors 
# Here, We want to terminate program if user does something unexpected 

# There are two things 
# In case we get something unexpected and we do not want to terminate 

# In case where we ourselves want to specify an error and terminate program 
# say user enters a value of 160 for age, We dont want to proceed for his voting procedure then 

age = int(input("Enter your age "))

# Assuming age <= 120 
if age > 120:
    raise ValueError("Please enter your correct age")
# you can raise memory error, name erro and so on . like you could search always 


# You can also make your own error class allowing you to raise more customized errors 
# class your_error_name (Exception):
#     pass
ui = input("Enter an integer between 5 and 9 ")
try:
    ui1 = int(ui)
    if ui1 < 5 or ui1 > 9:
        raise ValueError("Enter Number in Desired Range") 
except Exception as e:
    if ui.lower() == "quit":
        print("Exited.") 
    else:
        raise e