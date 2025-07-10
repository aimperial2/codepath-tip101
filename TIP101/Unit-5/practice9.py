# Problem 1: Battle Pokemon
# Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.
# If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.
# Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".
# class Pokemon():
# 	def  __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp # hit points
# 		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
# 	def attack(self, opponent):
# 		opponent.hp -= self.damage
# 		if opponent.hp <= 0:
# 			opponent.hp = 0
# 			print(f"{opponent.name} fainted!")
# 		else:
# 			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

# #Example Usage
# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)

# Problem 2: Convert to Linked List

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
    # def connect_two_nodes(self, node_1, node_2):
    #     pass

node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)


# Example Usages
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

# Jigglypuff -> Wigglytuff
# Wigglytuff -> None

# Problem 3: Add First
# Write a function add_first() that takes in a head of a linked list 
# and a new_node from the Node class as parameters.
# It should insert new_node as the new head of the linked_list.
# The function returns new_node.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	# pass
	new_node.next = head
	return new_node
	


# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

# Jigglypuff -> Wigglytuff 
# Ditto -> Jigglypuff

# Problem 4: Get Tail
# If the list is empty (head is None), return None.

def get_tail(head):
	
	if head is None:
		return None
	current = head
	while current.next is not None:
		current = current.next
	return current.value
	


# linked list: num1->num2->num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1",num2)

head = num1
tail = get_tail(num1)
print(tail)

# num3
 

#Problem 5: Replace Node
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	# Edge Case
	current = head
	
	while current is not None:
		if current.value == original:
			current.value = replacement
		current = current.next

			
		
#Example Usage
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"