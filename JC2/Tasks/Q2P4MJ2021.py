#question2
arrayData = [None for i in range(10)]
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

#b) i)
def linearsearch(searchint):
    index = 0
    found = False
    while index < len(arrayData) and found == False:
        if searchint == arrayData[index]:
            found = True
        index += 1

    return found

#b) ii)
searchele = int(input("Please enter an integer value to search: "))
if linearsearch(searchele):
    print("The search value was found.")
else:
    print("The search value was not found.")


#c)
def bubbleSort():
    theArray = arrayData
    for x in range(0, len(arrayData)-1):
        for y in range(0, len(arrayData)-1):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y+1] = temp
