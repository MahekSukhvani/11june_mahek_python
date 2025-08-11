# Write a Python program to demonstrate the use of super() in inheritance. 

class Parent:
    def display(self):
        print("This is the Parent class method.")

class Child(Parent):
    def display(self):
        super().display()
        print("This is the Child class method.")

obj = Child()
obj.display()
