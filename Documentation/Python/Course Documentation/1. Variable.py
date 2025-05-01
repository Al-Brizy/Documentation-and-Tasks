# First Real Python Project

# Strings
first_name = "Dude"
food = "Kebab"
email = "ilovekebab@yeetmail.com"

print(f"Hello {first_name}")
print(f"Do you love {food}?")
print(f"is this your email? {email}")

# Integers
age = 23
quantity = 4
num_of_students = 22

print(f"Your age around {age} right?")
print(f"So u must be buyin Kebab approx {quantity} i guess")
print(f"If u r bout to going to class today, there must be {num_of_students} students in ur class rn")

# Float
price = 14.50
gpa = 3.3
distance = 5.5

print(f"i'll give u special price for you today, it's only take {price} rupiah")
print(f"I'll give you another discount later if your gpa more than {gpa} in this semester")
print(f"Your class took {distance}km from here tho, take a chill mate")

# Boolean
is_student = True
for_sale = True
is_online = True

if for_sale:
    print("Are u really student around here kiddo?")
    if is_student==(True):
        print("Aight let's see if u r connected to wifi around here")
        if is_online==(True):
            print("Aight, i got u a special dish today, it's on sale now")
        else:
            print("Try to connect ur student account to Main Hall wifi overthere buddy, then i'll get you the special dish")
    else:
        print("Nah, i can't sell it for strangers man, good day")
else:
    print("I got no special dish to sale to you today, sorry mate")