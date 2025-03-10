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
    def GetFrameColour(self):
        return self.__FrameColour

    def SetDescription(self, new_description):
        self.__Description = new_description
    


PictureArray = [Picture("",0,0,"") for i in range(100)]

