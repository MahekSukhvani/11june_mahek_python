#defination : How does the Python code structure work? 

# Step 1: Define a function to greet the user
def greet_user(name):
    print("\nHello", name + "! Welcome to the Python Program.\n")

# Step 2: Define a function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print("The number", number, "is Even.")
    else:
        print("The number", number, "is Odd.")

# Step 3: Start of the main program
# Take user's name and number as input
user_name = input("Enter your name: ")
user_number = int(input("Enter a number: "))

# Step 4: Call the functions
greet_user(user_name)
check_even_odd(user_number)

# Step 5: Print numbers from 1 to user_number
print("\nCounting from 1 to", user_number, ":")
for i in range(1, user_number,1):
    print(i)