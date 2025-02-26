#1 a)
StackData = [None for i in range(10)]
StackPointer = 0

# b)
def PrintStack():
    print("Stack Pointer: ", StackPointer)
    print("Stack: ")
    for index in range(StackPointer-1, -1, -1):
        print(StackData[index])

# c)
def Push(PushElement):
    global StackPointer
    if StackPointer > len(StackData) - 1:
        return False
    else: 
        StackData[StackPointer] = PushElement
        StackPointer += 1
        return True
    
# d) i)
for i in range(11):
    PushElement = int(input("Please enter an element to push: "))
    Added = Push(PushElement)
    if Added == True:
        print(f"{PushElement} has been added to the stack.")
    else: print(f"Stack is full. {PushElement} has not been added to the stack.")

print("Stack:", StackData)

# e) i)
def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        PopElement = StackData[StackPointer-1]
        StackPointer -= 1
        return PopElement

# ii)
print("Popped element:", Pop())
print("Popped element:", Pop())
PrintStack()