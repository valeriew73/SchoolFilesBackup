StudentNames = ["","","","","","","","","",""] #student names is an array of data type str of 10 elements
StudentNames = [None, None, None, None, None, None, None, None, None, None]
StudentNames = [None for i in range(10)] #student names is an array of data type str of 10 elements
StudentMarks = [0 for i in range(10)] #student marks is an array of data type int of 10 elements


for index in range(10):
    StudentNames[index] = str(input("Enter Student Name: "))
    StudentMarks[index] = str(input("Enter Student Mark: "))

for index in range(10):
    print(StudentNames[index])
    print(StudentMarks[index])
    
print(StudentNames)
print(StudentMarks)

#Search algorithm

searchStudent = str(input("Enter a student name to search: "))
found = False

for index in range(10):
    if searchStudent[index] == StudentNames[index]: 
        found = True
    else: found = False

if found == True: 
    print(f"{searchStudent} was found and the student has scored {StudentMarks[index]}")
else: print(f"{searchStudent} was not found")


