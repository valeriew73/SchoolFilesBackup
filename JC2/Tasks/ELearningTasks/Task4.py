
#1 a)
DataArray = [None for i in range(100)]

# b)
def ReadFile():
    try:
        FileHandle = open("C:/Users/School and work/Documents/GitHub/SchoolFilesBackup/JC2/Tasks/ELearningTasks/IntegerData.txt", 'r')
        for index in range(100):
            TextFromFile = FileHandle.readline().strip()
            DataArray[index] = int(TextFromFile)
        FileHandle.close
    except FileNotFoundError:
        print("Sorry, the file you are trying to open does not exist. ")

# c)
def FindValues():
    searchnum = int(input("Please enter a number to search for in the array: "))
    while searchnum < 1 and searchnum > 100:
        searchnum = int(input("Number must be a whole number between 1 and 100 inclusive. Please re-enter: "))
    
    foundCount = 0
    for i in range(len(DataArray)):
        if searchnum == DataArray[i]:
            foundCount += 1
    return foundCount

# d) i)
ReadFile()
print(f"The number was found {FindValues()} times.")

# d) e)
def BubbleSort():
    swap = True
    top = len(DataArray)
    while (swap == True) or (top > 0):
        for index in range(0, top - 1):
            if DataArray[index] > DataArray[index + 1]:
                temp = DataArray[index]
                DataArray[index] = DataArray[index + 1]
                DataArray[index + 1] = temp
                swap = True
            else: swap = False
        top = top - 1
    print(DataArray)

BubbleSort()
