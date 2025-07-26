# Unit 8 Session 2 
# Remember: UMPIRE: Understand, Match, Plan, Implement, Review, Evaluate.

###### Version 1 ##########

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right


# Problem 1: Is Uni-valued
# A binary tree is uni-valued if every node in the tree has the same value. 
# Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.
# Evaluate the time complexity of your solution.
        
# know that the goal to traverse through the tree to see it is uni-valued
# must be a boolean value (T or F)
# if empty, return None
# possibility of using pointer current, maybe store and make sure that
# recursive approach: does not need current pointer
def is_univalued(root):
    # 1. base case: empty tree (considered true)
    if root is None:
        return True
    
    # Check that the left children exist and has the same value as root
    if root.left is not None and root.val != root.left.val:
        return False
    
    # check that the right children exist and has the same value as root
    if root.right is not None and root.val != root.right.val:
        return False
    
    return is_univalued(root.left) and is_univalued(root.right)


# Example Input Tree #1

#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: True

# Example Input Tree #2

#       1
#      / \
#     /   \
#    1     2
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: False

#Commented out 
# root1 = TreeNode(1)
# root1.left = TreeNode(1)
# root1.right = TreeNode(1)
# root1.left.left = TreeNode(1)
# root1.left.right = TreeNode(1)
# root1.right.right = TreeNode(1)

# Test it
# print(is_univalued(root1))  # Should print True

# root2 = TreeNode(1)
# root2.left = TreeNode(1)
# root2.right = TreeNode(2)  # This is the problem node!
# root2.left.left = TreeNode(1)
# root2.left.right = TreeNode(1)
# root2.right.right = TreeNode(1)

# Test it
# print(is_univalued(root2))  # Should print False


# Problem 2: Binary Tree Height
# Given the root of a binary tree, write a function height() that returns the height of a binary tree.
# UMPIRE

# edge/base case: empty tree, root only
# traverse through both left and right, return whichever side is the longest
# try recursive rather than iterative
def height(root):
    #1. base case: empty should return 0
    if root is None:
        return 0
    
    # left length and right length variable
    #2. Possibly traverse through left side?
    left = height(root.left)

     #3. traverse through right side
    right = height(root.right)

    # return either side's length 
    if left > right:
        return left + 1
    else:
        return right + 1



# Example Input Tree #1

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# root3 = TreeNode(4)
# root3.left = TreeNode(2)
# root3.right = TreeNode(5)  # This is the problem node!
# root3.left.left = TreeNode(1)
# root3.left.right = TreeNode(3)

# print(height(root3))
# Input: root = 4
# Expected Output: 3

# Example Input Tree #2 

#       4 

# Input: root = 4
# Expected Output: 1

# root4 = TreeNode(4)
# print(height(root4))


class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
       
# Problem 3: BST Insert
def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)
    
    if key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    else:
        root.val = value

    return root
    


# Problem 4: BST Remove 
def remove_bst(root, key):
    # base case if empty tree
    if root is None:
        return None

    # Locate the node to be removed
    # Traverse through the tree
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        # If the node is a leaf node:
		# Remove the node by redirecting the appropriate child reference of its parent to None
        if root.left is None and root.right is None:
            return None
	    # If the node has one parent:
		# Replace the node with its child, updating its parent's nodes child reference appropriately
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            
            root.key = successor.key
            root.val = successor.val

            root.right = remove_bst(root.right, successor.key)
	# If the node has two children:
		# Find the node's inorder successor (smallest node in right subtree)
		# Swap the value of the node and its inorder successor
		# Recursively remove the successor (which now has the current node's value)
	# Return the root of the updated tree
    return root

# Example Input Tree #1: (tree depicted using keys) 

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
root5 = TreeNode(10, "hello")
root5.left = TreeNode(5, "hi")
root5.right = TreeNode(15, "privyet")
root5.left.left = TreeNode(1, "annyeong")
root5.left.right = TreeNode(8, "konnichiwa")
root5.right.left = TreeNode(13, "hola")
root5.right.right = TreeNode(16, "kumusta")

print(remove_bst(root5, 10))