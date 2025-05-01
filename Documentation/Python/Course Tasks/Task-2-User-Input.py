# Second Real Python Project Task

'''
# Quest 1
length = float(input("How long is your item length?: "))
width = float(input("How wide is your item width?: "))
height = float(input("How tall is your item height?: "))

volume = length * width * height
if volume>10000:
    print(f"Your item volume is {volume}cm cubic, that's quite big")
else:
    print(f"Your item volume is {volume}cm cubic, that's kinda small isn't it?")
'''

# Quest 2
red_pot = 300
blue_pot = 200
purple_pot = 500
yes = True
no = False

item = str(input("Welcome to my shop, what do you wanna buy? i got red, blue, and purple potion: "))
if item == "red potion":
    item_temp = red_pot
elif item == "blue potion":
    item_temp = blue_pot
elif item == "purple potion":
    item_temp = purple_pot
else:
    print("We don't have that here sir, sorry")
    exit()

quantity_1 = int(input("How many pot do you need?: "))
total_temp = item_temp * quantity_1

print(f"Aight sir, here it is the pot you just bought sir, it's {quantity_1} pcs of {item}")
print(f"Total of the item is {total_temp} gold sir")
print("Thank you for stopping by sir, have a great journey!")

'''
#In Progress next update
add_more = str(input("Well, do you need anything else? just say yes or no: "))
if add_more == "yes":
    add_more = yes
    item = str(input("Then what is it? red, blue, or purple potion?: "))
    if item == "red potion":
        item_temp = red_pot
    elif item == "blue potion":
        item_temp = blue_pot
    elif item == "purple potion":
        item_temp = purple_pot
    else:
        print("We don't have that here sir, sorry")

    item_2 = item
    quantity_2 = int(input("How many pot do you need?: "))
    total = (item_temp * quantity_2) + total_temp

    print(f"Aight sir, here it is the pot you just bought sir, it's {quantity_1} pcs of {item}, and {quantity_2} pcs of {item}")
    print(f"Total of the item is {total} gold sir")
    print("Thank you for stopping by sir, have a great journey!")

elif add_more == "no":
    add_more = no

    print(f"Aight sir, here it is the pot you just bought sir, it's {quantity_1} pcs of {item}")
    print(f"Total of the item is {total_temp} gold sir")
    print("Thank you for stopping by sir, have a great journey sir!")

else:
    print("I say just say yes or no sir, *exhales*")
'''
