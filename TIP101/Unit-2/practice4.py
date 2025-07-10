# # Anagram Question - Instructor's Lesson
# def group_anagrams(words):
#     anagrams = {}
#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word not in anagrams:
#             anagrams[sorted_word] = []
#         anagrams[sorted_word].append(word)
#     return list(anagrams.values())

# Problem 2: Create a Dictionary
# def create_dictionary(keys, values):  
#    return dict(zip(keys, values))

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(create_dictionary(keys, values))

# # Problem 3: Print Pair

# def print_pair(dictionary, target):
    
#     if target in dictionary:
#         print("Key: ", target)
#         print("Value:", dictionary[target])
#     else:
#         print("That pair does not exist.")


# # Problem 
    
    
    