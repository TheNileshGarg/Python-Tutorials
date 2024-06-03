## Multiple Inheritance - A feature of object oriented programming that allows you to inherit 
# attributes and methods from multiple parent classes 

# In case of multiple inheritance, if a method is defined in two parent classes and not overriden, 
# Preference is given to method of class inherited first 

# mro - it tells you the preference order of methods for a class. 

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class CanFly:
    def __init__(self):
        self.flying_speed = 10

    def fly(self):
        print(f"{self.name} is flying at {self.flying_speed} km/h.")

class Bird(Animal, CanFly):
    def __init__(self, name, species, flying_speed):
        Animal.__init__(self, name)  
        CanFly.__init__(self)      
        self.species = species
        self.flying_speed = flying_speed  
        # you cant use super anymore, you need name of parent class and you have to pass self 

    def info(self):
        print(f"{self.name} is a {self.species}.")

    def fly(self):
        print(f"{self.name} is a {self.species}.")
        super().fly()  # Call the fly method from CanFly
        # here you can use super() as it is only defined in catfly

    def eat(self):
        print(f"{self.name}, the {self.species}, is eating gracefully.")

# Example usage
eagle = Bird("Eagle", "Golden Eagle", 50)
eagle.info()    # Outputs: Eagle is a Golden Eagle.
eagle.eat()     # Outputs: Eagle, the Golden Eagle, is eating gracefully.
eagle.fly()     # Outputs: Eagle is a Golden Eagle.
                #          Eagle is flying at 50 km/h.

# super automatically takes the object, using class name you need to have self parameter for it.