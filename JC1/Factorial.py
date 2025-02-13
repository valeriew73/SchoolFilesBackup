def fact(num):
    Factorial = 1
    for Count in range(1, num + 1): #the second parameter in "range()" always returns one value less
        Factorial = Factorial * Count
    return Factorial

num = int(input("Enter a number: "))
TempFactorial = fact(num)
print(f"The factorial is {TempFactorial}")