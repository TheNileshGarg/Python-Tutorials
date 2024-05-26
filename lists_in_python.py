# Lists in Python 

# Lists - Organize data items in an ordered manner 

marks = [79, 34, 89, 93]

print(marks[0])
print(marks[1])
 
# Lists are created by putting comma seperated items in square brackets 

# List can have different data types of elements in it 

li = ["Harry", 76, 90, True, ["tu","uo"]]
print(li)

# List is 0 indexed 
# List also supports negative indexing 

# L[-i] = L[len(L) - i]
# Or basically negative indexing is reversing the list and assuming it to be 1 indexed
# Though cnvinient way is to understand it in terms of positive indexing 

# To check if an element is in list 

if "Harry" in li:
    print("Harry is present")
else:
    print("Harry is absent")

# Same concept is applicable to strings too 

# We also have concept of slicing in list 
# List_name[start, stop, sep] 
# stop index is not included 

# List Comprehension 

l = [i*i for i in range(5)]
print(l)

l1 = [i*i*i for i in range(10) if i % 2 == 0]
print(l1)

## List Methods 

l2 = [1,2,3]
l2.append("Chris")
print(l2)

l3 = [11,2,33,43,23]
l3.sort(reverse= True)
# sorts the existing list and returns none, order depends on reverse parameter 
print(l3)
print(l3.index(11))

print(l3.count(23))
# count method returns frequency of an element in the list 

l4 = [1,3,4,5,7,9]
l5 = l4
l5[0] = 2
print(l4)
print(l5)
# Both l1 and l2 get changed as l2 and l1 are basically referring to the same list 

# Better way is to use copy function 

l6 = l5.copy()
l6[1] = 100
print(l5)
print(l6)

l7 = l6.insert(2,300)
# to insert an element at a particular index

m1 = ["Jack", "Jane", "Chris"]
m2 = ["Robert", "Natasha"]

print(m2.extend(m1))

# Extend - to add elements from a list to another list 

# There are many more methods. I have listed the more commonly used ones 