DataStored = [0 for i in range(20)] #array[0:20] of type integer
NumberItems = 0 #of type integer

def Initialise():
    QuantityToEnter = int(input("Please input the quantity of numbers you would like to enter: "))
    while QuantityToEnter < 1 or QuantityToEnter > 20:
        QuantityToEnter = int(input("Invalid input. Please enter a number between 1 and 20 inclusive: "))
    for i in range(QuantityToEnter):
        DataStored[i] =int(input("Enter a number: "))

NumberItems = 0
Initialise()
for ele in DataStored:
    print(ele)
