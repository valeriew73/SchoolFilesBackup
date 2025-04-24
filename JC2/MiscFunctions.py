#Split:

# The split function splits a string by the given parameter. It returns an array.
name = "Valerie Wilson"
print(name.split()) # if a parameter is not provided, then the string will be split by whitespace (" ")

comma_name = "Valerie,Wilson"
print(comma_name.split(","))

# The strip function removes leading and trailing character parameters 
# (unordered and can be combined, each character added to the string is treated as one item)
# from the string
fruit = "    banana   "
print(fruit.strip()) # if a parameter is not provided, trailing whitespaces or \n will be removed

# you can also straight up pass the string directly without assigning it first to a variable
print("grtrr..rt.tgg.....rgttt.apple.tgrtrt.tt..t.".strip("grt."))