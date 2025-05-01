#Fourth Real Python Project

'''
friends = 0

#Addition
friends = friends + 1
friends += 1

#Substraction
friends = friends - 2
friends -= 2

#Multiplication
friends = friends * 3
friends *= 3

#Division
friends = friends / 4
friends /= 4

#Exponent / Power
friends = friends ** 3
friends **= 3

#Remainder / Modulus
friends = friends % 2
friends %= 2
'''

'''
x = 3.14
x1 = 3.64
y = -5
z = 6

result = round(x)
result_alt = round(x1)
result_1 = abs(y)
result_2 = pow(2, 3)
result_3 = max(x, x1, y, z, result_2)
result_4 = min(x, x1, y, z, result_2)

print(result, result_alt, result_1, result_2, result_3, result_4)
'''

'''
import math

x = 9
y = 9.1
z = 9.9

print(math.pi) #Show Pi
print(math.e) #Show Euler
result = math.sqrt(x) #Squared root
result_1 = math.ceil(y) #Round up
result_2 = math.floor(z) #Round down

print(result, result_1, result_2)
'''

'''
#Tutorial 1
import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")
'''

'''
#Tutorial 2
import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")
'''

#Tutorial 3
import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")