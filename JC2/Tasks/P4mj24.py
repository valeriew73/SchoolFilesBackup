def ReadWords(filename):
    global NumOfAnswers, WordArray
    try:
        FileHandle = open(filename, 'r')
        WordArray = FileHandle.read().strip().split()
        NumOfAnswers = len(WordArray) - 1
        FileHandle.close()
    except FileNotFoundError:
        print("File is not found.")

difficulty = str(input("Please enter the chosen difficulty (easy, medium or hard): ")).lower()

match difficulty:
    case "easy": ReadWords("Easy.txt")
    case "medium": ReadWords("Medium.txt")
    case "hard": ReadWords("Hard.txt")
    case _: difficulty = str(input("Please enter a valid chosen difficulty (easy, medium or hard): "))

def Play():
    print("The word is:", WordArray[0])
    print(f"There are {NumOfAnswers} words that can be made with 3 or more letters")
    Loop = True
    Count = 0
    while Loop:
        UserAns = str(input("Please enter a word (Enter 'no' to stop): "))
        if UserAns == "no":
            print(f"Answers found: {Count/NumOfAnswers * 100}%")
            print("Answers not found: ")
            for answer in WordArray[:-1]:
                if answer != "":
                    print(answer)
            break
        elif UserAns in WordArray[:-1]:
            print(f"{UserAns} is an answer.")
            Count += 1
            WordArray[WordArray.index(UserAns)] = ""
        else:
            print(f"{UserAns} is not an answer.")

def ReadWords():
    ReadWords()
    Play()


class Node:
    def __init__(self, Data):
        self.__LeftPointer = -1 #of type integer
        self.__Data = Data #of type integer
        self.__RightPointer = -1 #of type integer
    
    def GetLeft(self):
        return self.__LeftPointer
    
    def GetRight(self):
        return self.__RightPointer
    
    def GetData(self):
        return self.__Data
    
    def SetLeft(self, NewLeftPointer):
        self.__LeftPointer = NewLeftPointer
    
    def SetRight(self, NewRightPointer):
        self.__RightPointer = NewRightPointer
    
    def SetData(self, NewData):
        self.__Data = NewData

class TreeClass:
    def __init__(self):
        self.Tree = [Node(-1) for i in range(20)] #array[0:19] of type node
        self.FirstNode = -1 #of type integer
        self.NumberNodes = 0 #of type integer
    
    def InsertNode(self, NewNode):
        if self.NumberNodes == 0:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            self.Tree[self.NumberNodes] = NewNode
            ItemPointer = self.FirstNode
            while ItemPointer != -1:
                PreviousPointer = ItemPointer
                if self.Tree[ItemPointer].GetData() > NewNode.GetData():
                    left = True
                    ItemPointer = self.Tree[ItemPointer].GetLeft()
                elif self.Tree[ItemPointer].GetData() < NewNode.GetData():
                    left = False
                    ItemPointer = self.Tree[ItemPointer].GetRight()
            if left == True:
                self.Tree[PreviousPointer].SetLeft(self.NumberNodes)
            else:
                self.Tree[PreviousPointer].SetRight(self.NumberNodes)
            self.NumberNodes += 1

    def OutputTree(self):
        if self.NumberNodes == 0:
            print("No nodes")
        else: 
            for i in range(self.NumberNodes):
                node = self.Tree[i]
                print(f"Left pointer: {node.GetLeft()}, Data: {node.GetData()}, Right pointer: {node.GetRight()}")
            
TheTree = TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))

TheTree.OutputTree()


