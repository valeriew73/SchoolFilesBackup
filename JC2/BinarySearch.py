#binary search is much more efficient than linear search because it runs in O(log2n) complexity 
#the only disadvantage is that the array has to be sorted before searching 
MyArr = [2, 3, 6, 8, 19, 23, 27, 58, 84, 92]
Found = False

SearchEle = int(input("Please enter a value to search: "))
low = 0 #the index of the first element in the array being searched
high = len(MyArr) #the index of the last element in the array being searched

while (Found == False) and (high != low): #terminates when the element being searched is found / when the whole array is searched
    #binary search keeps cutting the array in half, and discarding the half that the search element is not in 
    mid = (low + high) // 2 #gets the index of the middle element of the searched array
    #comparison of the middle element with the search element
    if SearchEle == MyArr[mid]:
        Found = True
    elif SearchEle < MyArr[mid]: #if the search element is less than the middle element, 
        #the searched array will be cut in half, and only the first half searched (elements that are less than the middle element only)
        high = mid - 1
    elif SearchEle > MyArr[mid]: #search element is more than middle element
        #searched array cut in half, only the second half searched (elements more than the middle element)
        low = mid + 1

if Found == True:
    print("Found at", mid)
else:
    print("Not found")
