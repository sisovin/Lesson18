# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien 
"""

from turtle import tilt


tilt = " Chapter 17 - Lambda & Higher Order Functions in main.py "
print(f"{tilt}".upper().center(80, "="))
print("")
tilt = " # Access and modify the attributes of an object: # "
print(f"{tilt}".center(80, "#"))

from classes import Vehicle, Person

# Creating an object of the Vehicle class
my_car = Vehicle("Tesla", "Model 3", 2021)

# Accessing attributes
print(my_car.make)
print(my_car.model)
print(my_car.year)

#Modifying attributes
my_car.year = 2022
print(my_car.year)

person = Person("Sovanny", 51)
print(person.name)
print(person.age)

# Adding a new attribute dynamically
person.sex = "female"

print("")
person.name = "Sovanny Ou"
person.age = 52

print(person.name) # Output: Sovanny Ou
print(person.age) # Output: 52
print(person.sex) # Output: 'female'
print(f"Person's dictionary: {person.__dict__}") # Output: {'name': 'Sovanny Ou', 'age': 52, 'sex': 'female'}


print(person.sex)  # Output: 'female'

# Deleting the attribute
del person.sex

# Trying to access the deleted attribute will raise an AttributeError
try:
    print(person.sex)
except AttributeError:
    print("The attribute 'sex' has been deleted.")

print(f"Person's dictionary after deletion: {person.__dict__}")  # Output: {'name': 'Sovanny Ou', 'age': 52}

# Check if the attribute exists
if hasattr(person, 'sex'):
    print("The attribute 'sex' exists.")
else:
    print("The attribute 'sex' does not exist.")

print("")
tilt = " # Access and modify the attributes of a class: # "
print(f"{tilt}".center(80, "#"))
# Creating an instance of the Person class
person = Person("Sovanny", 51)

# Adding a new attribute dynamically
setattr(person, 'sex', 'female')

# Accessing the new attribute dynamically
print(getattr(person, 'sex'))  # Output: 'female'

# Modifying the new attribute dynamically
setattr(person, 'sex', 'male')

# Accessing the modified attribute dynamically
print(getattr(person, 'sex'))  # Output: 'male'

# Checking if the attribute exists
if hasattr(person, 'sex'):
    print("The attribute 'sex' exists.")
else:
    print("The attribute 'sex' does not exist.")

# Deleting the attribute
delattr(person, 'sex')

# Checking if the attribute exists after deletion
if hasattr(person, 'sex'):
    print("The attribute 'sex' exists.")
else:
    print("The attribute 'sex' does not exist.")