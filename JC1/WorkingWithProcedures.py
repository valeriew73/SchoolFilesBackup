def printMyName():
    print("My name is Valerie")


printMyName()

# Good practice to enter twice (one space) after the end of the procedure definition

def sayHello(name):
    print(f"Hello, {name}")


sayHello("Valerie")

def addTwoNumbers(num1, num2):
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)


addTwoNumbers(5, 6)


# global variables are defined in the program (the variables are accessible in every function or procedure even if they are not passed into the function)
# turn the local variables into global variables by adding "global" infront of each variable inside the procedure/function (bad practice)
def addTwoNumbers():
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
addTwoNumbers()

# local variables are defined in the procedure or function, and are not accessible by the main program
def addTwoNumbers(num1, num2):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)

addTwoNumbers(num1, num2)

#number1 and number2 are both arguments, and num1 and num2 are parameters which take the value of the arguments
def addTwoNumbers(num1, num2):
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
addTwoNumbers(number1, number2)