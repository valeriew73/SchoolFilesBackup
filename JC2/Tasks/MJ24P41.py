DataStored = [0 for i in range(20)] #array[0:20] of type integer
NumberItems = 0 #of type integer

def Initialise():
    global NumberItems, DataStored
    NumberItems = int(input("Please input the quantity of numbers you would like to enter: "))
    while NumberItems < 1 or NumberItems > 20:
        NumberItems = int(input("Invalid input. Please enter a number between 1 and 20 inclusive: "))
    for i in range(NumberItems):
        DataStored[i] = int(input("Enter a number: "))

NumberItems = 0
Initialise()
for i in range(NumberItems):
    print(DataStored[i], end=" ")
print()

def BubbleSort():
    global DataStored, NumberItems
    top = NumberItems-1
    swap = True
    while swap and top > 0:
        for i in range(top):
            if DataStored[i] > DataStored[i+1]:
                temp = DataStored[i]
                DataStored[i] = DataStored[i+1]
                DataStored[i+1] = temp
                swap = True
            else: swap = False
        top -= 1

BubbleSort()
for i in range(NumberItems):
    print(DataStored[i], end=" ")
print()

def BinarySearch(DataToFind):
    global DataStored, NumberItems
    high = NumberItems 
    low = 0
    while high <= low:
        mid = int((high + low) / 2)
        if DataStored[mid] > DataToFind: 
            high = mid-1
        elif DataStored[mid] < DataToFind: 
            low = mid+1
        elif DataStored[mid] == DataToFind: 
            return mid
    return -1


DataToFind = int(input("Please enter a number to search: "))
print(BinarySearch(DataToFind))

