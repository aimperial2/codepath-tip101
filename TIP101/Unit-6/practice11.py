# Session 2
# Problem 1: Detect Circular Linked List

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# return a boolean; true or false
# circular linked list - tail node is an idicator of the head node appearing
# edge cases: empty linked list, if we have doubles (num1 -> num1), 
# current = head, traverse through the linked list, use a while loop

# A - B - C - *A* 
def is_circular(head):
    if head is None:
        return None
    current = head.next

    while current:
        if current == head:
            return True
        current = current.next
    return False



# Example Usage
# num1 -> num2 -> num3 -> num1
# True
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
print(is_circular(num1))

# var1 -> var2 -> var3
var1 = Node(1)
var2 = Node(1)
var3 = Node(3)
var4 = Node(1)
var1.next = var2
var2.next = var3
var3.next = var4
var4.next = var1
print(is_circular(var1))

# Output:
# True
# False

# Problem 2: Find Last Node in a Linked List Cycle
# Given the head of a singly linked list, write a function that returns the last node in the cycle.
# If there is no cycle in the linked list, return None.

def find_last_node_in_cycle(head):
    if head is None:
        return None
    
    slow = fast = head

# Example Input:
# num1 -> num2 -> num3 -> num4 -> num2

# Example Output: num4
