# a = True 
print(a := False)

# Walrus Operator - Added in python 3.8 
# Allows you to assign a value to a variable within an expression 
# Used in while loops and if statements 

a = [1,2,3,4,5]
while (n := len(a)):
    print(a.pop())
# Value of n is used in while loop 

#  This can be useful when you need to use a value multiple times in a loop,
# but don't want to repeat the calculation.

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
# here we append user's desired item to list of food unless he inputs quit. 


# It is important to note that the Walrus Operator 
#should be used sparingly as it can make code less readable if overused.
