myArr = [
[1,3,6,5], 
[4,8,2,1], 
[2,5,3,7]]

#Get the total of the rows
def rowtotal():
    rowtotal = 0
    for row in range(0, len(myArr)):
        for col in range(0, len(myArr[row])):
            rowtotal = rowtotal + myArr[row][col]
        print(f"row {row + 1} total: ", rowtotal)
        rowtotal = 0
    

#Total of the columns
def coltotal():
    coltotal = 0
    row = 0
    for col in range(0, len(myArr[row])):
        for row in range(0, len(myArr)):
            coltotal = coltotal + myArr[row][col]
        print(f"col {col + 1} total: ", coltotal)
        coltotal = 0


# Highest in each row

def rowhighest():
    rowhighest = 0
    for row in range(0, len(myArr)):
        for col in range(0, len(myArr[row])):
            if myArr[row][col] > rowhighest:
                rowhighest = myArr[row][col]
        print(f"row {row + 1} highest: ", rowhighest)
        rowhighest = 0


#Highest in each column
def colhighest():
    colhighest = 0
    row = 0
    for col in range(0, len(myArr[row])):
        for row in range(0, len(myArr)):
            if myArr[row][col] > colhighest:
                colhighest = myArr[row][col]
        print(f"col {col + 1} highest: ", colhighest)
        colhighest = 0
colhighest()