# If you want to store anything other than text, you need to use a binary file (.dat) (ex. for records)
# opening is the same, but:
# instead of readline, use getrecord
# instead of writeline, use putrecord

# You don't have to learn to use binary files in python because it's not in the syllabus and you need the pickle library

import pickle
# (load and dump)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alex", 16)
student2 = Student("Fiona", 14)

file = open("Student.dat", 'wb') #wb is write mode for binary
pickle.dump(student1, file) #dumping/writing student1 into the file 
pickle.dump(student2, file)
file.close()

file = open("Student.dat", 'rb') #rb is read mode for binary
tempStudent = pickle.load(file) #loading/reading the file into tempStudent 
tempStudent2 = pickle.load(file)
file.close()

print(tempStudent.name, tempStudent.age)
print(tempStudent2.name, tempStudent2.age)