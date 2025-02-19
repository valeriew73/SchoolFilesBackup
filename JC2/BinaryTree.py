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

print(binary_tree)