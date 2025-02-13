import random

def randlist():
    prevnum = 0
    OutputNum = 0
    while OutputNum <= 25:
        num = int(random.randint(0, 500))
        if num > prevnum:
            print(num)
            OutputNum +=1
            prevnum = num
