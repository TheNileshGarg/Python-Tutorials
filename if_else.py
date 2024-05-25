# if else 
# we use if else when you want to execute certain commands depending on whether a condition is true 

age = int(input("Please enter your age. "))

if age >= 18:
    print("You can drive")
else:
    print("You can not drive")

# Indentation is used to seperate a block of code 

a = int(input("First Number "))
b = int(input("Second Number "))
c = int(input("Third Number "))
print("Largest Number is :")
if(a > b):
    if(a > c):
        print("First Number", a)
    else:
        print("Third Number", c)
else:
    if(b > c):
        print("Second Number", b)
    else:
        print("Third Number", c)
# Assuming three numbers are different

num = int(input("Enter a number : "))
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number") 