# A procedure Count() will: 
# 1. input a value (all values will be positive integers) 
# 2. count the number of odd values and count the number of even values 
# 3. repeat from step 1 until the value input is 99 
# 4. output the two count values, with a suitable message. The value 99 must not be counted. 

def Count():
    listOfValues = [] #listOfValues is a list of integers
    value = 0 #value is a variable of data type integer
    evenValues = 0 #count of even values (data type integer)
    oddValues = 0 #count of odd values (data type integer)
    while value != 99:
        #input a value:
        value = int(input("Enter a positive value (or 99 to stop): ")) 
        #values must be positive integers:
        if value <= 0: 
            print("Value must be a positive integer.")
        #denotes the end of inputs:
        elif value == 99:
            print("End of inputs.")
        #valid values are appended into listOfValues
        elif value > 0 and value != 99:
            listOfValues.append(value)
            #the value is counted as either an even value or an odd value
            if (value % 2) == 0:
                evenValues = evenValues + 1
            else:
                oddValues = oddValues + 1
    print(f"All values entered: {listOfValues}")
    print(f"Number of odd values: {oddValues}")
    print(f"Number of even values: {evenValues}")

Count()

        