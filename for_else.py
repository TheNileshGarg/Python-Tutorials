for i in range(10):
    print(i)
else:
    print("Else block entered")

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Else block entered")

# In case we encounter a break statement during loop execution, We break out of loop. 
# Commands under else block are not executed in this case. as we never reach it . 
# Else block is executed if loop ends not if it gets broken 

# We can also use else statement along with while loop 
# In case of while loop too, it is executed only if loop executes naturally and is not broken
