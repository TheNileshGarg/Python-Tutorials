# Map, Filter, Reduce 

# Map, Filer, Reduce are built in functions that allow you to apply a function to a sequence and
# return a new sequence

def cube(x):
    return x*x*x 

l = [1, 2, 3, 4, 5, 6, 7, 8] 

# newl = []

# for el in l:
#     newl.append(cube(el))

newl = list(map(cube, l))
print(newl)
# map - applies a function to each element of sequence and return a new sequence containing 
# transformed elements 

def fil_func(x):
    if x % 2 == 0:
        return True 
    else:
        return False 
    
fil_list = list(filter(fil_func, l))
print(fil_list)

# filter - this function filters a functions based on predicate (a function returning true / false) 
# value and returns a sequence containing those elements which meet the predicate 
# Sequence can be list, tuple or any iterable object


from functools import reduce 
# reduce(function, iterable)
# reduce function applies a function to a sequence and returns a single value 

# function argument here takes a function which takes two value and returns a single one 

mysum = reduce(lambda x, y : x + y, l)
print(mysum)

myproduct = reduce(lambda x, y: x*y, l)
print(myproduct)

# Reduce starts using first two elements and then uses returned elemnt and next element and so on 
