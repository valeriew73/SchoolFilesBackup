
myArr = [5, 2, 1, 4, 3]
top = len(myArr)
swap = True

while (swap == True) or (top > 0):
    for index in range(0, top - 1):
        if myArr[index] > myArr[index + 1]:
            temp = myArr[index]
            myArr[index] = myArr[index + 1]
            myArr[index + 1] = temp
            swap = True
        else: swap = False
    top = top - 1

print(myArr)




