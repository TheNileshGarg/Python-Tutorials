# String - Text data enclosed between single or double quotes 

# Use \" to add quotations within a string 
# """ """ or ''' ''' - For mutiline strings while writing 
# on console for multiline we use \n 

name = "Jonathan"
print(name[0])

# In python, strings are 0 indexed 
# In python, string is immutable i.e name[1] = 'A' not allowed

# To access each char of string 

for a in name:
    print(a, end = ' ')
print("")

# loop - a process that runs continously till we get an exit condition 

## String Slicing 

names = "Alex, Jones, Harry, Jack"
print(names[0:4])
# In slicing [start, stop) , you may add a seperator 
# last index is not included 


# -1 index - last index i,e len - 1 
print(len(name))
print(len(names))
# len function gives the length of string 
print(name[-3::2])

# -1 in string slicing/ indexing means len(s) - 1 

## String Methods 

n = "Nicholas"

print(len(n))
print(n.upper())
print(n.lower())
# creates a new string in upper/ lower case rather than modifying previous 

# lstrip, rstrip, strip -> removes trailing characters/ spaces 


a1 = "!!!!Nick!!!!"
a2 = "   Jenny   "

print(a1.strip("!"))
print(a2.strip())

a3 = "Cherry is the king of england. He is also king of ireland"

print(a3.replace("king","queen"))

# split - create a list from a string 
# basically each piece of text seperated by sep becomes element of list 

a5 = "i am a GooD BoY"
print(a5.capitalize())

# center - aligns string to the center 

print(a5.count("king"))
# count a substring in a string 

a6 = "ttpp .."
print(a6.endswith("."))

print(a5.find("GooD"))
# returns index of first occurence of the given value if present else -1 is returned 

# isalnum, islower, isupper, isalpha - such methods are used to check what our strings are 
# istitle - returns true only if first letter of eacxh word is capitalized 

a7 = "I Am A Good Boy"
print(a7.istitle())