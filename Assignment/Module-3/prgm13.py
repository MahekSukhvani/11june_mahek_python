# Write a Python program to create a class and access its properties using an object.

class operation:
    
    nm = input("Enter Your Name : ")
    age = input("Enter Your Age : ")

    def sqrt(self):
        num = int(input("Enter Your Number : "))
        rt = num*num*num
        print(f"Square Root Of {num} is {rt}")


o1=operation()
o1.nm
o1.age
o1.sqrt()