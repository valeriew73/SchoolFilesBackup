'''
Insertion sort works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. 
It is like sorting playing cards in your hands. 
You split the cards into two groups: the sorted cards and the unsorted cards. 
Then, you pick a card from the unsorted group and put it in the right place in the sorted group. 
'''
#Use HackerEarth's visualiser!

Arr = [9, 5, 4, 2, 7, 8]

print(Arr)

for index in range(1, len(Arr)): #the index of key always starts with 1 because you're comparing it with the element before it 
    key = Arr[index] #key is the element to be moved to its sorted position in the sorted array
    j = index - 1 #index of element before key
    while j >= 0 and key < Arr[j]:
        temp = Arr[j] #swap algorithm
        Arr[j] = Arr[j + 1] #j+1 is used for key's index because j is changed after each swap
        Arr[j + 1] = temp
        j = j - 1 #since key is swapped, j will be decremented by 1 too (to point to the current element before key)

print(Arr)