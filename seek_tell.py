# seek and tell are used to work with file objects and their positions within a file 

with open("file_1.txt", "r") as f:
    print(type(f))
    # f is io.TextIOWrapper type object 
    f.seek(10)
    data = f.read(5)
    print(data)
    # seek function moves the cursor to a specific position within the file 
    print(f.tell())
    # returns the current position of cursor in file 

# truncate function - to truncate the characters in file to a specific size 

with open("write_1.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)

with open("write_1.txt", "r") as f:
    d = f.read()
    print(d)