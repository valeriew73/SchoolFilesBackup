

MyArr = [2, 3, 6, 8, 19, 23, 27, 58, 84, 92]
Found = False

SearchEle = input("Please enter a value to search: ")
low = 1
high = len(MyArr)

while (Found == False) and (high != low):
    mid = (low + high) // 2
    if SearchEle == MyArr[mid]:
        Found = True
    elif SearchEle < MyArr[mid]:
        high = mid - 1
    elif SearchEle > MyArr[mid]:
        low <- mid + 1

if Found == True:
    print("Found at", mid)
else:
    print("Not found")
