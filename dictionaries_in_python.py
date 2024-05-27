## Dictionaries in python 

dic = {"Leo" : "Lion", "Tommy" : "Dog", "Missy" : "Cat"}

print(dic["Leo"])
# Dictionary is a collection of key value pairs

employee_id = {"Jimmy" : 56, "Cartel" : 89, "Gary" : 67}

# From python 3.7, Dictionaries have become ordered. Previously, Dictionaries were unordered.

# Accessing single values 
print(employee_id["Jimmy"])
print(employee_id.get("Jimmy"))

# print(employee_id["James"])
print(employee_id.get("James")) # gives None 
# accessing using square brackets gives errors whereas using get method does not give errors 

# Accessing keys and using keys to get values 
print(employee_id.keys(), type(employee_id.keys()))

for key in employee_id.keys():
    print(key, employee_id[key])

# Accessing key value pairs 
for key, value in employee_id.items():
    print(key, value)

# Examples - student : marks, object : price, name : price 

cars = {"Model X" : 900, "Cayman" : 1000, "Buggatti": 3000, "Lamborghini": 2500}
# cars mapped to engine horsepower 

cars.update({"Model X" : 1200})
print(cars)
# update method updates the value if key is present else it creates a new key value pair 

# dic.clear() - to clear the dictionary 

print(cars.pop("Lamborghini"))
# removes key value pair and also returns it's value 

# pop_item - removes the last/ latest key value pair 
# del - deletes the dictionary, not empty but complete deal 
# You can also use del method to delete a key value pair but i would say why so use pop rather 


# While creating a website using django or flask, dictionaries are used a lot 
# Also used in APIs 
# Database also have methods which are similar to dictionary methods 
