## Method Overriding 

# Method Overriding is a feature of object overriding which allows you to provide
class Animal:
    def speak(self, word):
        print(f"{word} {word} {word}")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Cow(Animal):
    pass  # Cow doesn't override the speak method, so it inherits the one from Animal

# Create instances of each class
animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()
dog2 = Dog()
# Call the speak method on each instance
animal.speak("brr")  
dog.speak()     
cat.speak()    
cow.speak("cow")    
#dog2.speak("doggy") -> Does not work as method is overriden. No preference, you can only use child 
# class method. 