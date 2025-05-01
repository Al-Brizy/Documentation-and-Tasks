# Extras Real Python Project Task

name = input("\nWelcome to my Madlibs Game, this time the story theme is Medieval, so what's your name sir?: ")
print(f"Alright sir {name}, please follow any instruction below to achieve the best story experience, have fun!")

print("\nBelow is for the title of the story")
noun_1 = input("Should be a noun (person, place, thing): ")

print("\nBelow is for the first paragraph")
place_1 = input("Should be a region: ")
occupation_1 = input("Should be the occupation or job: ")
name_1 = input("Should be main character name, or you want to use your own name? (yes/no/[new name]): ")
if name_1 == "yes":
    name_1 = name
elif name_1 == "no":
    input("Then, what is your main character name: ")
name_2 = input("Should be the king's name: ")
building_1 = input("Should be name one of the building that built in medieval era: ")

print("\nBelow is for the second paragraph")
name_3 = input("Should be the villain's name: ")

print("\nBelow is for the third paragraph")
animal_1 = input("Should be the main character's animal: ")
adjective_1 = input("Should be adjective (description): ")
place_2 = input("Should be a region or adjective: ")
creature_1 = input("Should be a thing's or creature's name: ")
body_of_water_1 = input("Should be a body of water (ocean, seas, lake, etc.): ")

print("\nBelow is for the fourth paragraph")
adjective_2 = input("Should be adjective (description): ")
place_3 = input("Should be a place region or adjective: ")
weapon_1 = input("Should be the main character's weapon: ")

print("\nBelow is for the fifth paragraph")
food_1 = input("Should be a food's name: ")
drink_1 = input("Should be a drink's name: ")
number_1 = input("Shoud be a number of the days: ")

print("\nAll completed, thank you for filling out and here it is, your own story")

print(f"\nThe Quest for the Lost {noun_1}")
print(f"\nIn the ancient kingdom of {place_1}, there lived a brave {occupation_1} named Sir {name_1}. \nOne day, the wise King {name_2} summoned Sir {name_1} to the grand {building_1}.")
print(f'\n"My loyal {occupation_1}" said the King, "our precious {noun_1} has been stolen by the evil sorcerer \n{name_3}! You must embark on a quest to retrieve it!"')
print(f"\nSir {name_1} mounted his noble {animal_1}, donned his shining {adjective_1} armor, and set off toward \nthe dark forests of {place_2}. Along the way, he battled a fierce {creature_1}, crossed the raging {body_of_water_1},\n and outsmarted a cunning {occupation_1} disguised as a harmless {animal_1}.")
print(f"\nFinally, deep within the {adjective_2} caves of {place_3}, Sir {name_1} confronted the villainous {name_3}. \nWith a swift swing of his {weapon_1}, he defeated the sorcerer and reclaimed the kingdom’s beloved {noun_1}!")
print(f"\nReturning to {place_1}, Sir {name_1} was hailed as a hero, and celebrated with a grand feast of {food_1} \nand {drink_1} that lasted for {number_1} days and nights.")
print(f"\nAnd thus, the legend of Sir {name_1} and the Quest for the Lost {noun_1} lived on for generations.")

print(f"\nCongratulations for completing your own story, thank you for playing and stay tune for the next story, have a great day sir {name}!")