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
for row in range(10):
    for column in range(5):
        print(Arr[row][column], end=" ")
    print(" ")
    