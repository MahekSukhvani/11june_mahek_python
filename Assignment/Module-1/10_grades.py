#defination: Write a Python program to calculate grades based on percentage using if-else ladder. 

per = float(input("Enter Your Percentage : "))

if per>=90:
    print("You Got Grade A")
elif per>=80:
    print("You Got Grade B")
elif per>=75:
    print("You Got Grade C")
elif per>=60:
    print("You Got Grade D")
else:
    print("You Need Some More Practice")