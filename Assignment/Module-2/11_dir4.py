#Write a Python program to merge two lists into one dictionary using a loop.

dirr = {}

list1 = ['id','name','city']
list2 = [1,'mahek','rajkot']

for i in range(len(list1)):
    dirr[list1[i]] = list2[i]

print(dirr)