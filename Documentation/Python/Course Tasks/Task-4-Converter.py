# Fourth Real Python Project Task

'''
# Quest 1 (Weight Converter)
weight = float(input("\nEnter your weight: "))
unit = input("Kilograms or Pound? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid!")
'''

# Quest 2 (Temperature Converter)
unit = input("\nEnter your current temperature. Celcius, Fahrenheit, or Kelvin? (C/F/K): ")

# Unit in Celcius
if unit == "C" or "c" or "Celcius" or "celcius":
    target = input("What do want to convert to? Fahrenheit or Kelvin? (F/K): ")
    temp = float(input("Enter the temperature: "))

    # Convert to Fahrenheit
    if target == "F" or "f" or "Fahrenheit" or "fahrenheit":
        result = round(temp * (9 / 5) + 32, 2)
        print(f"The temperature in Fahrenheit is: {result}°F")

    # Convert to Kelvin
    elif target == "K" or "k" or "Kelvin" or "kelvin":
        result = round(temp + 273.15, 2)
        print(f"The temperature in Kelvin is: {result}°K")

    # Forced Stop
    else:
        print(f"\n{target} is an invalid input, please rerun the code!"
              "\nIn this point i'm only using basic syntax following my own course."
              "\nI'll update the new version later after learning a new method."
              "\nthank you for your concern.")
        exit()

# Unit in Fahrenheit
elif unit == "F" or "f" or "Fahrenheit" or "fahrenheit":
    target = input("What do want to convert to? Celcius or Kelvin? (C/K): ")
    temp = float(input("Enter the temperature: "))

    # Convert to Celcius
    if target == "C" or "c" or "Celcius" or "celcius":
        result = round((temp - 32) * 5 / 9, 2)
        print(f"The temperature in Celcius is: {result}°C")

    # Convert to Kelvin
    elif target == "K" or "k" or "Kelvin" or "kelvin":
        result = round((temp - 32) * 5 / 9 + 273.15, 2)
        print(f"The temperature in Kelvin is: {result}°K")

    # Forced Stop
    else:
        print(f"\n{target} is an invalid input, please rerun the code!"
              "\nIn this point i'm only using basic syntax following my own course."
              "\nI'll update the new version later after learning a new method."
              "\nthank you for your concern.")
        exit()

# Unit in Kelvin
elif unit == "K" or "k" or "Kelvin" or "kelvin":
    target = input("What do want to convert to? Celcius or Fahrenheit? (C/F): ")
    temp = float(input("Enter the temperature: "))

    # Convert to Celcius
    if target == "C" or "c" or "Celcius" or "celcius":
        result = round(temp - 273.15, 2)
        print(f"The temperature in Celcius is: {result}°C")

    # Convert to Fahrenheit
    elif target == "F" or "f" or "Fahrenheit" or "fahrenheit":
        result = round((temp - 273.15) * 9 / 5 + 32, 2)
        print(f"The temperature in Fahrenheit is: {result}°F")

    # Forced Stop
    else:
        print(f"\n{target} is an invalid input, please rerun the code!"
              "\nIn this point i'm only using basic syntax following my own course."
              "\nI'll update the new version later after learning a new method."
              "\nthank you for your concern.")
        exit()

else:
    print(f"\n{unit} is an invalid input, please rerun the code!"
          "\nIn this point i'm only using basic syntax following my own course."
          "\nI'll update the new version later after learning a new method."
          "\nthank you for your concern.")
    exit()
