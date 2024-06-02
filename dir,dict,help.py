x = [1,2,3]
print(dir(x))
# Returns all the methods and attributes associated with an object including 
# dunder methods 

class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age 
        self.sex = sex 


p = Person("Jerry", 12, "Male")
print(p.__dict__)
# returns all attributes and their values as a dictionary 

print(help(str))
print(help(Person))

# help gives us information about class, class method and anything