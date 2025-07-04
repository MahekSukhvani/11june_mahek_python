#Write a Python program to apply the map() function to square a list of numbers. 
    
list1 = [1,2,3,4,5,6,7]

# now we have to get the square of each number using map() function

sq_num = list(map(lambda x : x*x,list1))

'''here,
we use list() function to convert our output in list formate,
map -> this is function that apply each element of list , map(function,itreable),
lambda -> this is keyword use to create a function without name , it also one line function
lambda argument : ecxpression.'''

print("original numbers : ",list1)
print("squared numbers : ",sq_num)