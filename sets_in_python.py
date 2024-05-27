# Sets in Python 

# Set - No duplicates, Only unique objects 
# Sets are unordered 
s = {2,2,2,4,4,4,5,5,99,9,9}
print(s)

s1 = {"Nick", 2,3,32, True, "Karla"}
print(s1)
# You can have multiple data types in a python set 

s2 = {}
s3 = set()
print(type(s2), type(s3))

# {} - creates empty dictionary and not an empty set 

# Accessing elements 
for a in s:
    print(a)

## Set Methods 

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9}

print("Union Set")
print(s1.union(s2))
print(s1, s2)
# We basicaly get a new set which is union of sets s1 and s2 
print("Updated S1 set")
s1.update(s2)
print(s1)
print(s1,s2)
# New set is assigned to s1 here 
# update does not return new set 

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9}

print("Intersection Set")
print(s1.intersection(s2))
print(s1, s2)

print("Intersection updated Set 1")
s1.intersection_update(s2)
print(s1)
print(s1, s2)

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9}

# Gives vaues which not common to both sets technically A + B - (A intersection B)
print("Symmetric Difference Set")
print(s1.symmetric_difference(s2))
print(s1, s2)

print("Symmetric Difference Updated Set 1")
s1.symmetric_difference_update(s2)
print(s1)
print(s1, s2)

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9}

# Gives values from original set not present in other set 
# technically A - (A intersect B)

print("Difference Set")
print(s1.difference(s2))
print(s1, s2)

print("Difference Updated Set 1")
s1.difference_update(s2)
print(s1)
print(s1, s2)

print("..............................")

s1 = {2,3,4,5,6}
s2 = {5,6,7,8,9}

print(s1.isdisjoint(s2))
# check if two sets are disjoint 

print(s1.issuperset(s2))
# checks if s1 is superset of s2 

print(s1.issubset(s2))
# checks if s1 is subset of s2 

print((s1.intersection(s2)).issubset(s2))
# s1 intersect s2 is obviously a subset of s2


# Unlike tuples, sets are mutable 

set1 = {"Tokyo", "Paris","London"}
print(set1)
set1.add("Seoul")

# remove, discard - remove throws error if item not present 
# discard - does not raise error if not present 

set1.remove("Tokyo")
print(set1)

# pop() - delete a random item from set and also return it 

#del(set1)
#print(set1)
# Now set1 is not defined after using del command 

if "Tokyo" in set1:
    print("Present")
else:
    print("Absent")