## File Handling in Python 

# Opening a file in python 

f = open("a_file.txt","r")
#print(f)
text = f.read()
print(text)
f.close()
print()
# We give two arguments to the open function 
# 1st - file path 
# 2nd - mode in which we want to open file 

# Default argument for mode is read 
 
# Writing in a file 
# When you open a file in write mode and write something in it 
# You overwrite it's entire content. 

f1 = open("write_file.txt","w")
f1.write("Hello World \n")
f1.close()

# To append to the file instead of over writing, we use append mode 
# We use "a" as argument for append mode 

f2 = open("write_file.txt", "a")
f2.write("Hello World \n")
f2.close()

# It's important to close the file once you are done with it so as to free the resources and the file


# The code underneath automatically closes the file once you use it 
with open("write_file.txt", "r") as f:
    con = f.read()
    print(con)

# File handling is essential once you have to start storing data from your programs 


## ReadLine and ReadLines Method 

f = open("a_file.txt", "r")

while True:
    line = f.readline()
    if not line:
        break
    print(line, end = '')
print()
f.close()
# it reads each line as a string 

# Readlines method - it reads the file as a list of strings 

with open("a_file.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    lines = ''.join(lines)
    print(lines)

# Writelines 
# It writes a sequence of lines into file 
# Write lines does not automatically add \n to the strings. You have to do it manually 