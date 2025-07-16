# Recursion 
# Excused Absence

#### Problem Set Version 1 ########

# Problem 1: Hello Hello

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)

# create new function repeat_hello_iterative() without recursion
def repeat_hello_iterative():
	