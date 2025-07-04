a = "Hello, World!" 
print(a[1]) # print the 1 index character

a = "Hello, World!" 
print(a[2:5]) # returns the 2 to 5 in between character

a = "      Hello, World! " 
print(a.strip()) # returns "Hello, World!" 

a = "Hello, World!" 
print(len(a)) # returns string length

a = "Hello, World!" 
print(a.lower()) # convert string into lower case

a = "Hello, World!" 
print(a.upper()) # convert string into upper case

a = "Hello, World!" 
print(a.replace("H", "J")) # replace h char with j 

a = "hello, world!"
print(a.title())  # Capitalizes the first letter of each word

a = "hello, world!"
print(a.capitalize()) # Capitalizes the first character of the string

a = "hello, hello, hello!"
print(a.count("hello")) # Counts occurrences of a substring

a = "hello, world!"
print(a.find("world")) # Returns the index of the first occurrence

a = "apple banana apple"
print(a.rfind("apple")) # Returns the index of the last occurrence

a = "Hello world"
print(a.startswith("Hello")) # Checks if string starts with a substring

a = "Hello world"
print(a.endswith("world")) # Checks if string ends with a substring

a = "Hello"
print(a.isalpha())  # Checks if all characters are letters

a = "12345"
print(a.isdigit())  # Checks if all characters are digits

a = "Hello123"
print(a.isalnum()) # Checks if all characters are alphanumeric

a = "Python is fun"
print(a.split()) # Splits the string into a list

a = ["Python", "is", "fun"]
print(" ".join(a)) # Joins a list of strings into a single string

a = "Hello World"
print(a.swapcase()) # Swaps lowercase to uppercase and vice versa

a = "Hello"
print(a.center(12, "*")) # Centers the string with padding
