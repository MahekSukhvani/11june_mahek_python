# Write a Python program to search for a word in a string using re.search().

import re

text = "Hello, my name is mahek !"

word = "mahek"

if re.search(word, text):
    print(f"'{word}' found in the string!")
else:
    print(f"'{word}' not found is the string.")