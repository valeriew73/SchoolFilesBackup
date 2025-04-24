my_array = [2, 3, 6, 8, 19, 23, 27, 58, 84, 92]

search_ele = int(input("Please enter a value to search: "))

def RecursiveBinarySearch(low, high):
    global my_array, search_ele
    found = False
    if search_ele not in my_array:
        print(f"{search_ele} was not found.")
        return 
    else: 
        while low != high or not found:
            mid = (low + high) // 2
            if search_ele < my_array[mid]:
                return RecursiveBinarySearch(low, mid-1)
            elif search_ele > my_array[mid]:
                return RecursiveBinarySearch(mid+1, high)
            elif search_ele == my_array[mid]:
                found = True
                return mid
            
print(f"{search_ele} was found at index {RecursiveBinarySearch(0, len(my_array)-1)}.")