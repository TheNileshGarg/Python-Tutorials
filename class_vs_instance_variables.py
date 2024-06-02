## Class Varibles and Instance Variables

# One of advantages of OOPS is we are able to logically group things together. 

# You can not use instance methods which does not have self as a parameter 
# as while calling an instance method, instance is passed as an argument 


class Employee:
    company = "Tesla"
    def __init__(self, name, role):
        self.name = name 
        self.role = role 
    def show_details(self):
        print(f"Employee Name : {self.name} \nEmployee Role : {self.role}")
    
jake = Employee("Jake", "Assembly Engineer")
jake.show_details()
rahul = Employee("Rahul", "Mechanic")
rahul.show_details()
selena = Employee("Selena", "Designer")
selena.show_details()
# company is a class variable 
print(f"Jake's Company : {jake.company}")
print(f"Rahul's Company : {rahul.company}")
# Company is same for all instances of Employee 

jake.company = "Tesla Austin"
# It creates an instance variable rather than changing class variable
print(f"Jake's Company : {jake.company}")
# While printing, we give priority to instance variable over class variable 
print(f"Rahul's Company : {rahul.company}")

Employee.company = "Lucid"
print(f"Jake's Company : {jake.company}")
print(f"Rahul's Company : {rahul.company}")

# Example - no of employees will be a class variable (for an Employee class)
# In a game, no of enemies will be a class variable, 
# fps will be a class variable and so on. 

# An Employee can't have no of employees , it's for company/ class say.