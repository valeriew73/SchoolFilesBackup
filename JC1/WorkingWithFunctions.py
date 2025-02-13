def addTwoNumbers():
    num1 = 6
    num2 = 9
    sum = num1 + num2
    return sum

TempSum = addTwoNumbers()
print("The sum is", TempSum)


def addTwoNumbers(num1, num2):
    sum <- num1 + num2
    return sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
TempSum = addTwoNumbers(num1, num2)
print("The sum is", TempSum)