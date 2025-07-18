# Problem 2: Needle and Haystack

# haystack = "sadbutsad"
# needle = "sad"
# output = index of the first occurrence or -1

# string
# edge cases: if its empty: -1, letters (NO)
# sliding window
# iterate through the entire string = haystack
# if haystack = needle
# return index

# def needle_and_haystack(haystack, needle):
    
#     if not haystack:
#         return -1
    
#     length_h, length_n = len(haystack), len(needle)
    


#### Breakout Room : Ver 1 #####
# Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise.
# A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ).
# Your solution must be recursive.


def is_nested(paren_s):
	# edge case: if no parentheses: return true, number or letters; retur false
    if paren_s == "":
        return True
    
    # () = true
    # ()) = false
    # )))((( = false
    # base case
    if paren_s[0] == '(' and paren_s[-1] == ')':
        return is_nested(paren_s[1:-1])  # if the first and last characters are not a valid pair, return False

# Example Input: "(())"
# Expected Output: True
output = is_nested("(())")
print(output)