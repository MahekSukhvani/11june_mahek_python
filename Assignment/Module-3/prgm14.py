# Write a Python program to demonstrate the use of local and global variables in a class.
pi = 3.14159 # global variable


class Shape:
    def area_of_circle(self ):
        global pi  
        radius = int(input("Enter A Radius : ")) # local variable
        area = pi * (radius ** 2) 
        print(f"Area of circle with radius {radius} is : {area}")

s=Shape()
s.area_of_circle()
