# If you want to store anything other than text, you need to use a binary file (.dat) (ex. for records)
# opening is the same, but:
# instead of readline, use getrecord
# instead of writeline, use putrecord

# You don't have to learn to use binary files in python because it's not in the syllabus and you need the pickle library

import pickle
# (load and dump)


class Studentrecord:
    def __init__(self, studentID, studentClass):
        self.studentID = studentID
        self.studentClass = studentClass

