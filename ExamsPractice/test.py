try:
    FileHandle = open("Stack.txt", 'r')
    StackArr = FileHandle.read().strip().split()
    List = []
    FileHandle.close()
except FileNotFoundError:
    print("File is not found.")
def RPNToInfix():
    global StackArr, List

