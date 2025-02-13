PI = 3.141572653589793238462643323
# constants have to be in all capital letters. 
Radius = float(input("Enter the Radius of the circle (cm): "))
if Radius <= 0:
    print("Error: Radius can't be less than or equal to 0") 
else:
    Area = PI * Radius * Radius 
    print("The area of a circle with radius ", Radius, "is", Area, "cm")
