# 1. Create a dictionary
student = {"name": "Joe", "age": 21, "grades": [89.3, 90.2, 75.5], 
"address": {"city": "San Francisco", "state": "CA"}}

# 2. Access a key:value pair
print(student["name"]) #Joe
print(student["age"]) #21
print(student["grades"][0]) #89.3
print(student["address"]["state"]) #"CA"

# 3. Add a key:value pair (keys are always unique)
student["is_graduated"] = True
print(student["is_graduated"])

student["address"]["zip"] = "94014"
print(student["address"]["zip"])

# 4. Update a key:value pair
student["is_graduated"] = False
print(student["is_graduated"])

# 5. Delete a key:value pair
student.pop("is_graduated") # Removes the key "is_graduated" from student
# print(student["is_graduated"]) -> returns Error: key doesn't exist

# 6. Get all keys and values
print(student)
for key in student:
    value = student[key]
    print(f"{key} -> {value}")

# 7. Searching for a key
searchkey = input("Please enter a key to search: ")
if searchkey not in student:
    print(f"{key} is not found.")
else:
    print(f"Value found: {student[searchkey]}")

# 8. Copying a dictionary
dict_copy = student.copy()
print(dict_copy)

