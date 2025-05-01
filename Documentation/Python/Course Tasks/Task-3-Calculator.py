# Third Real Python Project Task
import math

print("\n===================================="
      "\n  Welcome to my shapes calculator.  "
      "\n    here is the shapes list that    "
      "\n         available for now.         "
      "\n------------------------------------"
      "\n 1. 2D SHAPES     | 2. 3D SHAPES    "
      "\n------------------------------------"
      "\n 1. Area          | 1. Volume       "
      "\n 2. Circumference | 2. Surface Area "
      "\n------------------------------------"
      "\n 1. Square        | 1. Cube         "
      "\n 2. Rectangle     | 2. Cuboid       "
      "\n 3. Triangle      | 3. Cylinder     "
      "\n 4. Trapezoid     | 4. Cone         "
      "\n 5. Circle        | 5. Sphere       "
      "\n------------------------------------"
      "\n 0. EXIT                            "
      "\n====================================")

w = 0
x = 0
y = 0
z = 0
result = 0

dimensions = input("\nWhich Shape Dimension do you want to calculate, 2D or 3D? (1 or 2): ")

# 2D Shapes
if dimensions == "1":
    choice = input("What do you want to calculate? Area or Circumference (1 or 2): ")

    # Area
    if choice == "1":
        shapes = input("Which Shape do you want to calculate? (pick a number): ")

        # Area of Square
        if shapes == "1":
            x = float(input("Enter Length: "))
            result = math.pow(x, 2)
            print(f"The Area of your Square is: {round(result, 2)}cm^2")

        # Area of Rectangle
        elif shapes == "2":
            x = float(input("Enter Length: "))
            y = float(input("Enter Width: "))
            result = x * y
            print(f"The Area of your Rectangle is: {round(result, 2)}cm^2")

        # Area of Triangle
        elif shapes == "3":
            x = float(input("Enter Length: "))
            y = float(input("Enter Height: "))
            result = 1 / 2 * x * y
            print(f"The Area of your Triangle is: {round(result, 2)}cm^2")

        # Area of Trapezoid
        elif shapes == "4":
            x = float(input("Enter Base 1 (top): "))
            y = float(input("Enter Base 2 (bottom): "))
            z = float(input("Enter Height: "))
            result = 1 / 2 * (x + y) * z
            print(f"The Area of your Trapezoid is: {round(result, 2)}cm^2")

        # Area of Circle
        elif shapes == "5":
            x = float(input("Enter Radius: "))
            result = math.pi * math.pow(x, 2)
            print(f"The Area of your Circle is: {round(result, 2)}cm^2")

        # Exit
        elif shapes == "0":
            print("\nThank you for using my first version shapes calculator, next version will updated soon.")
            exit()

        # Forced Stop
        else:
            print(f"\n{shapes} is an invalid input, please rerun the code!"
                  "\nIn this point i'm only using basic syntax following my own course."
                  "\nI'll update the new version later after learning a new method."
                  "\nthank you for your concern.")
            exit()

    # Circumference
    elif choice == "2":
        shapes = input("Which Shapes do you want to calculate? (pick a number): ")

        # Circumference of Square
        if shapes == "1":
            x = float(input("Enter Length: "))
            result = 4 * x
            print(f"The Circumference of your Square is: {round(result, 2)}cm^2")

        # Circumference of Rectangle
        elif shapes == "2":
            x = float(input("Enter Length: "))
            y = float(input("Enter Width: "))
            result = 2 * (x + y)
            print(f"The Circumference of your Rectangle is: {round(result, 2)}cm^2")

        # Circumference of Triangle
        elif shapes == "3":
            x = float(input("Enter Side 1: "))
            y = float(input("Enter Side 2: "))
            z = float(input("Enter Side 3: "))
            result = x + y + z
            print(f"The Circumference of your Triangle is: {round(result, 2)}cm^2")

        # Circumference of Trapezoid
        elif shapes == "4":
            w = float(input("Enter Side left: "))
            x = float(input("Enter Side right: "))
            y = float(input("Enter Side top: "))
            z = float(input("Enter Side bottom: "))
            result = w + x + y + z
            print(f"The Circumference of your Trapezoid is: {round(result, 2)}cm^2")

        # Circumference of Circle
        elif shapes == "5":
            x = float(input("Enter Radius: "))
            result = 2 * math.pi * x
            print(f"The Circumference of your Circle is: {round(result, 2)}cm^2")

        # Exit
        elif shapes == "0":
            print("\nThank you for using my first version shapes calculator, next version will updated soon.")
            exit()

        # Forced Stop
        else:
            print(f"\n{shapes} is an invalid input, please rerun the code!"
                  "\nIn this point i'm only using basic syntax following my own course."
                  "\nI'll update the new version later after learning a new method."
                  "\nthank you for your concern.")
            exit()

    # Exit
    elif choice == "0":
        print("\nThank you for using my first version shapes calculator, next version will updated soon.")
        exit()

    # Forced Stop
    else:
        print(f"\n{choice} is an invalid input, please rerun the code!"
              "\nIn this point i'm only using basic syntax following my own course."
              "\nI'll update the new version later after learning a new method."
              "\nthank you for your concern.")
        exit()

# 3D Shapes
elif dimensions == "2":
    choice = input("What do you want to calculate? Volume or Surface Arae (1 or 2): ")

    # Volume
    if choice == "1":
        shapes = input("Which Shape do you want to calculate? (pick a number): ")

        # Volume of Cube
        if shapes == "1":
            x = float(input("Enter Length: "))
            result = math.pow(x, 3)
            print(f"The Volume of your Cube is: {round(result, 2)}cm^3")

        # Volume of Cuboid
        if shapes == "2":
            x = float(input("Enter Length: "))
            y = float(input("Enter Width: "))
            z = float(input("Enter Height: "))
            result = x * y * z
            print(f"The Volume of your Cuboid is: {round(result, 2)}cm^3")

        # Volume of Cylinder
        elif shapes == "3":
            x = float(input("Enter Radius: "))
            y = float(input("Enter Height: "))
            result = math.pi * math.pow(x, 2) * y
            print(f"The Volume of your Cylinder is: {round(result, 2)}cm^3")

        # Volume of Cone
        elif shapes == "4":
            x = float(input("Enter Radius: "))
            y = float(input("Enter Height: "))
            result = 1 / 3 * math.pi * math.pow(x, 2) * y
            print(f"The Volume of your Cone is: {round(result, 2)}cm^3")

        # Volume of Sphere
        elif shapes == "5":
            x = float(input("Enter Radius: "))
            result = 4 / 3 * math.pi * math.pow(x, 3)
            print(f"The Volume of your Sphere is: {round(result, 2)}cm^3")

        # Exit
        elif shapes == "0":
            print("\nThank you for using my first version shapes calculator, next version will updated soon.")
            exit()

        # Forced Stop
        else:
            print(f"\n{shapes} is an invalid input, please rerun the code!"
                  "\nIn this point i'm only using basic syntax following my own course."
                  "\nI'll update the new version later after learning a new method."
                  "\nthank you for your concern.")
            exit()

    # Surface Area
    elif choice == "2":
        shapes = input("Which Shapes do you want to calculate? (pick a number): ")

        # Surface of Cube
        if shapes == "1":
            x = float(input("Enter Length: "))
            result = 6 * math.pow(x, 2)
            print(f"The Surface of your Cube is: {round(result, 2)}cm^3")

        # Surface of Cuboid
        if shapes == "2":
            x = float(input("Enter Length: "))
            y = float(input("Enter Width: "))
            z = float(input("Enter Height: "))
            result = 2 * (x + y + z)
            print(f"The Surface of your Cuboid is: {round(result, 2)}cm^3")

        # Surface of Cylinder
        elif shapes == "3":
            x = float(input("Enter Radius: "))
            y = float(input("Enter Height: "))
            result = 2 * math.pi * x * (x + y)
            print(f"The Surface of your Cylinder is: {round(result, 2)}cm^3")

        # Surface of Cone
        elif shapes == "4":
            x = float(input("Enter Radius: "))
            y = float(input("Enter Height: "))
            result = math.pi * x * (x + math.sqrt(math.pow(y, 2) + math.pow(x, 2)))
            print(f"The Surface of your Cone is: {round(result, 2)}cm^3")

        # Surface of Sphere
        elif shapes == "5":
            x = float(input("Enter Radius: "))
            result = 4 * math.pi * math.pow(x, 2)
            print(f"The Surface of your Sphere is: {round(result, 2)}cm^3")

        # Exit
        elif shapes == "0":
            print("\nThank you for using my first version shapes calculator, next version will updated soon.")
            exit()

        # Forced Stop
        else:
            print(f"\n{shapes} is an invalid input, please rerun the code!"
                  "\nIn this point i'm only using basic syntax following my own course."
                  "\nI'll update the new version later after learning a new method."
                  "\nthank you for your concern.")
            exit()

    # Exit
    elif choice == "0":
        print("\nThank you for using my first version shapes calculator, next version will updated soon.")
        exit()

    # Forced Stop
    else:
        print(f"\n{choice} is an invalid input, please rerun the code!"
              "\nIn this point i'm only using basic syntax following my own course."
              "\nI'll update the new version later after learning a new method."
              "\nthank you for your concern.")
        exit()

# Exit
elif dimensions == "0":
    print("\nThank you for using my first version shapes calculator, next version will updated soon.")
    exit()

# Forced Stop
else:
    print(f"\n{dimensions} is an invalid input, please rerun the code!"
          "\nIn this point i'm only using basic syntax following my own course."
          "\nI'll update the new version later after learning a new method."
          "\nthank you for your concern.")
    exit()

# Created by Albrizy