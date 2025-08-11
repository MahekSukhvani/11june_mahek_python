# Write a Python program to show hierarchical inheritance.

class data:
    def val(self):
        self.val1 = int(input("Enter the first value: "))
        self.val2 = int(input("Enter the second value: "))
        
class addition(data):
    def add(self):
        self.a = self.val1 + self.val2
        print("\naddition of value is :",self.a)   
        print("========================================")     
    
class subtraction(data):     
    def sub(self):
        self.b =  self.val1 - self.val2
        print("\nsubtraction of value is :",self.b)
        print("========================================")


class multiplication(data):
    def mul(self):
        self.c = self.val1 * self.val2    
        print("\nmultiplication of value is :",self.c)
        print("========================================")

class division(data):
    def div(self):
        self.d = self.val1 / self.val2
        print("\ndivision of value is :",self.d)

a1=addition()
s1=subtraction()
m1=multiplication()
d1=division()
a1.val()
a1.add()
s1.val()
s1.sub()
m1.val()    
m1.mul()
d1.val()
d1.div()
