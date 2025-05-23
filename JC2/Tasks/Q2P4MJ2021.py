
#question 1
#1. a)
class node:
    def __init__(self, data, nextNode):
        self.data = data #of type integer
        self.nextNode = nextNode #of type integer

#b)
#declaring a 1D array of type node, called linkedList:
linkedList = [node(0, -1) for i in range(10)]
#initialising the array:
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
#declaring the pointers:
startPointer = 0
emptyList = 5

#c) i)
def outputNodes(linkedList, startPointer):
    node_index = startPointer
    while linkedList[node_index].nextNode != -1:
        print(linkedList[node_index].data)
        node_index = linkedList[node_index].nextNode
    print(linkedList[node_index].data)

outputNodes(linkedList, startPointer)

#d) i)
def addNode(linkedList, startPointer, emptyList):
    data = input("Enter the data to be added: ")
    if emptyList == -1:
        return False
    else:
        node_index = startPointer
        while linkedList[node_index].nextNode != -1:
            node_index = linkedList[node_index].nextNode
        linkedList[node_index].nextNode = emptyList
        new_emptyList = linkedList[emptyList].nextNode
        linkedList[emptyList] = node(int(data), -1)
        emptyList = new_emptyList
        return True

#d) ii)
print("Linked list before adding: ")
outputNodes(linkedList, startPointer)
added_state = addNode(linkedList, startPointer, emptyList)

if added_state == True:
    print("The node has been successfully added.")
else: 
    print("The node has not been added because there are no empty nodes.")

print("Linked list after: ")
outputNodes(linkedList, startPointer)

#question 2
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

#3. a)
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question #of type string
        self.__answer = answer #of type integer
        self.__points = points #of type integer

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, userAnswer):
        if userAnswer == self.__answer:
            return True
        else: return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return int(self.__points)//2
        elif attempts == 3 or attempts == 4:
            return int(self.__points)//4
        else: return 0
          
    def setQuestion(self, newQuestion):
        self.__question = newQuestion
        
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer

    def setPoints(self, newPoints):
        self.__question = newPoints
    
#3. b)
arrayTreasure = [] #of type TreasureChest
def readData():
    try:
        file = open("C:/Users/School and work/Documents/GitHub/SchoolFilesBackup/JC2/Tasks/TreasureChestData.txt", 'r')
        for i in range(5):
            question = file.readline().strip()
            answer = int(file.readline().strip())
            points = int(file.readline().strip())
            arrayTreasure.append(TreasureChest(question, answer, points))
        file.close()
    except FileNotFoundError:
        print("File is not found.")

# c) iv)
readData()

questionNumber = int(input("Please enter a number between 1 and 5: "))
print(f"Question: {arrayTreasure[questionNumber-1].getQuestion()}")
correct = False
attempts = 0
while not correct:
    userAnswer = int(input("Enter your answer here: "))
    correct = arrayTreasure[questionNumber-1].checkAnswer(userAnswer)
    attempts += 1

print(f"You have been awarded {arrayTreasure[questionNumber-1].getPoints(attempts)} points.")

