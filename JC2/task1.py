
myArr = [1, 5, 3, 2, 4]

#Get the total of the array
def total():
    total = 0
    for index in range(0, len(myArr)):
        total = total + myArr[index]
    print("total: ", total)

#Get the smallest value in the array
def smallest():
    smallest = myArr[0]
    for i in range(0, len(myArr)):
        if myArr[i] < smallest:
            smallest = myArr[i]
    print("smallest: ", smallest)

#Get the largest value in the array
def largest():
    largest = myArr[0]
    for i in range(0, len(myArr)):
        if myArr[i] > largest:
            largest = myArr[i]
    print("largest: ", largest)



