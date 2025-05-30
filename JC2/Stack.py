# Operates on the LIFO protocol

# Abstract data types, unlike concrete data types hide their implementation from the user (abstract)

# Operations: Push, Pop and Peak (to get the element on the top of the stack)

# Pointers: Base (points to the base position in the stack), Top (points to the top element in the stack)


#Declare the stack as an array (it has a fixed length)
stack = [None for i in range(7)]
basePointer = 0 #index of the first element in the stack
topPointer = -1 #index of the top element in the stack
#topPointer starts off as basePointer-1 when it is empty, so when one element is pushed in, it will be equal to the basePointer
Stackful = len(stack) - 1 #the last index of the stack- when the stack is full, the topPointer points to this index

def pop():
    global topPointer
    if topPointer == basePointer-1: #check whether the stack has any elements in it
        print("Unable to pop, stack is empty.")
    else:
        popelement = stack[topPointer]
        topPointer -= 1
        return popelement

def push(pushelement):
    global topPointer
    if topPointer == Stackful:
        print("Unable to push, Stack is full.")
    else: 
        topPointer += 1
        stack[topPointer] = pushelement

def peak():
    return stack[topPointer]


push(5)
print(stack)
print(pop())
print(stack)