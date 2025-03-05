#Exploring static and class methods in python

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
# class attribute 
class MathOperations:
    calculation_type = "Arithmetic Operations" 

    @classmethod
    def multiply(cls, x, y):
        print(f"Multiplying {x} and {y}")
        return x * y
    