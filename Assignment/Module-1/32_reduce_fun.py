'''In Python, reduce() is not a built-in function, meaning it is not available by default.
That's why we must import it manually from the functools module before using it.
'''

from functools import reduce

# List of numbers
numbers = [2, 3, 4, 5]

# Use reduce() to calculate the product of the list
#reduce function keeps reducing the list to a single value by applying your function step by step.

product = reduce(lambda x, y: x * y, numbers)

# Print the result
print("List of numbers:", numbers)
print("Product of all numbers:", product)