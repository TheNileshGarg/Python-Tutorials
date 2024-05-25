# Loops in python 

# Loops - Repeat a task till a certain condition is met 

# if you want to print 1 to say 20000, you cant really write it manually 

# for loop in python accesses each element in an iterable object 
name = "Joyce"

for a in name:
    print(a, end = ', ')
print()

l = ['Katie', 'Joyce', 'Ella', 'Isabella']

for a in l:
    print(a)

for a in range(1,5):
    print(a)

for a in range(1,12,3):
    print(a)
# you are accesing every 3rd index from the current index 


# while loop 
# usually we use while loop when we do not know the exact number of times we need to execute 
# it is more of based on condition 
inp = None
while True:
    try:
        inp = int(input("Enter a number "))
        break 
    except:
        print("Please enter a valid integer")

# Here we did not know in how many tries will user enter correct input 

# while else 
# code block under else statement with while loop is executed only if no break statement occurs 

# We do not have do and while statements in python 



# break and continue statements in python 

# continue - to skip execution of a particular iteration 

# break - come out of loop irrespective of loop condition 

# Printing all non factors of i using continue statement 
i = int(input("Enter a positive number : "))
for a in range(1,i+1):
    if i % a == 0:
        continue
    else:
        print(a)

# using while true - you can emulate a do while loop 
