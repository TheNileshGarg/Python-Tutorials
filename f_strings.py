# f string 
# Used for string formatting 

# It's technically best way to use variables in a string 

name = "Jake"
age = 19 

print("Hi I am {}. I am {} years old.".format(name, age))
# You could definitely use this but f strings is simply more covinient as variable is placed in place.

print(f"Hi I am {name}. I am {age} years old.")

price = 99.9901
print(f"This items costs {price: .2f} dollars.")

# Messing with f string 
print(f"Hi , My name is {{name}}")