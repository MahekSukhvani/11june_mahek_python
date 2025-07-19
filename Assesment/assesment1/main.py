import Read_data
import take_data

def note():

    while True:

        print("WELCOME TO PYTHON E - NOTE ")
        print("===========================================")

        print("1. FOR GENERATE NOTE ")
        print("2. FOR VIEW NOTE ")
        print("3. EXIT")
        print()

        ch = int(input("Enter Your Choice : "))
        print()

        if ch==1:
            take_data.tdt()
        elif ch==2:
            Read_data.readdt()
            break
        else:
            exit

note()
    
