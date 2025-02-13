

def LinearSearch(searchval):
    array = [1, 2, 5, 4, 3]
    found = False
    index = 0
    while not found and index <= len(array):
        if searchval == array[index]:
            found = True
        else: index = index + 1
    
    if found == True:
        print(f"{searchval} was found at index {index}.")
    else: print("Not found.")

searchval = input("Please enter a value to search: ")
LinearSearch(searchval)

