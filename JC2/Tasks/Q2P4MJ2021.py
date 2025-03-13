#question 1
# 1. a)
class node:
    def __init__(self, data, nextNode):
        self.data = data #of type integer
        self.nextNode = nextNode #of type integer

# b)
linkedList = [node(0, -1) for i in range(10)]
linkedList = [node(1, 1),
              node(5, 4),
              node(6, 7),
              node(7, -1),
              node(2, 2),
              node(0, 6),
              node(0, 8),
              node(56, 3),
              node(0, 9),
              node(0, -1)]

# c)
startPointer = 0
emptyList = 5
def outputNodes(linkedList, startPointer):
    

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
