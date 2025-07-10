# def above_threshold(lst, threshold):
#     # initialize empty list
#     # loop through list (each element)
#     # check if num > threshold
#     # if true, add to new list
#     # return NEW list

#     result = []
    
#     for num in lst:
#         if num > threshold:
#             result.append(num)

#     return result


# list = []

# threshold = 3

# print(above_threshold(list, threshold))

# def is_subsequence(lst, sequence):

#     i = 0

#     # if len(s) > Len(l):
# 	# return false

#     for num in lst:
#         if num  == sequence[i]:
#             i += 1
    
#     if i == len(sequence):
#         return True
#     else: 
#         return False
    
# lst = []
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))

# Problem 4 = Keys vs Values
# takes dictionary as a parameter
# outputs whether keys and values has a greater sum
# i have to calculate a dictionary's sum of values and keys
# next, i would have to evaluate both and print one or the other
# special cases: if the dictionary is empty, if both keys & values have the same integer amount

# value_sum = 0 and key_sum = 0 

# def keys_v_values(dictionary):
#     value_sum = 0
#     key_sum = 0

#     #own comment: .items() allows us to loop through both keys and values in the dictionary
#     for key,value in dictionary.items():
#         key_sum += key
#         value_sum += value
    
#     if value_sum >= key_sum:
#         return("values")
#     else:
#         return("keys")

    
# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)


# Problem 5 = Restock Inventory

    # for k, v in 
