# Problem 1: Nested Constructors
# Step 1: Copy the following code into Replit.

# Step 2: Add a line of code (outside of the class)
# to create the linked list 4 -> 3 -> 2 in a single assignment statement.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
# head = Node(4, Node(3, Node(2)))

# Problem 2: Find Frequency
# Given the head of a linked list and a value val, return the frequency of val in the list.
# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
# for why you believe your solution has the stated time and space complexity.

def count_element(head, val):
	# create a list
	frequency = 0
	curr = head
	while curr:
		if curr.value == val:
			frequency += 1
		curr = curr.next
	return frequency
			
			

# Example Usage
# Input List: 3 -> 1 -> 2 -> 1
head = Node(3, Node(1, Node(2, Node(1))))
# Input: head = 3, val = 1
print(count_element(head, 1))
# Output: 2


# PROBLEM SET VERSION 2
# Problem  1: One to many
# The assignment statement to the head variable below creates the linked list Mario -> Luigi -> Wario. 
# Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node("Mario", Node("Luigi", Node("Wario")))

node1 = Node("Mario")
node2 = Node("Luigi")
node3 = Node("Wario")
node1.next = node2
node2.next = node3


# Problem  1: Remove First Value 
# Given the head of a linked list where each node is an integer value,
# return the maximum value in the linked list.

def find_max(head):
	if head is None:
		return None
	max_val = head.value
	current = head
	while current:
		if current.value > max_val:
			max_val = current.value
		current = current.next

	return max_val
		
	
# Example Usage
# Linked List: 5 -> 6 -> 7 -> 8 
head = Node(5, Node(6, Node(7, Node(8))))

print(find_max(head))
# Input: head = 5