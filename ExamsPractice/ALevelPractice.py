# 1. Searches:
myArray = [2, 5, 1, 3, 4]
# - Linear Search:
def LinearSearch():
    global myArray
    found = False
    index = 0
    searchval = int(input("Please enter a value to search:"))
    while not found and index <= len(myArray):
        if searchval == myArray[index]:
            print(f"{searchval} has been found at index {index}.")
            found = True
        else: index += 1
    if not found:
        print(f"{searchval} was not found.")

# - Binary Search:
mySortedArray = [1, 2, 3, 4, 5]
def BinarySearch():
    global mySortedArray
    high = len(myArray)
    low = 0
    found = False
    searchval = int(input("Please enter a value to search:"))

    while (not found) and (high != low):
        mid = (high + low) // 2
        if mySortedArray[mid] > searchval:
            high = mid-1
        elif mySortedArray[mid] < searchval:
            low = mid+1
        else:
            found = True
            print(f"{searchval} has been found at index {mid}.")
    if not found:
        print(f"{searchval} was not found.")


# 2. Sorts:
# - Bubble sort:
def BubbleSort():
    global myArray
    swap = True
    top = len(myArray)

    while swap and top > 0:
        for i in range(0, top-1):
            if myArray[i] > myArray[i+1]:
                temp = myArray[i]
                myArray[i] = myArray[i+1]
                myArray[i+1] = temp
                swap = True
            else: swap = False
        top -= 1

# - Insertion sort
def InsertionSort():
    global myArray
    for i in range(1, len(myArray)):
        j = i-1
        while (j >= 0) and myArray[j] > myArray[i]:
            temp = myArray[j]
            myArray[j] = myArray[j+1]
            myArray[j+1] = temp
            j -= 1

# 3. ADTs:
# - Stacks = basePointer, topPointer, stackful (push, pop, peak)
stack = [None for i in range(7)]
basePointer = 0
topPointer = -1
Stackful = len(stack) - 1

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
    if topPointer > Stackful:
        print("Unable to push, Stack is full.")
    else: 
        topPointer += 1
        stack[topPointer] = pushelement

def peak():
    return stack[topPointer]

# - Queues
Queue = [None for i in range(7)]
frontPointer = 0
rearPointer = -1
Queuefull = len(Queue)
QueueLength = 0 


def Enqueue(enqueueele):
    global QueueLength, rearPointer
    if QueueLength < Queuefull: # Checks whether the queue is full
        if rearPointer == Queuefull - 1: # The queue is not full so there is still space to enqueue but the last element is at the end of the queue
            rearPointer = 0 # Rear pointer points to the first space of the queue again
        else:
            rearPointer += 1
        Queue[rearPointer] = enqueueele
        QueueLength += 1
    else:
        print("Unable to enqueue, Queue is full.")


def Dequeue():
    global QueueLength, frontPointer
    if QueueLength > 0: # Checks whether the queue has items in it
        dequeueele = Queue[frontPointer]
        if frontPointer == Queuefull - 1:
            frontPointer = 0
        else:
            frontPointer += 1
        QueueLength -= 1
        return dequeueele
    else:
        print("Unable to dequeue, queue is empty.")

# - Linked list
llistData = [5, 6, 9, 3, None, None, None]
llistPointers = [-1, 0, 1, 2, 5, 6, -1] # Initialised: [1, 2, 3, 4, 5, 6, -1]
startPointer = 3
heapPointer = 4

def addtoLlist(item):
    global startPointer, heapPointer
    print(f"Before add: linked list data: {llistData}, linked list pointers: {llistPointers}")
    if  heapPointer == -1:
        print("Linked list is full.")
    else:
        temp = startPointer
        startPointer = heapPointer
        llistData[startPointer] = item
        heapPointer = llistPointers[heapPointer]
        llistPointers[startPointer] = temp
    print(f"After: linked list data: {llistData}, linked list pointers: {llistPointers}")

# addtoLlist(8)
# addtoLlist(3)
# addtoLlist(5)
# addtoLlist(9)

def delfromLlist(item):
    global startPointer, heapPointer
    print(f"Before delete: linked list data: {llistData}, linked list pointers: {llistPointers}")
    if  startPointer == -1:
        print("Linked list is empty.")
    else:
        itemPointer = -1
        i = startPointer
        while i != -1:
            if item == llistData[i]:
                itemPointer = i
            i = llistPointers[i]

        if itemPointer == -1:
            print("Item is not found.")
        else:
            llistData[itemPointer] = None
            llistPointers[startPointer] = llistPointers[itemPointer]
            llistPointers[itemPointer] = heapPointer
            heapPointer = itemPointer
            print(f"After: linked list data: {llistData}, linked list pointers: {llistPointers}")

item = int(input("Please enter an item to delete: "))
delfromLlist(item)

# - Binary Trees
binary_tree = [[1, 9, 2], 
               [3, 7, -1], 
               [4, 13, 5], 
               [-1, 5, -1],
               [-1, 12, -1],
               [-1, 15, -1],
               [-1, 7, -1],
               [-1, 8, -1], 
               [-1, 9, -1], 
               [-1, -1, -1]]

free_pointer = 5
root_pointer = 0

def searchval(val_to_search):
    node_index = root_pointer
    while node_index != -1 and val_to_search != binary_tree[node_index][1]:
        if val_to_search < binary_tree[node_index][1]:
            node_index = binary_tree[node_index][0] # left child
        else:
            node_index = binary_tree[node_index][2] # right child

    return node_index 

val_to_search = int(input("Please enter a value to search: "))
print(searchval(val_to_search))

def insert_to_tree(element):
    global free_pointer
    global root_pointer
    # Check if there's enough space in the tree (if free pointer = -1: tree is full)
    if free_pointer == -1:
        print("The binary tree is full, cannot insert an element.")
    else:
        new_item_pointer = free_pointer
        free_pointer = binary_tree[new_item_pointer][1]
        item_pointer = root_pointer
        if root_pointer == -1: # no root
            root_pointer = new_item_pointer
        else:
            while item_pointer != -1:
                previous_pointer = item_pointer
                if element < binary_tree[item_pointer][1]:
                    left = True
                    item_pointer = binary_tree[item_pointer][0]
                elif element > binary_tree[item_pointer][1]:
                    left = False
                    item_pointer = binary_tree[item_pointer][2]
            if left == True:
                binary_tree[previous_pointer][0] = new_item_pointer
            else: binary_tree[previous_pointer][2] = new_item_pointer
        
        binary_tree[new_item_pointer][1] = element


# 4. Recursion

# 5. File Handling

# 6. Exception Handling

# 7. OOP

class Class:
    def __init__(self, name):
        self.__name = name
    
    def getter(self):
        return self.__name
    
    def setter(self, name):
        self.__name = name 

