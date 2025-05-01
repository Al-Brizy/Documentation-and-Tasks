# Third Real Python Project

# Example
name = input("Who are you again sir? sorry: ")

# case 2 if u want to typecasting first, idk what it is called
age = int(input("How long did you live?: ")) #best method

# case 1 if u want to typecasting later
#age = int(age)
age += 1

print(f"Ahh yes sir {name}, glad to see you back sir!")
print(f"Congratulations for completing your {age} years journey sir!")
print(f"That's quite long journey isn't it? {age} years old of wandering, sure u had crazy story")

# Tutorial 1
length = float(input("Enter your sword length: "))
width = float(input("Enter your sword width: "))
area = length * width

print(f"Your sword area approx {area}cm square")

# Tutorial 2
item = input("Which item do you need sir?: ")
price = float(input("How much is it? i mean the price: "))
quantity = int(input("Aight then, how many?: "))

total = price * quantity

print(f"There you go, {quantity} x {item}/s are ready to go")
print(f"It'll cost you ${total} sir!")