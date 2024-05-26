# Tuples - Similar to list but immutable 

tup = (1, 2, 3, "sd")
print(tup)
print(type(tup))

print("---- Single Value Tuple ----")
tup1 = (1)
print(type(tup1))
tup2 = (1,)
print(type(tup2))

# Tuples are basically used when you want an immutable order collection of data items 

print(tup[0])
print(tup[1])
# Tuples are 0 indexed 

if 2 in tup:
    print("Yes")
else:
    print("No")

print(tup[1:3])
# A new sliced tuple is returned 

# Negative indexing is allowed in tuples 

print(tup[-1])


## Tuple Methods 

# You can not directly manipulate tuple . You create a list from tuple, manipulate it 
# Using this modified list, you create a new tuple 

tu = (11, 13, 14)
lis = list(tu)
lis.append(16)
lis.append(19)
tu = tuple(lis)
print(tu)

print(tu.count(11))
print(tu.index(19))
# count - counts number of occurences of that element 
# index - returns index of first occurence of that element 

# You can also search for index in a particular range in tuple 
# tuple.index(element, start, end)

print(len(tu))