# When you want to execute a block of code based on value of a variable 

a = int(input("First Number "))
b = int(input("Second Number "))

print("1. a + b \n2. a - b \n3. a * b\n4. a / b")
ch = int(input("Enter Your Choice "))

match ch:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Wrong Choice")