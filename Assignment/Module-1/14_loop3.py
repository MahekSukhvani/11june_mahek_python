#Write a Python program to find a specific string in the list using a simple for loop and if condition. 

List1 = ['apple', 'banana', 'mango']
search_item = "banana"

for i in List1:
    if i == search_item:
        print("True")
        break
else:
    print("False")