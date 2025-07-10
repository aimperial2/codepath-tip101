# Problem Set Ver 3
# Longest Substring

# if string = abcdeefghhhhh
# output: 5

# if string = aaaaaaaaaaaa
# output: 0

# what is sliding window 
# a b c d e f g h h h h h
# set & counter: max length



# def length_of_longest_substring(s):
#     seen = set()
#     left = 0
#     max_length = 0

#     for right in range(len(s)):
#         while s[right] in seen:
#             seen.remove(s[left])
#             left += 1
#         seen.add(s[right])
#         max_length = max(max_length, right - left + 1)

#     return max_length

# print(length_of_longest_substring("abcdeefghhhhh"))

# Problem Set Version 1 

# def count_mississippi(limit):
#     for num in range(1, limit):
#         print( )

# Problem 2: Swap Ends

# def swap_ends(my_str):
#     first = my_str[0]
#     last = my_str[-1]

#     print (last + my_str[1:-1] + first)

# my_str = ""
# swapped = swap_ends(my_str)


# # boolean return
# def is_pangram(my_str):
#     word = my_str.lower()

# #     alphabet = set("abcdefghijklmnopqrstuvwxyz")
# #     f

# # Problem 4: Reverse String

# def reverse_string(my_str):
#     new = ''

#     for i in my_str:
#         new = i + new
    
#     return new

    

# my_str = "live"
# print(reverse_string(my_str))
    

# # Problem 5: 
# # def first_unique_char(my_str):
# #     for i in my_str:
# #         if my_str.count(i) == 1:
# #             return my_str.index
        
# #     return -1




    
# def min_distance(words, word1, word2):
#     right = len(words) - 1
#     left = 0

#     while right >= left:
#         if words[left] == word1 and words[right] == word2:
#             return right - left
#         elif words[left] != word1 and words[left] != word1:
#             left += 1
#             right -= 1
#         elif words[left] != word1:
#             right -= 1
#         elif words[right] != word2:
#             left += 1
 

        
# Problem Set Ver 2 - Session 1

# Perfect Match
# def match_made(dictionary):
# 	for key, value in dictionary.items():
# 		print( f"{key} and {value} are a perfect match.")
		

# match_made({"Peanut butter": "Jelly", 
# 			"Spongebob": "Patrick",
# 			"Ash": "Pikachu"})

# Remove Char
# parameters: s - string; n - integer
# function returns new string with n characters removed where 0 < n < len(s)


def remove_char(s, n):
    if 0 <= n < len(s):     # range only 0 < n < len(s)
        chars = list(s)     # turn it into a list since string is immutable
        chars.pop(n)        # list is mutable so I can remove or pop the specific integer
        return ''.join(chars)   # join the chars-list into string
    
    return s        #default: if not in range, just return the string 

s = "misssing"
fixed_s = remove_char(s, 3)
print(fixed_s)

t = "typpo"
fixed_s = remove_char(t, 2)
print(fixed_s)

# Problem 3: Count Vowels
# parameter takes in a string, and returns an integer value of how many vowels are in the string
# cases to consider: uppercase or lowercase considered
# using set? set = ('A','a','E','e','I','i','O','o','U','u')
# if in the set, we set a vowel counter +1 or use .count()
# a for loop and an if statement?
# is there a default return statement (like -1 or 0?)

# def vowel_count(s):
#     set = {'a','e','i','o','u'}
#     count = 0

#     for i in s.lower():
#         if i in set:
#             count += 1
    
#     return count

#another way to do it that is faster and leetcode efficient

#both are O(n) in time and space complexity going through each character
#for loop: O(n)
#if char in vowels: O(1)
def vowel_count(s):
    vowels = {'a','e','i','o','u'}

    return sum(1 for char in s.lower() if char in vowels)
    
    return count

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)   # 3
count2 = vowel_count(my_str2)
print(count2)   # 10
count3 = vowel_count(my_str3)
print(count3)   # 0

# Problem 4: Reverse Sentence

# takes in sentence - string as parameter
# returns string with sentence but reversed words
# cases: sentence is one word return original sentence, only contain alphabetic chars and spaces
# 
def reverse_sentence(sentence):
    words = []
    for word in sentence.split(" "):
        words.append(word)
    
    return " ".join(reversed(words))

# example: 
sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

# Problem 5: String Compression

# function that has my _str - string as a parameter
# performs basic string compression using counts of repeated characters
# if a char appears more than one time, have a counter of total of that char
# if there is only one instance of that char, don't output char(num)
# possibility of it being "", just return the string
# create a new string? or just use "".join(my_str)

def compress_string(my_str):
    if not my_str:
        return my_str
    
    count = 1
    compressed_str = ""
    current_char = my_str[0]
    for i in range(1, len(my_str)):
        if my_str[i] == current_char:
            count += 1
        else:
            compressed_str += current_char + str(count)
            current_char = my_str[i]
            count = 1

    compressed_str += current_char + str(count)
    
    # Return compressed only if it's shorter than original
    if len(compressed_str) < len(my_str):
        return compressed_str
    else:
        return my_str




my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = ""
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)

