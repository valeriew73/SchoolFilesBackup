NumbersArray = [" " for i in range(10)]
FileHandle = open("Numbers.txt", "r")
for count in range(10):
    NumbersFromFile = FileHandle.readline().strip() 
    NumbersArray[count] = NumbersFromFile
FileHandle.close
for index in range(10):
    print(NumbersArray)


lb = 0
ub = 9
Top = 0

Swap = True
while Swap == True and Top <= ub:
    Swap = False
    for Index in range(lb, ub - Top):
        if NumbersArray[Index] < NumbersArray[Index + 1]:
            Temp = NumbersArray[Index]
            NumbersArray[Index] = NumbersArray[Index + 1]
            NumbersArray[Index + 1] = Temp
            Swap = True
        else:
            Swap = False
        print(NumbersArray)
    Top = Top + 1
    