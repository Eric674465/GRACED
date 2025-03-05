#import math module

import math
# Create a class named Shape
class Shapes:
    def area(self):
#Method to override
     raise NotImplementedError("Subclass must implement abstract method") 
    
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

#Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
    def area(self):
        return self.length * self.width

class Circle(Shapes):
    def __init__(self, radius):
         self.radius = radius

    def area(self):
       return math.pi * self.radius **2
   

