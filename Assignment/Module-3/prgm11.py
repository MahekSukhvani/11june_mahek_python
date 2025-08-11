#Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    f1 = open("sq.txt",'w')
    num = int(input("Enter Your Number For Square : "))
    val = num*num
    f1.write(f"Square Of {num} Is :{val}" )
except ValueError:
    print("Please Enter Integert Type Of Value For Square Operation")
finally:
    f1.close()
    print("File Closed SuccessFully !")