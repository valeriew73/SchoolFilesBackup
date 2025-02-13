
count = 1
while (count <= 10):
    print(f"{count}. Hello")
    count += 1

sum = 0 
for count in range(10):
    num = int(input("Please enter a number: "))
    sum = sum + num
print("Sum is ", sum)

sum = 0
count = 1
while count <= 10:
    num = int(input("Please enter a number: "))
    sum = sum + num
    count += 1
print("Sum is ", sum)

#Find the sum of all of the inputted numbers until a rogue value of -999 is input
num = 0
sum = 0
while num != -999:
    num = int(input("Please enter a number: "))
    sum = sum + num
print("Sum is ", sum)

#Find the sum of all of the positive inputted numbers until a rogue value of -999 is input
num = 0
sum = 0
while num != -999:
    num = int(input("Please enter a number: "))
    if num > 0:
       sum = sum + num
print("Sum is ", sum)