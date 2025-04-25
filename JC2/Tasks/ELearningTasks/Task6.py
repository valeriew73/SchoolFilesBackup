# 1 a) i)
DataFile = open("C://Users/School and work/Documents/GitHub/SchoolFilesBackup/JC2/Tasks/ELearningTasks/Data.txt", 'r')
DataArray = []

# ii)
for i in range(25):
    DataArray.append(DataFile.readline().strip())
print(DataArray)
DataFile.close()

# b) i)
def PrintArray(IntArray):
    NumString = ""
    for num in IntArray:
        NumString += f"{num} "
    print(NumString)

# ii)