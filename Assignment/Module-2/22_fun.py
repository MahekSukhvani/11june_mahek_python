#Write a Python program to create a calculator using functions. 

def add():
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    num = num1 + num2
    print("Addition Of Value Is : ",num)

def sub():
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    num = num1 - num2
    print("Substraction Of Value Is : ",num)

def mul():
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    num = num1 * num2
    print("Multiplication Of Value Is : ",num)

def div():
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    num = num1 / num2
    print("Division Of Value Is : ",num)

def mod():
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    num = num1 % num2
    print("Modulus Division Of Value Is : ",num)

while True :
    print("============== MENU ==============")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus Division")
    print("6.Exit")
    print()

    ch = int(input("Enter Your Choice For Perform Relevent Opration: "))


    if ch==1:
        add()
        print()

    elif ch==2:
        sub()
        print()

    elif ch==3:
        mul()
        print()

    elif ch==4:
        div()
        print()

    elif ch==5:
        mod()
        print()
        break

    else:
        exit()

