# Write a Python program to show multiple inheritance. 

class Addition:
    def add(self, a, b):
        return a + b

class Multiplication:
    def multiply(self, a, b):
        return a * b

class Calculator(Addition, Multiplication):
    def calculate(self, a, b):
        print(f"Addition of {a} and {b}: {self.add(a, b)}")
        print(f"Multiplication of {a} and {b}: {self.multiply(a, b)}")

calc = Calculator()
calc.calculate(5, 3)