# Question 1
class Employee:
    def __init__(self, Name, EmployeeID, Department):
        self.__Name = Name #of type string
        self.__EmployeeID = EmployeeID #of type integer
        self.__Department = Department #of type string

    def GetName(self):
        return self.__Name
    
    def GetEmployeeID(self):
        return self.__EmployeeID
    
    def GetDepartment(self):
        return self.__Department

    def ChangeDepartment(self, NewDepartment):
        self.__Department = NewDepartment

    def SetName(self, NewName): #the setters aren't in the class diagram but the properties are private
        self.__Name = NewName
    
    def SetEmployeeID(self, NewID):
        self.__EmployeeID = NewID

    
AllEmployees = [Employee(None, -1, None) for i in range(10)]
FileHandle = open("EmployeeFile.txt", 'r')
for index in range(len(AllEmployees)):
    AllEmployees[index].SetName(FileHandle.readline().strip())
    AllEmployees[index].SetEmployeeID(FileHandle.readline().strip())
    AllEmployees[index].ChangeDepartment(FileHandle.readline().strip())


Found = False
while not Found:
    index = 0
    NameToSearch = input("Please enter the employee name to search: ")
    while index < len(AllEmployees):
        if AllEmployees[index].GetName() == NameToSearch:
            Found = True
        else: 
            index += 1


Valid = False
while not Valid:
    Action = input("Enter a letter (P = print, D = change department): ")
    if Action == 'P':
        Valid = True
        print(f"Name: {AllEmployees[index].GetName()}")
        print(f"EmployeeID: {AllEmployees[index].GetEmployeeID()}")
        print(f"Department: {AllEmployees[index].GetDepartment()}")
    elif Action == 'D':
        Valid = True
        NewDepartment = input("Please enter a new Department: ")
        AllEmployees[index].ChangeDepartment(NewDepartment)
        print(f"{AllEmployees[index].GetName()} ({AllEmployees[index].GetEmployeeID()}) has changed department to {AllEmployees[index].GetDepartment()}.")


# Question 2
QueueData = [None for i in range(8)] #array of type integer
QueueFront = 0
QueueRear = -1
QueueLength = 0

def DisplayQueue():
    global QueueData, QueueFront, QueueRear, QueueLength
    print(QueueData)
    print(f"Queue Length: {QueueLength}")
    print(f"Queue Front: {QueueFront}")
    print(f"Queue Rear: {QueueRear}")


def Enqueue(EnqueueEle):
    global QueueData, QueueFront, QueueRear, QueueLength
    if QueueLength >= len(QueueData):
        return False
    else:
        if QueueRear == len(QueueData)-1:
            QueueRear = 0
        else: 
            QueueRear += 1
        QueueData[QueueRear] = EnqueueEle
        QueueLength += 1
        return True

for i in range(9):
    EnqueueEle = int(input("Please enter a number: "))
    Added = Enqueue(EnqueueEle)
    if Added:
        print(f"{EnqueueEle} has been added.")
    else:
        print(f"{EnqueueEle} has not been added.")
    
DisplayQueue()

def Dequeue():
    if QueueLength == 0:
        return -1
    else:
        DequeueEle = QueueData[QueueFront]
        if QueueFront == len(QueueData)-1:
            QueueFront = 0
        else: 
            QueueFront += 1
        QueueLength -= 1
        return DequeueEle

Dequeue()
Dequeue()
DisplayQueue()

# Question 3
myArray = [-1 for i in range(10)] #of type integer

def ReadNumbers():
    NumbersFile = open("Numbers.txt", 'r')
    for i in range(10):
        Number = NumbersFile.readline().strip()
        myArray[i] = Number
    NumbersFile.close()
    
def OutputNumbers():
    for ele in myArray:
        print(ele)

ReadNumbers()
OutputNumbers()

def InsertionSort():
    for i in range(1, len(myArray)):
        key = myArray[i]
        j = i-1
        while j >= 0 and myArray[j] > key:
            temp = myArray[j]
            myArray[j] = myArray[j+1]
            myArray[j+1] = temp
            j -= 1
    
def WriteSorted():
    NumbersFile = open("Numbers.txt", 'w')
    for ele in myArray:
        NumbersFile.write(ele)
    NumbersFile.close()