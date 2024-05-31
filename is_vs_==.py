# is vs == in python 

# a = list()
# b = a 
# changing a will change b too 
# for collection based data structures 

a = 4 
b = 4 

print(a is b) # exact location of object in memory 
print(a == b) # compares value of two objects 

# Python is using same memory for both of the objects 

a1 = [1, 2, 3, 4]
b1 = [1, 2, 3, 4]
print(a1 is b1)
print(a1 == b1)

# == compares value, is compares memory locations 
