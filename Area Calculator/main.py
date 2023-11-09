#Joshua Strutton CS160

import math

#Rectagle, Triange, Circle

print("Choose a shape: Rectangle, Triangle, or Circle")
shape = input()
result = -1


if shape == "Rectangle":
    print("Length Dimension: ")
    length = int(input())
    
    print("Width Dimension: ")
    width = int(input())
    
    result = length * width
elif shape == "Triangle":
    print("Base Dimension: ")
    base = int(input())
    
    print("Height Dimension: ")
    height = int(input())
    
    result = (base * height)/2
elif shape == "Circle":
    print("radius Dimension: ")
    radius = int(input())
    
    result = math.pi * math.pow(radius, 2)

else:
    print("Not a valid Shape!!")
    
if result != -1:
    print(result)
    
input()