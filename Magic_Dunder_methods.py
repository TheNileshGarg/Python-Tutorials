## Magic Methods in python 
# Magic methods, also known as “dunders” from the double underscores surrounding their names, 
# are powerful tools that allow you to customize the behaviour of your classes.

# __init__ method
#The init method is a special method that is automatically invoked
#when you create a new instance of a class. 
#This method is responsible for setting up the object’s initial state, and it is 
#where you would typically define any instance variables that you need


#__str__ and __repr__ methods
#The str and repr methods are both used to convert an object to a string representation. 
#The str method is used when you want to print out an object, 
#while the repr method is used when you want to get a string representation of an object 
#that can be used to recreate the object.

#__len__ method
#The len method is used to get the length of an object. 

#__call__ method
#The call method is used to make an object callable, meaning that
#you can pass it as a parameter to a function and it will be executed when the function is called.


# We inherently used these methods without even knowing - abstraction hehe

class shop:
    def __init__(self,sales,expenditure):
        self.sales=sales
        self.expenditure=expenditure
    def __str__(self):
        return f"A class representing {self.sales} usd business."
    def __call__(self):
        print(f"The total profit is {self.sales-self.expenditure} usd")

shop1=shop(15000,12000)
print(shop1)
shop1()