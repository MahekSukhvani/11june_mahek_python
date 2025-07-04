'''defination : Write a Python program that demonstrates the correct use of indentation, comments, and 
variables following PEP 8 guidelines.'''

#it takes the input from user for number1 and number2

n1 = float(input("Enter the number1: ")) 
n2 = float(input("Enter the number2: ")) 

#menu form which user can able to take the choice

print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice : ")

# conditional statements which show the use of the variables and the indentations.

if choice == "1":
    print("Addition is :", n1 + n2)
elif choice == "2":
    print("Subtraction is :", n1 - n2)
elif choice == "3":
    print("Multiplication is :", n1 * n2)
elif choice == "4":
        print("Division is :", n1 / n2)
else:
    print("Invalid choice.")