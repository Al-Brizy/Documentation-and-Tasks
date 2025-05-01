# Seventh Real Python Project

num = 7
a = 3
b = 7
age = 23
temperature = 22
user_role = "Officer"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age > 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
accces_level = "Full Access" if user_role == "Admin" else "Limited Access"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(accces_level)