# Fifth Real Python Project Task
# It is on reverse condition

username = input("Enter a username: ")

# Checking username length
if len(username) > 12:
    print("Your username can't be more than 12 characters")

# Checking if there is not containing spaces, then continue.
# if we didn't put not in the condition, then it will be (whenever the .find return -1 or doesn't contain spaces, it will printed)
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")

# Checking the username only has character or contain numbers
elif not username.isalpha():
    print("Your username can't contain numbers")

else:
    print(f"Welcome {username}")