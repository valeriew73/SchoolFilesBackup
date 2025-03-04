'''
Recursive function = a function that calls itself in its definition.
- Iterative functions can be used instead but using recursion sometimes makes problems simpler to solve and make the code more efficient
- Sometimes iteration can't solve a problem whereas recursion can
- Sometimes the program runs slower because of the many push and pops to and from the call stack
'''

# def dream():
#     dream() 
# dream()
#FIXME: the program crashes and an error occurs because maximum recursion depth is exceeded

''' 
Everytime a function is called, it acts as an interrupt so the last instruction is pushed into a call stack to be executed after the interrupt is serviced.
The values of variables, state of the program, etc. is also saved in the call stack.
The call stack has a maximum capacity due to the RAM so when there's no base case (terminating case) or the base case is not met in a recursive function like in the above example, 
the function keeps calling itself and the stack becomes full.

Recursive function has to have a:
- Recursive case: the part that calls the function in the definition
- Base/Terminating case
'''

def factorial(num):
    if num == 0: #base case (condition where the function returns a known value)
        return 1
    else:
        return num * factorial(num - 1) 
# factorial complexity

# print(factorial(999))

def sum_of_array(my_array):
    if len(my_array) == 1:
        return my_array[0]
    else:
        return my_array[0] + sum_of_array(my_array[1:])    

print(sum_of_array([1, 2, 3, 4, 5]))


def reverse(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverse(string[:-1])  
    
print(reverse("Hello"))


def letter_count(string):
    if len(string) == 0:
        return 0
    else:
        if string[0] == letter:
            return 1 + letter_count(string[1:])
        else:
            return letter_count(string[1:])

letter = input("Please enter a letter to count: ")
print(letter_count("abacad"))


def fibonacci(num_of_ele):
    if num_of_ele == 1:
        return 0
    elif num_of_ele == 2:
        return 1
    else:
        return fibonacci(num_of_ele - 2) + fibonacci(num_of_ele - 1)

num_of_ele = int(input("Please enter the no. of elements in the fibonacci sequence: "))

fib_array = []
for i in range(1, num_of_ele + 1):
    fib_array.append(fibonacci(i))


# MyArr = [2, 3, 6, 8, 19, 23, 27, 58, 84, 92]
# Found = False

# low = 0
# high = len(MyArr)


# def recursive_binary_search(mid):
#     SearchEle = int(input("Please enter a value to search: "))
#     while (Found == False) and (high != low):
#         if SearchEle == MyArr[mid]:
#             Found = True
#         elif SearchEle < MyArr[mid]:
#             high = mid - 1
#         elif SearchEle > MyArr[mid]:
#             low = mid + 1
#         recursive_binary_search((low + high) // 2)

# if Found == True:
#     print("Found at", mid)
# else:
#     print("Not found")
