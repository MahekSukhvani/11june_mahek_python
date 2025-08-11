# Write a Python program to show multilevel inheritance.


class Add:
    def addition(self, a, b):
        return a + b

class Subtract(Add):
    def subtraction(self, a, b):
        return a - b

class Multiply(Subtract):
    def multiplication(self, a, b):
        return a * b

o1 = Multiply()

# Access methods from all levels
print("Addition:", o1.addition(10, 5))       
print("Subtraction:", o1.subtraction(10, 5)) 
print("Multiplication:", o1.multiplication(10, 5)) 
