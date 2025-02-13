
# the upper bound in the range should be incremented by 1 from the intended value, range(1,11) loops 10 times instead of 11
# in range(10) loops 10 times because python is zero based
# third value in range tells many steps/increments to the counter
for counter in range(1, 11, 1):
    print(f"{counter}. Hello")