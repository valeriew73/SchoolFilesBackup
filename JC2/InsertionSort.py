Arr = [9, 5, 4, 2, 7, 8]

print(Arr)

for i in range(1, len(Arr)):
    key = Arr[i]
    j = i - 1
    while j >= 0 and key < Arr[j]:
        temp = Arr[j]
        Arr[j] = Arr[j + 1]
        Arr[j + 1] = temp
        j = j - 1

print(Arr)