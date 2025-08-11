# Write a Python program to show single inheritance.

class tkdata:
    def getdata(self):
        self.nm = input("Enter Your Name : ")
        self.age = input("Enter Your Age : ")
        self.ct = input("Enter Your City : ")
        self.st = input("Enter Your Stream : ")
        

class ptdata(tkdata):
    def printdata(self):
        print("\n========================================")
        print("Your name is : ",self.nm)
        print("Your age is : ",self.age)
        print("Your city is : ",self.ct)
        print("Your stream is : ",self.st)

p1 = ptdata()
p1.getdata()
p1.printdata()