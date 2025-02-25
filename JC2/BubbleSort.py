'''
Bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order.
It uses multiple passes. After the first pass, the maximum element will go to the end.
After the second pass, the second largest element goes to the second last position.
After each pass, we only process the elements that have not been moved to the correct position so the top element to be sorted -= 1.
A boolean variable, "swap", is also used to terminate the program early in case the array is already sorted.
'''
#Use HackerEarth's visualiser!

myArr = [5, 2, 1, 4, 3]
top = len(myArr) #top is the index of the last element
swap = True #assume that swap is True at the start so the program will run + because the array is assumed to start off unsorted

while (swap == True) and (top > 0): #swap var allows the program to terminate early if in a pass there are no swaps (meaning the list is sorted)
    for index in range(0, top - 1):
        if myArr[index] > myArr[index + 1]: #swap algorithm
            temp = myArr[index]
            myArr[index] = myArr[index + 1]
            myArr[index + 1] = temp
            swap = True
        else: swap = False #if swap remains False at the end, there aren't any swaps in that pass
    top = top - 1 #after each pass, the top element is where it's supposed to be so it isn't going to be included in the sorting algorithm anymore
    #end of pass

print(myArr)
