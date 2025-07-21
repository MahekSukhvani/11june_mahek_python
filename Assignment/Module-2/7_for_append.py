# Write a Python program to insert elements into an empty list using a for loop and append().

data = []
n = int(input("How many values do you want to enter : "))

for i in range(n):
    value = input("Enter a value : ")
    data.append(value)

print(data)