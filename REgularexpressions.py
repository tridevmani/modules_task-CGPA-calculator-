import re

reg = input("Enter registration number: ")

# Regular Expression Pattern
pattern = r"^[0-9]{5,10}$"

if re.match(pattern, reg):
    print("Valid Registration Number")
else:
    print("Invalid Registration Number")