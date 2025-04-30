integer = 0
print(f"outside function: {integer}")
def modify(immutable_var):
    immutable_var += 2
    print(f"inside function: {immutable_var}")
modify(integer)
print(f"after function, outside function: {integer}")


array = []
print(f"outside function: {array}")
def modify(immutable_var):
    immutable_var += 2
    print(f"inside function: {immutable_var}")
modify(array)
print(f"after function, outside function: {array}")
