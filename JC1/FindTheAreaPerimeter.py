# Write a program to calculate the area or perimeter of a circle.
# Use procedures and/or functions for each of the following:
# 1. Input and validate the radius 
# 2. Calculate the area
# 3. Calculate the perimeter
# 4. Output the result
# 5. The main program should give the user a choice to either calculate the area or perimeter

pi = 3.141592

def area(radius):
    area = pi * radius * radius
    print(f"The area of the circle is {area}cm^2.")

def perimeter(radius):
    perimeter = 2 * pi * radius
    print(f"The perimeter of the circle is {perimeter}cm.")

radius = float(input("Please enter the radius of the circle (cm) (Must be > 0): "))

while radius <= 0: 
    print("Invalid radius.")
    radius = float(input("Please reenter the radius of the circle (cm) (Must be > 0): "))

choice = str(input("Would you like to calculate the area or the perimeter? "))

if choice == "area" or "Area":
    area(radius)
elif choice == "perimeter" or "Perimeter":
    perimeter(radius)