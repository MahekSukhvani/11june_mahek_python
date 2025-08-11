#  Write a Python program to print custom exceptions. 

try:
    a = int(input("Enter Value For A : "))
    b = int(input("Enter Value For B : "))

    print("Sum : " ,a+b)

except Exception as ex:
    print("Error Occur : ",ex)