NumberArray = [100, 85, 644, 22, 15, 8, 1] #array[0:6] of type integer
LastItem = 0 #of type integer
CheckItem = 0 #of type integer
LoopAgain = False #of type boolean

def RecursiveInsertion(IntegerArray, NumberElements:int):
    if NumberElements <= -1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements-2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem = CheckItem-1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray

ReturnedArr = RecursiveInsertion(NumberArray, 7)
print("Recursive")
print(ReturnedArr)
    
def IterativeInsertion(IntegerArray, NumberElements:int):
    for i in range(1, NumberElements):
        key = IntegerArray[i]
        j = i-1
        while j != -1 and key < IntegerArray[j]:
            temp = IntegerArray[j]
            IntegerArray[j] = IntegerArray[j+1]
            IntegerArray[j+1] = temp
            j -= 1
    return IntegerArray

ReturnedArr2 = IterativeInsertion(NumberArray, 7)
print("Iterative")
print(ReturnedArr2)

def BinarySearch(IntegerArray, First, Last, ToFind):
    if ToFind not in IntegerArray:
        return -1
    else:
        found = False
        while First != Last or not found:
            mid = (First + Last) // 2
            if ToFind < IntegerArray[mid]:
                return BinarySearch(IntegerArray, First, mid-1, ToFind)
            elif ToFind > IntegerArray[mid]:
                return BinarySearch(IntegerArray, mid+1, Last, ToFind)
            elif ToFind == IntegerArray[mid]:
                found = True
                return mid

res = BinarySearch(ReturnedArr2, 0, 6, 644)
if res == -1:
    print("Not found.")
else:
    print(f"Search value was found at index {res}.")