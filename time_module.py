## Time Module in Python 
# Time.time() - returns time from a fixed date
# A particular use - difference between start and end to calculate the running time of a function 


## Time Module - provides a lot of functions to play with time in python 



import time
curr = time.time()
print("Current time in seconds since epoch =", curr)

curr1 = time.ctime(curr)
print("Current time:", curr1)

# time.sleep() - to delay the execution of a program 