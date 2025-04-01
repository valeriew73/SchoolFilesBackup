def Unknown(x, y):
    if x < y:
        print(x + y)
        return Unknown(x+1, y)*2
    elif x == y:
        return 1
    else:
        print(x + y)
        return Unknown(x-1, y)//2

print("Recursive: ")
print(f"X: 10 \nY: 15")
print(f"Return Value: {Unknown(10, 15)}")
print(f"X: 10 \nY: 10")
print(f"Return Value: {Unknown(10, 10)}")
print(f"X: 15 \nY: 10")
print(f"Return Value: {Unknown(15, 10)}")

def IterativeUnknown(x, y):
    returnValue = 1
    while x != y:
        if x < y:
            print(x + y)
            x += 1
            returnValue *= 2
        else:
            print(x + y)
            x -= 1
            returnValue //= 2
    return returnValue

print("Iterative: ")
print("X: 10 \nY: 15")
print(f"Return Value: {IterativeUnknown(10, 15)}")
print("X: 10 \nY: 10")
print(f"Return Value: {IterativeUnknown(10, 10)}")
print("X: 15 \nY: 10")
print(f"Return Value: {IterativeUnknown(15, 10)}")

class Picture:
    def __init__(self, PDescription, PWidth, PHeight, PFrameColour):
        self.__Description = PDescription #of type string
        self.__Width = PWidth #of type integer
        self.__Height = PHeight #of type integer
        self.__FrameColour = PFrameColour #of type string

    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, new_description):
        self.__Description = new_description
    
PictureArray = [Picture("",0,0,"") for i in range(100)]

def ReadData():
    FileHandle = open("Pixtures.txt", 'r')
    
    PictureObject = Picture()