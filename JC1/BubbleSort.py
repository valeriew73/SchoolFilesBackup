Array = [5, 2, 3, 4, 1]
lb = 0
ub = 5
Top = 0
Swap = True
while Swap == True and Top <= ub:
    Swap = False
    for Index in range(lb, ub - Top):
        if Array[Index] > Array[Index + 1]:
            Temp = Array[Index]
            Array[Index] = Array[Index + 1]
            Array[Index + 1] = Temp
            Swap = True
        else:
            Swap = False
        print(Array)
    Top = Top + 1
