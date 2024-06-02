## Class Methods 

# Classes are used to built a template for objects 

class Employee:
    company = "Google"

    def show(self):
        print(f"The Name is {self.name} and the Company is {self.company}.")
    
    @classmethod
    def change_company(cls, new_comp):
        cls.company = new_comp
    
e1 = Employee()
e1.name = "Jake"
e1.show()
e1.change_company("Tesla")
e1.show()
print(Employee.company)
# If you did not specify that the method is a class method using decorator, 
# It would just take instance as argument and create an instance variable. 


## Class Methods as alternative constructors 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("Peter", 23000)
print(e1.name,e1.salary)

string = "Kent-12000"
e = Employee(string.split("-")[0], int(string.split("-")[1]))
print(e.name, e.salary)

# Imagine creating objects using strings for 10 empployees. Wont it become ugly 
# So we will add a class method to solve this problem. 

str2 = "Jenny-13000"
e2 = Employee.fromStr(str2)
print(e2.name, e2.salary)
# class method takes class as first input 


## Example - In Date Time Module, class methods are used to entertain different types of 
# input to instantiate objects. 