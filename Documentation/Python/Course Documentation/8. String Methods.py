# Eighth Real Python Project

#name = input("Enter your full name: ")
phone_number = input("Enter your phone number #: ")

# For measure the length of string, started with 0
# result = len(name)

# For find specific letter (Case sensitive) in string from front, output will be an array, started with 0
# result = name.find("i")

# For find specific letter (Case sensitive) in string from behind, output will be an array, started with 0
# result = name.rfind("a")

# For capitalized the first array of string
# name = name.capitalize()

# For uppercase all letter of string
# name = name.upper()

# For lowercase all letter of string
# name = name.lower()

# For check the inputted string has only digit/integer (can't combine char with int)
# result = name.isdigit()

# For check the inputted string has only alphabet/character without space, it will say False (can't combine char with int)
# result = name.isalpha()

# For count the specific condition in inputted string
# result = phone_number.count("-")

# For replace the specific condition in inputted string to a new condition
phone_number = phone_number.replace("-", "")

print(phone_number)