# Write a Python program to show method overloading.


class Calculator:
    def add(self, a, b):
        print("Sum of 2 numbers:", a + b)

    def add(self, a, b, c):
        print("Sum of 3 numbers:", a + b + c)

    def add(self, a, b, c, d):
        print("Sum of 4 numbers:", a + b + c + d)


calc = Calculator()
calc.add(1, 2, 3, 4)