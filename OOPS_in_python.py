## Object Oriented Programming 

# The Idea of OOPS is to use classes and objects to represent real world concepts and entities 

# Say in language of GTA 
# player is an entity 
# it has health, guns, location and or info
# we can also perform operations on player
# say if he got hit, we will reduce his/ her health 

# city can be another class 

# Say we have 100 enemies 
# would we create 100*x variables and track them 
# Rather, If we declare a template using class i.e using Object Oriented approach 


# Class - Blueprint 
# Object - entity 

#A class is a blueprint or template for creating objects. 
#It defines the properties and methods that an object of that class will have. 
#Properties are the data or state of an object,
#and methods are the actions or behaviors that an object can perform.

#An object is an instance of a class, and it contains its own data and methods.
#For example, you could create a class called "Person" that has properties such as 
#name and age, and methods such as speak() and walk(). 
#Each instance of the Person class would be a unique object with its own name and age,
#but they would all have the same methods to speak and walk.

# It enables abstraction, encapsulation, inheritance, polymorphism 

## OOPS - helps us map real world entities in programming 



## Creating a class 

class Person:
    name = "Jake"
    profession = "Engineer"
    networth = 10000000
    
    def info(self):
        print(f"{self.name} is a {self.profession}")
a = Person()
a.name = "Peter"
a.profession = "Financer"
a.networth = 500000
print(a.name, a.profession)
a.info()

# Using a class method, you can easily manipulate an object of that class. 
# You dont have to play with variables, pass them as arguments and do messy stuff 
# Classes make it more organized 

# self - A reference to the current instance of a class and is used to access variables belonging to 
# the class 

# You can create as many objects using a class as you like 


## Constructors in Python 
# Constructor - A method to create a class object 
# A constructor is automatically called once an object is created 

class Student:

    def __init__(self, name, gpa, major):
        self.name = name 
        self.gpa = gpa
        self.major = major
        #print("Hey I am a student")
    
    def info(self):
        print(f"Hey, My Name is {self.name}. I am {self.major} student. My GPA is {self.gpa}.")

jake = Student("jake", 3.2, "CS")
yu = Student("Yu", 3.5, "ECE")
# Constructor is always called when an object is created 
jake.info()
yu.info()
# To a class method, object is automatically passed as an argument to self. 
# It's better that it's automatic. as purpose of instance methods is to perform operations on instance
print()
# Default constructor - one that does not take any arguments from object and has only self as parameter
# Parameterized constructor - one that takes in multiple arguments 

 
## Decorators in python 
# Decorator - A tool to modify behaviour of functions and methods 
# They extend functionality of function or method without modifying the source code 
# A decorator is a special function which takes functions as an argument and returns 
# a new function that modifies behaviour of original function 


def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
    return mfx 

@greet
def hello():
    print("Hello World")

# Greet is decorating function 
# Decorator is technically a synatic sugar for performing a modification 
# it is same as greet(hello)()

hello()
# Technically, Decorators just increase readability 

# One common use of decorators is to add logging to the function. 
# It is better to call function directly having a decorator attached to it 
# Rather than having to call a function by passing function 

# You can create a decorator function once and then use it on multiple functions. 

## Getters and Setters in Python 

# Getter - A method in python to access the values of an object's properties. 
# They return the value of a specific property and are defined using @property decorator 

class my_class:
    def __init__(self, value):
        self._value = value

    def info(self):
        print(f"My value is {self._value}.")

    @property
    def ten_value(self):
        return 10*self._value

    @ten_value.setter
    def ten_value(self, value):
        self._value = value / 10 
        
obj = my_class(10)
obj.info()
print(obj.ten_value)
obj.ten_value = 56
obj.info()
print(obj.ten_value)

#Getters and setters are methods used in classes to control access to private variables.
#A getter retrieves the value of a private variable, while a setter updates it,
#allowing you to add validation or processing logic when the value is accessed or modified.


#In a banking application, a `BankAccount` class might use a private variable for the account balance.
#A getter method allows clients to check the balance, and 
#a setter method ensures that only valid transactions (like deposits or withdrawals) can change the balance, 
#preventing invalid or unauthorized changes.

# Basically, you can add validation when a person is trying to access or change value of a variable 

# @property - setter 
# @variable_name.setter



## Inheritance

# Using an existing class to create a new class 
# When a class derives from another class, child class will inherit all the public and 
# protected properties and methods from the base class 
# In addition it can have it's own methods 


class Employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id 
    def show_details(self):
        print(f"The name of employee {self.id} is {self.name}.")
    
class Programmer(Employee):
    def tell_specialisation(self):
        print("My Specialization is Software Engineering")

emp1 = Employee("Jake", 342)
emp1.show_details()
# emp1.tell_specialisation() will not work 

prog1 = Programmer("Peter", 90)
prog1.tell_specialisation()

# Programmer can be inherited further too in case of any doubts 
# We have single inheritance, multiple inheritance, and multilevel inheritance.


## Access Modifiers in Python 

# In Python, Nothing is public, private and protected 

# In General, Access Modifiers are used to limit the access of class variables and class methods
# outside the class while implementing concepts of inheritance 


# All methods and variables in python are by default public 
# Any instance variable in python followed by self key word is by default public. 

# By definition, private members of a class are those memebers are those members 
# which are only accesssible inside the class. 
# Python does not have a concept of strict private access modifiers 
# You can still access these variables however putting double underscore before variable name 
# gives a weak indication that a variable should be considered private 

class customer:

    def __init__(self, name, id, password, gpa):
        self.name = name
        self.id = id 
        self.__password = password
        self._gpa = gpa

c1 = customer("John", 23, 5665, 3.7)

print(c1.name, c1.id)
#print(c1.__password)
# You can not access c1.__password directly 
print(c1._customer__password)
print(c1.__dir__())

# Name Mangling - A Technique in python used to protect class attributes and superclass attributes 
# from being accidently overwritten by subclasses 

## Protected Access Modifier 
print(c1._gpa)
# It can be accessed directly, no mangling 
# _ is just a naming convention. It does not enforce anything. 


'''Important Python does not have a concept of private, protected and public. It is just 
a convention/ indication for fellow programmers.'''


# A Doubt 
'''Isn't getter setter a better way than private variables which are not technically private in python ? '''
'''Yes, getters and setters offer a better way to manage 
access and modification of variables in Python. 
Although Python's convention of prefixing variables with an underscore (e.g., `_variable`) 
indicates they are private, 
this does not enforce strict access control. 
Getters and setters provide a formalized method for encapsulating data,
allowing you to add validation and control while still maintaining a clean interface. 
This helps ensure data integrity and enhances maintainability.'''

