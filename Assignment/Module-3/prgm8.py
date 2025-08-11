# Write a Python program to check the current position of the file cursor using tell().

f1 = open('text.txt','r')

pos = f1.tell()
print(f"Current position of the cursor is {pos} ") #in the begning cursor position is 0

rd = f1.read(10) # we have to read something

pos = f1.tell() # after reading cursor move from 0 so its return curret position
print(f"Current position of the cursor is {pos} ")
