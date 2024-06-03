## A Doubt 
## Why domnt we pass self to super method() whenever we call a function but use it to 
# when you call same method through parent class name.

#No self needed: super() returns a proxy object bound to the correct instance,
#so self is implicitly passed.

#No self needed: super() returns a proxy object bound to the correct instance, 
#so self is implicitly passed.



## Multilevel Inheritance - When a child class inherits from another derived class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

dog = GoldenRetriever("Max", "Golden")
dog.show_details()
# We first calling Dog's show_details which in turns calls Animal's show details first. 