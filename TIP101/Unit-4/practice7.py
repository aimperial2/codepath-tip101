# Problem Set Ver 1
# Problem 1: Prime Number
# takes in positive integer n, returns a boolean true or false
# the condition is that n must be a prime number
# a prime number is a number that is only divisible by 1 and itself
# for example, 2, 3, 5, 7, 11,
# may need to use a while loop 
def is_prime(n):
  # check if n is a positive integer
  while n > 1:
          # check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
      if n % i == 0:
        return False  # n is divisible by i, so it's not prime
    return True  # if no divisors found, n is prime  
    

# example usage
print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# Problem 2: Two-Pointer Reverse List


# def find_middle(lst):
#   slow = fast = 0
    
#    while fast < len(lst) and fast + 1 < len(lst):
#         slow += 1
#         fast += 2
#     return slow  # slow will be at the middle index when fast reaches the end

# # example list
# lst = [1, 2, 3, 4, 5, 6]
# print(find_middle(lst))  # Output: 3 (middle element in the list)

# def reverse_list(lst):
#   start, end = 0, len(lst) - 1

#   while start < end:
#     hold = lst[start]
#     lst[start] = lst[end]
#     start -= 1
#     end += 1

#     return lst

# lst = [1, 2, 3, 4, 5]
# print(reverse_list(lst))

# def max_sublist_sum(lst, k):
#     max_sum = float('-inf')
#     current_sum = 0

#     for i in range(len(lst)):
#         current_sum += lst[i]
#         max_sum = max(max_sum, current_sum)
#         if i >= k - 1:
#             current_sum -= nums[i - (k - 1)]
#             max_sum = max(max_sum, current_sum)
    
#     return max_sum

# # Example usage
# nums = [1, 2, 3, 4, 5]
# k = 3
# print(max_sublist_sum(nums, k))  # Output: 12 (sublist 

def find_middle(lst):
  slow = fast = 0 
  while fast < len(lst) and fast + 1 < len(lst):
    slow += 1
    fast += 2
  return slow

#example list
lst = [1,2,3,4,5,6]
print(find_middle(lst))