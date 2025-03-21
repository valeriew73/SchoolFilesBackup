my_array = [2, 3, 6, 8, 19, 23, 27, 58, 84, 92]

search_ele = int(input("Please enter a value to search: "))

def binary_search(low, high):
    global my_array, search_ele
    if search_ele not in my_array:
        print("Not found.")
    else:
        mid = (low + high) // 2 
        if search_ele == my_array[mid]:
            return mid
        elif search_ele < my_array[mid]:
            return binary_search(low, mid-1)
        elif search_ele > my_array[mid]:
            return binary_search(mid+1, high)

print(binary_search(0, len(my_array)-1))
