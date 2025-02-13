Num1 = int(input("Please enter the first number: "))
Num2 = int(input("Please enter the second number: "))
Num3 = int(input("Please enter the third number: "))
if Num1 > Num2:
    if Num1 > Num3:
        print(Num1, "is the greatest number")
    else:
        print(Num3, "is the greatest number")  
elif Num2 > Num3:
    print(Num2, "is the greatest number")