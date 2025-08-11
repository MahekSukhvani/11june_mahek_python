# Write a Python program to demonstrate handling multiple exceptions.

# Python program to handle multiple exceptions

def list_and_math_operations():
    try:
        numbers = [10, 20, 30, 40, 50]
        index = int(input("Enter list index (0-4): "))
        value = numbers[index]
        print(f"Value at index {index}: {value}")

        divisor = int(input("Enter a number to divide the value: "))
        result = value / divisor
        print(f"Result: {result}")

    except IndexError:
        print("Error: Index out of range. Please choose between 0 and 4.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Please enter valid integer values.")

    except Exception as e:
        print(f"Unexpected error: {e}")

list_and_math_operations()

