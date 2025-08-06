from collections import deque 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# # current = head
# # while loop to traverse
# # swap the elements from its initial 
# # current, previous, next - pointers
# # assuming that the linked list isnt empty
# # edge cases: linked list could be empty, theres only one element in the list

# def reversed_singly_list(head):
#     previous = None
#     current = head
    

#     # traverse the linked list
#     while current:
#         # store the next node
#         temp_next = current.next

#         # store the next value to the previous node
#         current.next = previous

#         # go to the next node, which is now set to previous
#         previous = current

#         # swap the pointers 
#         current = temp_next 
    
#     # return the head of the new linked list
#     return previous.val

# head = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9, None)))))
# print(reversed_singly_list(head))


# # Input: 1 → 3 → 5 → 7 → 9 # head = [1, 3, 5, 7, 9]
# # Output: 9 → 7 → 5 → 3 → 1 # [9, 7, 5, 3, 1]



# Problem 1: Level Order Traversal of Binary Tree
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
# understand:
# root of a binary tree
# return the list of the level order (list)
# do the edge cases first
# traverse through the binary tree and know the level order of the tree

def level_order(root):
    # If the tree is empty:
    if not root:
        return []
    # return an empty list

    # Create an empty queue using deque
    queue = deque()
    # Create an empty list to store the explored nodes
    stored_nodes = []

    # Add the root to the queue (root.val != ROOT)
    queue.append(root)

    # While the queue is not empty:
    while queue is not None:
        # Pop the next node off the queue (pop from the left side!)
        # Add the popped node to the list of explored nodes
        popped_val = queue.popleft()
        stored_nodes.append(popped_val)
         # Add each of the popped node's children to the end of the queue
        if popped_val.left:
            queue.appendleft(popped_val.left)
        else:
            queue.append(popped_val.right)

    # Return the list of visited nodes
    return stored_nodes


# Example Usage:

# Example Input Tree:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: [4, 2, 6, 1, 3]
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3