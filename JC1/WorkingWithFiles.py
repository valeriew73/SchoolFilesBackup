# Always use exception handling when handling files so that if the file is not found, the program will not crash
try:
    # OPENFILE "StudentNames.txt" FOR WRITE
    #Files can be opened in read, write or append mode (r,w) or a) (don't use r+ mode because it opens the file for both read and write mode)
    FileHandle = open("StudentNames.txt", "w")

    #write operations
    FileHandle.write("Line 1\n")
    FileHandle.write("Line 2\n") #\n makes an enter (goes to the next line)

    #Every opened file must be closed when you are done with it
    FileHandle.close()
except FileNotFoundError:
    print("File was not found.")

# The previously written lines are overwritten once the file is opened again in write mode
FileHandle = open("StudentNames.txt", "w")
FileHandle.write("Line 3\n") 
FileHandle.close()
# Append mode can be used to add more lines
FileHandle = open("StudentNames.txt", "a")
FileHandle.write("Line 4\n") 
FileHandle.close()

# Read operation 
TextFromFileArr = [" ", " "]
FileHandle = open("StudentNames.txt", "r")
#.readline only reads one line at a time, and goes to the next line automatically everytime it is run
#strip removes any spaces made from enter (which is a \n character)
#rstrip only removes the spaces coming from the right while lstrip deletes from the left
for count in range(2):
    TextFromFile = FileHandle.readline().strip() 
    TextFromFileArr[count] = TextFromFile
FileHandle.close
for index in range(2):
    print(TextFromFile)

#.readlines puts the entire file in an array of strings
file = open("Numbers.txt", "r")
myArr = file.readlines()
total = 0
for totalcount in range(10):
    total += int(myArr[totalcount].strip())
for index in range(2):
    print(total)
file.close()

myArr = [0 for i in range(10)]
file = open("Numbers.txt", "r")
for i in range(10):
    text = file.readline()
    myArr[i] = text.strip()
#.read puts the entire file in one variable
file.close()