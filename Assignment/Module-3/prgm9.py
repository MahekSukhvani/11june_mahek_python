# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 



def add():
    val1 = int(input("Enter First Value : "))
    val2 = int(input("Enter Second Value : "))
    cal = val1 + val2
    print(f"Addition Of {val1} And {val2} Is {cal}")

def sub():
    val1 = int(input("Enter First Value : "))
    val2 = int(input("Enter Second Value : "))
    cal = val1 - val2
    print(f"Substraction Of {val1} And {val2} Is {cal}")

def mul():
    val1 = int(input("Enter First Value : "))
    val2 = int(input("Enter Second Value : "))
    cal = val1 * val2
    print(f"Multiplication Of {val1} And {val2} Is {cal}")

def div():
    val1 = int(input("Enter First Value : "))
    val2 = int(input("Enter Second Value : "))
    cal = val1 / val2
    print(f"Division Of {val1} And {val2} Is {cal}")



while True:

    print()
    print("=============== CALCULATOR ===============\n")

    print("1.ADDITION")
    print("2.SUBSTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION\n")

    ch = int(input("Enter Your Choice : "))
    print()

    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        try:
            div()   
        except ZeroDivisionError:
            print("division by zero invalid input ,Value Can Not Divide By Zero..!")
        break
    else:

        print("Invalid Choice ! Please Choose From 1 To 4")