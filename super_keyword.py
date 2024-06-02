## Super Keyword 

# When a class inheits from another class, 
# You can override or extend the methods in child class 
# However, you also wanna use methods from parent class 
# super keyword helps accomplishes the same thing 

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def info(self):
        print(f"I am {self.name}. I am {self.age} years old.")
    
class student(person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age)
        self.school = school
        self.grade = grade 
    def info(self):
        super().info()
        print(f"I am a {self.grade} grade student at {self.school}.")

s = student("Jake", 12, "Joseph Mary School", "6th")
p = person("William", 17)
s.info()
p.info()

# We did overwrite the methods of class but we also used methods from parent class. 