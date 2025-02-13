myArr = [
[1,3,6,5], 
[4,8,2,1], 
[2,5,3,7]]

searchval = int(input("Please enter a value to search: "))

def LinearSearch():
    found = False
    for row in range(0, len(myArr)):
        for col in range(0, len(myArr[row])):
            if searchval == myArr[row][col]:
                found = True
                print(f"{searchval} has been found at row {row}, column {col}.")
    if not found:
        print("Not found.")


def LinearSearchRow():
    found = False
    row = int(input("Please enter the row to search: "))
    for col in range(0, len(myArr[row])):
        if searchval == myArr[row][col]: 
            found = True
            print(f"{searchval} has been found at column {col}.")
    if not found:
        print("Not found.")




for row in range(0, len(myArr)):
    top = len(myArr[row])
    swap = True
    while (swap == True) or (top > 0):
        for index in range(0, top - 1):
            if myArr[row][index] > myArr[row][index + 1]:
                temp = myArr[row][index]
                myArr[row][index] = myArr[row][index + 1]
                myArr[row][index + 1] = temp
                swap = True
            else: swap = False
        top = top - 1
print(myArr)

#     searchval = input("Please enter a value to search: ")
#     row2 = input("Please enter a row to search: ")
#     low = 1
#     high = len(myArr[row2])
#     while (Found == False) and (high != low):
#         mid = (low + high) // 2
#         if searchval == myArr[row2][mid]:
#             Found = True
#         elif searchval < myArr[row2][mid]:
#             high = mid - 1
#         elif searchval > myArr[row2][mid]:
#             low <- mid + 1
#         if Found == True:
#             print("Found at", mid)
#     else:
#         print("Not found")
