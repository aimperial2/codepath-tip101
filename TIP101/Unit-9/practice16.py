# Problem Set Version 1

# Problem 1: Is Symmetric Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# starting plan
# return boolean
# have a helper function
def is_symmetric(root):
	# base case: empty
    if not root:
        return True
    
    def helper(node1, node2):
        # left has to match right, vice versa
        # if both do mirror each other 
        if not node1 and not node2:
            return True
        
        # if either don't mirror each other 
        if not node1 or not node2:
            return False
        
        # traversal?
        # if values 
        return (helper(node1.left, node2.right) and helper(node1.right, node2.left))
    
    return helper(root.left, root.right)
        

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

print(is_symmetric(root1))
# Example Tree #1:

#        1
#      /   \
#     /     \
#    2       2
#   / \     / \
#  3   4   4   3
#            |
# Input: root = 1
# Expected Output: True

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(is_symmetric(root2))
# Example Tree #2:

#         1
#       /   \
#      /     \
#     2       2
#      \       \
#       3       3
# Input: root = 1
# Expected Output: False


# Problem 2: Root-to-Leaf Paths
# Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

# A leaf is a node with no children.

# list with strings

def binary_tree_paths(root):
	# base case
    if not root:
        return []
    
    result = []
    
    # helper function
    def helper(node, path):
        if not node:
            return
        
        #path -> result; if we find leaf
        if path == "":
            current_path = str(node.val)
        else:
            current_path = path + "->" + str(node.val)
        
        if not node.left and not node.right:
            result.append(current_path)
        else:
            helper(node.left, current_path)
            helper(node.right, current_path)
        
    helper(root, "")
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

result1 = binary_tree_paths(root)
print(result1)
# Example Input Tree #1:

#   1
#  / \
# 2   3
#  \  
#   5         

# Example Input: root = 1
# Expected Output: ["1->2->5", "1->3"]
# ["1->3", "1->2->5"] is also valid

# Example Input Tree #2:

#   1    

# Example Input: root = 1
# Expected Output: ["1"]

# Problem 3: Minimum Difference in BST
# Given the root of a binary search tree, 
# return the minimum difference between the values of any two different nodes in the tree.

def min_diff_in_bst(root):
    pass

# HINT
# We can represent positive and negative infinity with the following syntax.
# positive_infinity = float('inf')

# negative_infinity = float('-inf')

# Example Input Tree #1:

#     4
#    / \
#   2   6
#  / \  
# 1   3

# Example Input: root = 4
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)