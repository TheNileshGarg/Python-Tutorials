marks = [23, 45, 56, 79, 98, 70, 89]

index = 0
for mark in marks:
    print(mark)
    if(index == 4):
        print("Awesome Jake")
    index += 1 

# Better Way 

for index, mark in enumerate(marks):
    print(mark)
    if index == 4:
        print("Awesome Jake")

# Enumerate - Loop over list, string, tuple at the time and return index and value at the same time 

# You can also pass in an argument to start from a different index 

