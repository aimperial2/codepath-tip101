# Recursion 
# Excused Absence


# Iterative vs Recursion:
# Both achieves the same goal with different approaches
# iteration uses bottom up approach; uses a loop to repeat code
# recursion uses top down approach; calls the function itself for code to repeat

# Building Recursion Function:
# 1. Base Case - end condition
# 2. Recursive case - code to execute in all other cases

def count_recursive(num):
    # Action to repeat
    print(f"Count {num}!")

    # Base Case: If num is 1 we want to stop counting down
    if num == 1:
        # Terminate the function by returning
        return

    # Recursive Case: If num is larger than 1
    else:
       # Call count_recursive() again, but decrement the input value by 1
       count_recursive(num - 1)

# Recursive Driver and Helper Functions:
def partition_evens_odds(lst):
  return recurse_partition(lst, [], [])

def recurse_partition(lst, evens, odds):
  if not lst:
      return evens, odds
  if lst[0] % 2 == 0:
      evens.append(lst[0])
  else:
      odds.append(lst[0])
  return recurse_partition(lst[1:], evens, odds)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens, odds = partition_evens_odds(lst)
print(evens) # Prints: [2, 4, 6, 8]
print(odds)  # Prints: [1, 3, 5, 7, 9]


#### Problem Set Version 1 ########

# Problem 1: Hello Hello

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)
print("end of 1st method (recursive)")
# create new function repeat_hello_iterative() without recursion
def repeat_hello_iterative(n):
	while n != 0:
          print("Hello")
          n -= 1

repeat_hello_iterative(5)
print("end of 2nd method (iterative).")
