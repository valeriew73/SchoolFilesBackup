
#1 a)
Jobs = [[None for i in range(2)] for i in range(100)]
NumberOfJobs = None

# b)
def Initialise():
    global NumberOfJobs
    NumberOfJobs = 0
    for row in range(len(Jobs)):
        for col in range(len(Jobs[row])):
            Jobs[row][col] = -1
        
# c)
def AddJob(job_number: int, priority: int):
    global NumberOfJobs
    if NumberOfJobs < len(Jobs):
        Jobs[NumberOfJobs] = [job_number, priority]
        NumberOfJobs += 1
        print("Added")
    else:
        print("Not Added")

# d)
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

# e)
def InsertionSort():
    for index in range(1, NumberOfJobs):
        key = Jobs[index][1]
        j = index - 1
        while j >= 0 and Jobs[j][1] > key:
            temp = Jobs[j]
            Jobs[j] = Jobs[j+1]
            Jobs[j+1] = temp
            j -= 1

# f)
def PrintArray():
    for index in range(NumberOfJobs):
        print(Jobs[index][0], "priority", Jobs[index][1])

# g)
InsertionSort()
PrintArray()

