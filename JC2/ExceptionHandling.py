
# Exception = an extreme condition that makes you program crash 
# can lead to loss of data in files

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# print("Quotient:", num1/num2)  # FIXME: Exception: zero error - when num2 is 0, an error occurs

try:
    print("Quotient:", num1/num2)
except ZeroDivisionError:
    print("Hey, you can't divide by zero. ")
