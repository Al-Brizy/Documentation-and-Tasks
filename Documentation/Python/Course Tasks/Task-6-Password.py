# 1. Password must not less than 8 characters
# 2. Password must contain characters and numbers
# 3. Password must contain capital character in the first character
# 4. Password must not contain spaces

password = input("Enter your password: ")

if len(password) < 8:
    print("Your password can't be less than 8 characters")
elif not password.find(" ") == -1:
    print("Your password can't contain spaces")
elif not password == password.capitalize():
    print("Your password must contain capital in the first character")
elif password.isalpha() or password.isdigit():
    print("Your password must contain characters and numbers")
else:
    pick = input("Your password is strong enough, wanna see it? (Y/N): ")
    print(f"Here is your password: {password}" if pick == "Y" else "...ok")