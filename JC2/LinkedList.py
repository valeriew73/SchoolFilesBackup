# The linked list is already initialised
llistData = [5, 6, 9, 3, None, None, None]
llistPointers = [-1, 0, 1, 2, 5, 6, -1] # Initialised: [1, 2, 3, 4, 5, 6, -1]
startPointer = 3
heapPointer = 4

i = startPointer
while i != -1:
    print(llistData[i])
    i = llistPointers[i]

