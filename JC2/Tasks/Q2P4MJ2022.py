import random

#2 a)
# declaration
twoDArray = []
for i in range(10):
    twoDArray.append([0 for i in range(10)])

# initialisation
for  row in range(10):
    for col in range(10):
        twoDArray[row][col] = random.randint(0, 100)

