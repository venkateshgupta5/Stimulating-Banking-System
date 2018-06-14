# Stimulating Banking System in Python 3

This project is a stimulation of a simple banking system in Python. A user can create account by entering his name 

## Concepts Implemented 
1. Abstract Base Class
2. Overriding
3. Single Level Inheritance
4. Abstraction
5. Encapsulation

### Overriding

Modifying the inherited behaviour of methods of a base class in a derived class is called overriding.
 Syntax: 
class BaseClass: 
   def methodOne(self): # Body of method class 

DerivedClass(baseClass): 
   def methodOne(self): # Redefine the body of methodOne 

Example: class Shape: 
           def area(): 
           return 0 
         class Square(Shape): 
           def area(self, side): 
           return (side * side)
           
### Single Level Inheritance

Inheriting the attributes and methods of a base class into a
derived class is called Inheritance.
Syntax:
 class BaseClass: # Body of BaseClass
 class DerivedClass(BaseClass): # Body of DerivedClass
 
 Example:
 class Shape:
 unitOfMeasurement = 'centimetre'
 class Square(Shape):Modifying the inherited behaviour of methods of a base class in a derived class is called overriding.
 Syntax: 
class BaseClass: 
   def methodOne(self): # Body of method class 

DerivedClass(baseClass): 
   def methodOne(self): # Redefine the body of methodOne 

Example: class Shape: 
           def area(): 
           return 0 
         class Square(Shape): 
           def area(self, side): 
           return (side * side)
 
 def __init__(self): # The attribute unitOfMeasurement has been
                       inherited from the class Shape to this class Square
  print("Unit of measurement for this square: ",

self.unitOfMeasurement)
square = Square()

### Abstract Base Class (ABC)

A base class which contains abstract methods that are to
be overridden in its derived class is called an abstract base
class. They belong to the abc module.
Example:
from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCMeta):
@abstractmethod
def area(self):
return 0
class Square(Shape):
def area(self, side)
return side * side




