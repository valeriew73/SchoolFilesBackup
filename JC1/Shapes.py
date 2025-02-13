import math 
pi = math.pi

#circle
def areaOfCircle(rad):
    circleArea = pi * rad * rad
    return circleArea

def perimeterOfCircle(rad):
    circlePerimeter = 2 * pi * rad
    return circlePerimeter

#rectangle
def areaOfRectangle(height, length):
    rectangleArea = height * length
    return rectangleArea

def perimeterOfRectangle(height, length):
    rectanglePerimeter = 2 * (height + length)
    return rectanglePerimeter

#parallelogram
def areaOfParallelogram(height, length):
    parallelogramArea = height * length
    return parallelogramArea

def perimeterOfParallelogram(height, length):
    parallelogramPerimeter = 2 * (height + length)
    return parallelogramPerimeter

#triangle
def areaOfTriangle(height, length):
    triangleArea = 1/2 * height * length
    return triangleArea

def perimeterOfTriangle(length, side2, side3):
    trianglePerimeter = (length + side2 + side3)
    return trianglePerimeter

#sphere
def volumeOfSphere(rad):
    sphereVolume = 4/3 * pi * (rad**3)
    return sphereVolume

shapeChoice = str(input("Pick a shape: Circle, Rectangle, Parallelogram, Triangle, Sphere: "))
if shapeChoice == "Circle":
    rad = int(input("Enter the radius of the circle: "))
    areaTemp = areaOfCircle(rad)
    perimeterTemp = perimeterOfCircle(rad)
    print(f"The area of the circle is {areaTemp} and the perimeter  is {perimeterTemp}.")
elif shapeChoice == "Rectangle":
    height = int(input("Enter the height of the rectangle: "))
    length = int(input("Enter the length of the rectangle: "))
    areaTemp = areaOfRectangle(height, length)
    perimeterTemp = perimeterOfRectangle(height, length)
    print(f"The area of the rectangle is {areaTemp} and the perimeter is {perimeterTemp}.")
elif shapeChoice == "Parallelogram":
    height = int(input("Enter the height of the parallelogram: "))
    length = int(input("Enter the length of the parallelogram: "))
    areaTemp = areaOfParallelogram(height, length)
    perimeterTemp = perimeterOfParallelogram(height, length)
    print(f"The area of the parallelogram is {areaTemp} and the perimeter is {perimeterTemp}.")
elif shapeChoice == "Triangle":
    height = int(input("Enter the height of the triangle: "))
    length = int(input("Enter the length of the first side the triangle: "))
    side2 = int(input("Enter the length of the second side of the triangle: "))
    side3 = int(input("Enter the length of the third side of the triangle: "))
    areaTemp = areaOfTriangle(height, length)
    perimeterTemp = perimeterOfTriangle(length, side2, side3)
    print(f"The area of the triangle is {areaTemp} and the perimeter is {perimeterTemp}.")
elif shapeChoice == "Sphere":
    rad = int(input("Enter the radius of the sphere: "))
    volumeTemp = volumeOfSphere(rad)
    print(f"The volume of the sphere is {volumeTemp}.")
