#Write a Python program that filters out even numbers using the filter() function. 

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even_num = list(filter(lambda x : x%2==0,list1))

print("Original numbers : ",list1)
print("even numbers : ",even_num)