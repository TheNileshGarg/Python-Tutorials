# Typecasting 

def string_to_int(a):
    try:
        return int(a)
    except:
        print("Please enter a valid value")
        return a 

print(type(string_to_int("11")))
print(type(string_to_int("Nick")))

# int(), str(), float(), list() ... functions for explicit typecasting 
# Explicit typecasting works only when it is possible/ compatible else python gives an error 

# Implicit Typecasting 

a = 1 
b = 2.342 

# Lowe order variable is converted to higher order in implicit type casting 

c = a + b # a is automatically converted to float and therefore we get c as float value 
print(c)
