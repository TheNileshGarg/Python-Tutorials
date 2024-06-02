## Static Methods 
# Methods that belong to a class rather than an instance of a class 
# They are neither called on class itself nor on instance of class 
# Often used to create utility functions that do not need an instance of class 

# Why keep static method in class ?
# Because I want to ship the method with the class 

# You can call this method using class_name.func_name()
# instance_name.func_name()


class MathOperations:
    # A static method for adding two numbers
    @staticmethod
    def add(x, y):
        return x + y

    # A static method for subtracting two numbers
    @staticmethod
    def subtract(x, y):
        return x - y

    # A static method for multiplying two numbers
    @staticmethod
    def multiply(x, y):
        return x * y

    # A static method for dividing two numbers
    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

# Usage of static methods
print("Addition:", MathOperations.add(10, 5))       # Outputs: Addition: 15
print("Subtraction:", MathOperations.subtract(10, 5)) # Outputs: Subtraction: 5
print("Multiplication:", MathOperations.multiply(10, 5)) # Outputs: Multiplication: 50
print("Division:", MathOperations.divide(10, 5))     # Outputs: Division: 2.0
print("Division by zero:", MathOperations.divide(10, 0)) # Outputs: Division by zero: Cannot divide by zero

#Static methods are useful when you want to include functionalities related to a class, 
#but those functionalities don't require access to the instance-specific data. 
#They allow users to perform complex operations using the class itself, 
#without needing to instantiate it.