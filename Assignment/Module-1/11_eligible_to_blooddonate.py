#defination: Write a Python program to check if a person is eligible to donate blood using a nested if. 

#take the age and weight from user

age = int(input("Enter Your Age : "))
weight = int(input("Enter Your weight : "))

if age>=18:
    if weight>=55:
        print("You are Eligible to donate Blood")
    else:
        print("You are not Eligible to donate Blood")
else:
    print("You are not Eligible to donate Blood")
