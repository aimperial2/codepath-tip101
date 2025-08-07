# Unit 10 : Session 1

# UMPIRE

#Problem 1: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# dictionary: "(" - value ")" - key
# set = {}
# possibly use a stack (?) last in first out, return true/false
# recursion ? 
# stack: append() and pop() methods 
# alway in correct order
# base cases, edge cases : empty = false, 
def is_valid(s):
   # base case: it is empty, must be true
    if s == "":
        return True
    
    # set up the stack and valid bracket set to work with
    stack = []
    check_set = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in check_set:
            if len(stack) == 0:
                return False
            else:
                top_element = stack.pop()
                exp_opening = check_set[char]
                if top_element != exp_opening:
                    return False
        else:
            stack.append(char)

    # returns True if empty, False if not
    return len(stack) == 0 


# Example #1:
# Expected Output: True
str = "()"
print(is_valid(str))

# Example #2:
# s = "()[]{}"
# Expected Output: True
str2= "()[]{}"
print(is_valid(str2))

s = "(]"
print(is_valid(s))
# Expected Output: False


#Problem 2; Best Time to Buy & Sell Stock
# You are given a list of integers 'prices' where 'prices[i]' is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# UMPIRE:
# takes list - pieces
# pieces[i] = prices of stocks on ith day
# BUY LOW, SELL HIGH !!! - really helpful insight
# we want maximum profit

def max_profit(prices):
	pass


# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.