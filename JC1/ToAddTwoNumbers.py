
# Num1 = 5 #Num1 is a variable of data type int
# Num2 = 6 #Num2 is a variable of data type int

# sum = Num1 + Num2
# print("First number:", Num1)
# print("Second number:", Num2)
# print("Sum:", sum)


#for functions, use parentheses '( )'
#'[]' is called a bracket
#'{}' is called a brace

# to run a program, shortcut: "Ctrl + F5"
# settings shortcut: "Ctrl + ,"
# how to mass turn into comment "Select, Ctrl + /"

Num1 = int(input("Enter the first number: ")) #Num1 is a variable of data type int
Num2 = int(input("Enter the second number: ")) #Num2 is a variable of data type int

Sum = Num1 + Num2
Difference = Num1 - Num2
Product = Num1 * Num2
Quotient = Num1 / Num2
IntegerQuotient = Num1 // Num2
Remainder = Num1 % Num2

print("Sum of the two numbers:", Sum)
print(f"The sum of {Num1} and {Num2} is {Sum}") #format function (put an 'f' before the apostrophes and brace the variables)
print(f"The product of {Num1} and {Num2} is {Product}")
print(f"The quotient of {Num1} and {Num2} is {Quotient}")
print(f"The integer Quotient of {Num1} and {Num2} is {IntegerQuotient}")
print(f"The remainder of the division of {Num1} and {Num2} is {Remainder}")

