## Single Inheritance - Type of inheritance where child class inherits behaviours and properties from 
# only single parent class 
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
class Cat(Animal):
        def __init__(self, name, breed):
            super().__init__(name, "cat")
            self.breed = breed
        def make_sound(self):
            print("Meow!")
        def info(self):
            print(f"{self.name} is a cat of {self.breed} species.")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

c = Cat("Tommy", "Siamese")
c.make_sound()
c.info()



