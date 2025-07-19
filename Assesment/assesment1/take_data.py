f1 = open("note.txt","a")

def tdt():
    nm = input("Enter Your E-Book Name : ")
    ttl = input("Enter Your E-Book Title Name : ")
    cnt = input("Enter Your E-Book Content : ")

    f1.write(f"Your E-Book Name : {nm}\n Your E-Book Title Name : {ttl}\n Your E-Book Content :{cnt} ")

