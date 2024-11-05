# Chapter 18 - Classes & Objects

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is Classes & Objects in Python?

Classes and objects are fundamental concepts in object-oriented programming (OOP) in Python.

- **Class**: A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Classes encapsulate data for the object and methods to manipulate that data.

- **Object**: An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created. Objects can have attributes (data) and methods (functions) that act on the data.

### Example

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing class attribute
print(my_dog.species)  # Output: Canis familiaris

# Accessing instance attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

# Calling instance methods
print(my_dog.description())  # Output: Buddy is 3 years old
print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof
```

In this example:

- `Dog` is a class with a class attribute `species`, instance attributes `name` and `age`, and instance methods `description` and `speak`.
- `my_dog` is an object (instance) of the `Dog` class.

## What are the differences of Attributes and Properties in Python?

In Python, attributes and properties are both used to store and manage the state of an object, but they have some key differences:

### Attributes

- **Attributes** are variables that belong to an instance or class.
- They are defined directly within the class and can be accessed using dot notation.
- Attributes can be modified directly without any control over the value being set.

### Properties

- **Properties** provide a way to add logic to attribute access.
- They are defined using the `property()` function or the `@property` decorator.
- Properties allow you to define methods that get, set, or delete an attribute, providing control over how the attribute is accessed and modified.
- They are useful for encapsulating data and adding validation logic.

### Example

Here is an example to illustrate the difference:

```python
class Person:
    def __init__(self, name, age):
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
person = Person("Alice", 30)
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
```

In this example:

- `name` is a simple attribute that can be accessed and modified directly.
- `age` is a property that adds validation logic to ensure the age cannot be set to a negative value. The `@property` decorator is used to define getter and setter methods for the `age` attribute.

## Object: a collection of data (variables) and methods (functions) that act on the data

Certainly! Here is the extracted definition of an object from the provided code structure:

```python
# Object: a collection of data (variables) and methods (functions) that act on the data
```

This line can be added to the code structure to provide a clear definition of what an object is in the context of object-oriented programming. Here is how you can integrate it:

````python
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

# Object: a collection of data (variables) and methods (functions) that act on the data

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

The error occurs because the [`Airplane`] class constructor requires four arguments ([`make`]), [`model`], [`year`], and [`faa_id`]), but only three were provided in the instantiation. The correct instantiation should include all four arguments.

Here is the corrected code:

```python
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
````

### Explanation

1. **Class Definitions**: Ensure the `Vehicle`, `Airplane`, `Truck`, and `GolfCart` classes are defined correctly.
2. **Object Instantiation**: Provide all required arguments when creating instances of the `Airplane`, `Truck`, and `GolfCart` classes.
3. **Method Calls**: Access methods and attributes of the created objects correctly.
4. **Loop Through Objects**: Ensure all objects in the loop are defined and instantiated correctly.

This should resolve the `TypeError` and ensure the code runs without issues.

## How can I access and modify the attributes of an object in Python?

class Car:
def **init**(self, make, model, year):
self.make = make
self.model = model
self.year = year

# Create an instance of the Car class

my_car = Car('Toyota', 'Corolla', 2020)

# Access attributes

print(my_car.make) # Output: Toyota
print(my_car.model) # Output: Corolla
print(my_car.year) # Output: 2020

# Modify attributes

my_car.year = 2021

# Verify the change

print(my_car.year) # Output: 2021

The issue arises because you are trying to add an attribute to an instance of the [`Person`] class using incorrect syntax. The correct way to add an attribute to an instance dynamically is by using dot notation directly on the instance.

Here is how you can do it:

### Correct Way to Add an Attribute Dynamically

```python
from classes import Vehicle, Person

# Creating an object of the Vehicle class
my_car = Vehicle("Tesla", "Model 3", 2021)

# Accessing attributes
print(my_car.make)
print(my_car.model)
print(my_car.year)

# Modifying attributes
my_car.year = 2022
print(my_car.year)

# Creating an object of the Person class
person = Person("Sovanny", 51)
print(person.name)
print(person.age)

# Adding a new attribute dynamically
person.sex = "female"
print(person.sex)
```

### Explanation

1. **Create an Instance**: Create an instance of the `Person` class.
2. **Add Attribute Dynamically**: Use `person.sex = "female"` to add the `sex` attribute to the `person` instance dynamically.
3. **Access the New Attribute**: Print the new attribute to verify it has been added.

This approach allows you to add new attributes to an instance of a class without modifying the class definition itself.

To delete an attribute from an object in Python, you can use the `del` statement. Here is how you can do it with the [`person`] object from your [`main.py`] file:

### Example of Deleting an Attribute

```python
# Adding a new attribute dynamically
person.sex = "female"

print(person.sex)  # Output: 'female'

# Deleting the attribute
del person.sex

# Trying to access the deleted attribute will raise an AttributeError
try:
    print(person.sex)
except AttributeError:
    print("The attribute 'sex' has been deleted.")

print(f"Person's dictionary after deletion: {person.__dict__}")  # Output: {'name': 'Sovanny Ou', 'age': 52}
```

### Explanation

1. **Add Attribute**: Add the `sex` attribute to the `person` object.
2. **Delete Attribute**: Use `del person.sex` to delete the `sex` attribute.
3. **Handle AttributeError**: Attempt to access the deleted attribute will raise an `AttributeError`, which is caught and handled.
4. **Print Object Dictionary**: Print the object's dictionary to verify the attribute has been removed.

This approach ensures that the attribute is completely removed from the object.

You can check if an attribute exists in an object in Python using the `hasattr()` function. This function returns `True` if the object has the specified attribute, and `False` otherwise.

Here's how you can use `hasattr()` in your existing code:

### Example of Checking if an Attribute Exists

```python
# Adding a new attribute dynamically
person.sex = "female"

print(person.sex)  # Output: 'female'

# Check if the attribute exists
if hasattr(person, 'sex'):
    print("The attribute 'sex' exists.")
else:
    print("The attribute 'sex' does not exist.")

# Deleting the attribute
del person.sex

# Check if the attribute exists after deletion
if hasattr(person, 'sex'):
    print("The attribute 'sex' exists.")
else:
    print("The attribute 'sex' does not exist.")
```

### Explanation

1. **Add Attribute**: Add the `sex` attribute to the `person` object.
2. **Check Attribute Existence**: Use `hasattr(person, 'sex')` to check if the `sex` attribute exists.
3. **Delete Attribute**: Use `del person.sex` to delete the `sex` attribute.
4. **Check Attribute Existence Again**: Use `hasattr(person, 'sex')` again to verify that the attribute has been deleted.

This approach allows you to safely check for the presence of an attribute before attempting to access or delete it.

## How can I access and modify attributes of an object dynamically in Python?

You can access and modify attributes of an object dynamically in Python using the `getattr()` and `setattr()` functions. These functions allow you to interact with attributes using their names as strings.

### Example of Accessing and Modifying Attributes Dynamically

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

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
```

### Explanation

1. **Create an Instance**: Create an instance of the `Person` class.
2. **Add Attribute Dynamically**: Use `setattr(person, 'sex', 'female')` to add the `sex` attribute.
3. **Access Attribute Dynamically**: Use `getattr(person, 'sex')` to access the `sex` attribute.
4. **Modify Attribute Dynamically**: Use `setattr(person, 'sex', 'male')` to modify the `sex` attribute.
5. **Check Attribute Existence**: Use `hasattr(person, 'sex')` to check if the `sex` attribute exists.
6. **Delete Attribute**: Use `delattr(person, 'sex')` to delete the `sex` attribute.
7. **Check Attribute Existence Again**: Use `hasattr(person, 'sex')` again to verify that the attribute has been deleted.

This approach allows you to dynamically interact with attributes of an object using their names as strings, providing flexibility in managing object attributes.
