Arr = [[0 for i in range(5)],
       [1 for i in range(5)],
       [2 for i in range(5)],
       [3 for i in range(5)],
       [4 for i in range(5)],
       [5 for i in range(5)],
       [6 for i in range(5)],
       [7 for i in range(5)],
       [8 for i in range(5)],
       [9 for i in range(5)]]
    
# When you're printing/displaying a 2D array, you have to print it as a matrix like this
for row in range(10):
    for column in range(5):
        print(Arr[row][column], end=" ") #if you don't specify the end, usually it will put a \n at the end of each print statement
    print()

for row_arr in Arr: #accessing the items directly without using the indexes
    for col_item in row_arr:
        print(col_item, end = " ")
    print()