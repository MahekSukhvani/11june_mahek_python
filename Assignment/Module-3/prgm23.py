# Q - 28 Write a Python program to match a word in a string using re.match().

import re

text = "hello, my name is mahek !"

word = "mah"

if re.match(word, text):
    print(f"'{word}' matched  the the string!")
else:
    print(f"'{word}' did not match the string.")