#defination: How to check the type of a variable dynamically using type(). 


# Take input from user
data = input("Enter any value: ")

# Detect type using simple conditions
if data.lower() in ["true", "false"]:
    data = bool(data)
elif data.isdigit():
    data = int(data)
elif "." in data :
    data = float(data)
else:
    data = str(data)

# Print the result
print("\nYou entered:", data)
print("Detected data type:", type(data))
