Stimulating Banking System in Python 3 

This project is a stimulation of a simple banking system in Python.

Concepts Implemented :- 

Abstract Base Class
Overriding
Inheritance
Abstraction
Encapsulation

Overriding

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


