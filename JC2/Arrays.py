# for initialising/declaring arrays of integers in python, replace 0 with None or " " for string
myArr = [0] * 10
for i in range(len(myArr)):
    print(myArr[i])

# alternative
myNewArr = [0 for i in range(10)]
print(myNewArr)

# for initialising/assigning values to the array
for i in range(len(myArr)):
    myArr[i] = input(f"Please enter a value for index {i}: ")

print(myArr)

# alternative
for i in range(10):
    addEle = input(f"Please enter a value for index {i}: ")
    myNewArr.append(addEle)

print(myNewArr)