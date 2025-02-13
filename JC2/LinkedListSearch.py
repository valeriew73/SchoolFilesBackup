# Search for an item in a linked list (the only algorithm that can be used is linear search because binary search requires the linked list to be ordered, 
# linked list can only be traversed sequentially)

llistData = [5, 6, 9, 3, None, None, None]
llistPointers = [-1, 0, 1, 2, 5, 6, -1] # Initialised: [1, 2, 3, 4, 5, 6, -1]
startPointer = 3
heapPointer = 4

searchele = int(input("Please enter an element to search: "))
def searchll(searchele):
    i = startPointer
    while i != -1:
        if searchele == llistData[i]:
            return i
        i = llistPointers[i]
    
print(f"{searchele} is found at pointer {searchll(searchele)}.")