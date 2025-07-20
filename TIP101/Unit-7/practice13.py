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
4
# Problem 2: How Many 1s
# Given a sorted list of integers containing only 0s ad 1s, count the total number of 1’s in the array in O(log n) time.
def count_ones(lst):
     low, high = 0, len(lst)

     while low < high:
         mid = (low + high) // 2
         if lst[mid] == 0:
             low = mid + 1
         else:
             high = mid

     return len(lst) - low

 # Test
lst = [0, 0, 0, 1, 1, 1]
print(count_ones(lst))  # Output: 3

# Binary Search IV
# try a recursive approach of binary search

def binary_search(nums, target):
    def helper(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return helper(left, mid - 1)
        else: 
            return helper(mid + 1, right)
    return helper(0, len(nums) - 1)
     

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(nums, target))

nums2 = [2, 4, 6, 8, 10, 12, 14, 16]
target2 = 8
print(binary_search(nums2, target2))

# Problem 4: Count Rotations
# You are given a circularly sorted list of integers.
# A circularly sorted list of integers is a sorted list
# whose elements have then been rotated some number of times such that the last element of the array becomes the first element of the array.
# Write a function count_rotations() that returns the total number of times the array is rotated. Assume there are no duplicates in the array.

def count_rotations(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] <= nums[right]:
            return left  # Already sorted, minimal at left
        
        mid = (left + right) // 2
        next_index = (mid + 1) % len(nums)
        prev_index = (mid - 1 + len(nums)) % len(nums)

        if nums[mid] <= nums[prev_index] and nums[mid] <= nums[next_index]:
            return mid
        
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid + 1
    
    return 0 

        

# Example Usage
nums = [8, 9, 10, 2, 5, 6] 
rotations = count_rotations(nums)
print(f"Array is rotated {rotations} times.")

# Problem : Merge Sort 1

# helper function
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
      # Add any remaining elements from the left half to the result list
    while i < len(left):
      result.append(left[i])
      i += 1
  
  # Add any remaining elements from the right half to the result list
    while j < len(right):
      result.append(right[j])
      j += 1
  
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


# Example Usage
nums = [5, 3, 8, 4, 2, 7, 1, 6]
sorted_nums = merge_sort(nums)
print(f"Sorted number array using merge sort: {sorted_nums}")

# Problem 6: Circle Search

def search_circular_list(nums, target):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    
    if nums[left] >= nums[mid]:
        if target >= nums[left] and target < nums[mid]:
            # move right
            right = mid - 1
        else:
            left = mid + 1
    else:
        if target > nums[mid] and target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example Usage:
arr = [8, 9, 10, 2, 5, 6]
target = 10
print(search_circular_list(arr, target))