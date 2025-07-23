
# Problem Set Version 1
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(1)

root3 = TreeNode(5)
root3.left = TreeNode(2)


# Problem 2: 3-Node Sum 1

# def check_tree(root):
# 	return root.val == root.left.val + root.right.val

# Example Input Tree #1: 
#   10
#  /  \
# 4    6
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False


# Problem 3: 3-Node Sum II
def check_tree(root):
    if root is None:
        return False

    left = 0
    right = 0
    if root.left:
        left = root.left.val
    if root.right:
        right = root.right.val
          
    child_sum = left + right

    return root.val == child_sum


print(check_tree(root))
print(check_tree(root2))
print(check_tree(root3))

# Problem 4: Find Leftmost Node 

def left_most(root):
    # edge case
    if root is None:
        return None
    
    if root.left is None:
        return root.val
    
    return left_most(root.left)

   
# Problem 5: Find Leftmost Node Iteratively

def left_most_iterative(root):
    if root is None:
        return None
    
    current = root
    while current.left:
        current = current.left
    return current.val

# Problem 6: In-order Traversal

def inorder_traversal(root):
    if root is None:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


example_root = TreeNode(1)
example_root.right = TreeNode(2)
example_root.right.left = TreeNode(3)

print(inorder_traversal(example_root))

    



