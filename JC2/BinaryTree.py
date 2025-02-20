'''
root_pointer always points to the root node so it is a constant (root is added only once)
free_pointer points to the next available location in the heap (because binary trees are dynamic data structures)
You can implement a binary tree as an array of nodes

'''

'''
class Node():
    def __init__(self, left_child_pointer, data, right_child_pointer):
        self.left_child_pointer = left_child_pointer
        self.data = data
        self.right_child_pointer = right_child_pointer

root_pointer = 0 
free_pointer = 0

binary_tree = [Node()]
'''


binary_tree = [[None for i in range(3)] for i in range(10)]

for row in range(10):
    for col in range(3):
        if col == 1:
            binary_tree[row][col] = row + 1
        else: binary_tree[row][col] = -1

# left_child_pointer is column 0, data is at column 1 and right_child_pointer is at column 2


binary_tree = [[1, 9, 2], 
               [3, 7, -1], 
               [4, 13, 5], 
               [-1, 5, -1],
               [-1, 12, -1],
               [-1, 7, -1],
               [-1, 8, -1], 
               [-1, 9, -1], 
               [-1, -1, -1]]

free_pointer = 6
root_pointer = 0

def searchval(val_to_search):
    node_index = root_pointer
    while node_index != -1 and val_to_search != binary_tree[node_index][1]:
        if val_to_search < binary_tree[node_index][1]:
            node_index = binary_tree[node_index][0] # left child
        else:
            node_index = binary_tree[node_index][2] # right child

    return node_index 

val_to_search = int(input("Please enter a value to search: "))
print(searchval(val_to_search))

def insert_to_tree(element):
    # Check if there's enough space in the tree (if free pointer = -1: tree is full)
    if free_pointer == -1:
        print("The binary tree is full, cannot insert an element.")
    elif free_pointer == 0: # no root
        root_pointer = 0
        free_pointer = binary_tree[0][1]
        binary_tree[0][1] = element
        binary_tree[0][0] = 1
        binary_tree[0][2] = 2
    else:
        new_item_pointer = free_pointer
        free_pointer = binary_tree[new_item_pointer][1]
        binary_tree[new_item_pointer][1] = element
        

