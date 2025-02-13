
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