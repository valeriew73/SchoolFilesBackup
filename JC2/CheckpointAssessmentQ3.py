# 3. a) i)
myArray = [-1 for i in range(10)]

# b)
def ReadNumbers():
    global myArray
    FileHandle = open("Numbers.txt", 'r')
    for i in range(10):
        myArray[i] = FileHandle.readline().strip()
    FileHandle.close()

# c)
def OutputNumbers():
    global myArray
    for i in range(10):
        print(myArray[i])

# d)
ReadNumbers()
OutputNumbers()

# e)
def InsertionSort():
    global myArray
