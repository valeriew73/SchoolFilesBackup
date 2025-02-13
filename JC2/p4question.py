# q2
arrayData = [0] * 10
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(num):
    found = False
    i = 0
    while i <= len(arrayData) and not found:
        if num == arrayData[i]:
            found = True
        else: i += 1
    return found

num = int(input("Please enter an integer to search: "))
print("Found: ", linearSearch(num))

