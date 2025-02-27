def fibonacci(num_of_ele):
    if num_of_ele == 1:
        return 0
    elif num_of_ele == 2:
        return 1
    else:
        fibonacci_array = []
        fibonacci_array.append(fibonacci(num_of_ele) + fibonacci(num_of_ele - 1))
        return fibonacci_array

fibonacci(3)