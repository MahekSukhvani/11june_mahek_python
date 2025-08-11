# Write a Python program to read a string, an integer, and a float from  the keyboard and display them.

val = input("Enter A Value : ")

try : 
    int_val = int(val)
    print(f"You Entered Integer Value {val}")
except ValueError:
    try:
        float_val = float(val)
        print(f"You Entered Float Value {val}")
    except ValueError:
        print(f"You Entered String Value {val}")
