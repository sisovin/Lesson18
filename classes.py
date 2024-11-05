# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:51:46 2024

@author: chien
"""

from turtle import title
from functools import reduce


print("")
title = " Chapter 18 - Classes & Objects in classes.py "
print(f"{title}".upper().center(80, "="))
print("")

title = " # fundamental concepts in object-oriented programming (OOP): # "
print(f"{title}".center(80, "#"))

# 1. Class: a blueprint for creating objects
class Vehicle: # class name
    def __init__(self, make, model, year): # constructor
        self.make = make # attributes
        self.model = model # attributes
        self.year = year # attributes
    
    def moves(self): # methods
        print(f"Moves along..") # methods
        
    def get_make_model(self): # methods
        return f"I'm a{self.make} {self.model}" # methods
      
my_car = Vehicle("Tesla", "Model 3", 2021) # object

print(my_car.make) # accessing attributes
print(my_car.model) # accessing attributes
my_car.get_make_model() # accessing methods
my_car.moves() # accessing methods

print("")
title = " # Attributes and Properties: # "
print(f"{title}".center(80, "#"))
class Person: # Class
    def __init__(self, name, age): # Constructor
        self.name = name  # Attribute
        self._age = age   # Attribute (with leading underscore to indicate it's intended to be private)

    # Property for age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Using attributes
person = Person("Sisovin", 52) # Creating an object of the Person class with name and age
print(person.name)  # Accessing attribute directly
person.name = "Bob"  # Modifying attribute directly
print(person.name)

# Using properties
print(person.age)  # Accessing property
person.age = 35    # Modifying property with validation
print(person.age)

try:
    person.age = -5  # Attempting to set an invalid value
except ValueError as e:
    print(e)  # Output: Age cannot be negative

print("")
title = " # Inheritance: # "
print(f"{title}".center(80, "#"))

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def moves(self):
        print(f"Moves along..")
        
    def get_make_model(self):
        return f"I'm a {self.make} {self.model}"

class Airplane(Vehicle): # Inheritance
    def __init__(self, make, model, year, faa_id): # constructor
        super().__init__(make, model, year) # call parent constructor
        self.faa_id = faa_id # additional attribute

    def moves(self): # override method
        print('Flies along..') # override method

class Truck(Vehicle): # Inheritance
    def moves(self): # override method
        print('Rumbles along..') # override method

class GolfCart(Vehicle): # Inheritance
    pass # no additional attributes or methods

# Corrected object instantiation
cessna = Airplane('Cessna', 'Skyhawk', 2021, 'N-12345') # object
mack = Truck('Mack', 'Pinnacle', 2020) # object
golfwagon = GolfCart('Yamaha', 'GC100', 2019) # object

print(cessna.get_make_model()) # accessing methods
cessna.moves() # accessing methods
print(mack.get_make_model()) # accessing methods
mack.moves() # accessing methods
print(golfwagon.get_make_model()) # accessing methods
golfwagon.moves() # accessing methods

print('\n\n') # blank lines

# Assuming my_car and your_car are defined somewhere in the code
# For demonstration, let's define them here
my_car = Vehicle('Toyota', 'Corolla', 2018)
your_car = Vehicle('Honda', 'Civic', 2017)

for v in (my_car, your_car, cessna, mack, golfwagon): # loop through objects
    print(v.get_make_model()) # call method
    v.moves() # call method

# 2. Object: a collection of data (variables) and methods (functions) that act on the data

class Vehicle1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def moves(self):
        print(f"Moves along..")
        
    def get_make_model(self):
        return f"I'm a {self.make} {self.model}"

# Creating multiple objects of the Vehicle class
car1 = Vehicle1("Tesla", "Model 3", 2021)
car2 = Vehicle1("Ford", "Mustang", 2020)
car3 = Vehicle1("Chevrolet", "Camaro", 2019)

# Accessing attributes and methods of each object
print(car1.get_make_model())
car1.moves()

print(car2.get_make_model())
car2.moves()

print(car3.get_make_model())
car3.moves()