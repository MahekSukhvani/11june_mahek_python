# Write a generator function that generates the first 10 even numbers. 

#genrator return the value one at a time
#yield is keyword that pause the loop

def even_num():
    for i in range(2,21,2):
        yield i
    
for i in even_num():
    print(i)





