# return a modified list
# hint: while loop
# sorted list, no unsorted

# def remove_duplicates(nums):    
#     new = []

#      for num in nums:
#          if num not in new:
#              new.append(num)
        
#     return new


# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))

# Problem 3: Reverse Letters

# You can convert the string to a list (since strings are immutable),

# Use two pointers (left and right) — one starting at the beginning, the other at the end,

# Skip non-letter characters, and

# Swap the letters when both pointers are on letters.



def reverse_only_letters(s):
# turn the string into a list for mutability
# use two pointers to swap letters
# if it is '-' or '_' or any other non-letter character, skip it
    new = list(s)
    left, right = 0, len(new) - 1

    while left < right:
        while left < right and not new[left].isalpha():
            left += 1
        while left < right and not new[right].isalpha():
            right -= 1
        if left < right:
            new[left], new[right] = new[right], new[left]
            left += 1
            right -= 1
        

    return ''.join(new)



s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)


# Problem 4: Longest Uniform Substring
def longest_uniform_substring(s):
# if string is None or empty, return 0   
    if s is None or len(s) == 0:
        return 0
# initialize variables
    max_length = 1
    current_length = 1

    # loop through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
        
    max_length = max(max_length, current_length)
    return max_length
    


s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)


# 
def constant_frequencies(str):
    # accept a string as input and returns a dictionary
    # dictionary onl contains consonants as keys and frequencies as values 
    # B and b are considered the same consonant (make it case-insensitive, do all lowercase)
    # whitespace, punctuation, sybmols, and integers are ignored
    # input can have alphabetic characters, whitespace, punctuation, symbols, and integers
    # but should ignore all those EXCEPT consonants
    # consider edge cases like empty strings, strings with no consonants, etc.
    str = str.lower()  # make it case-insensitive

    if not str:
        return {}
    
    consonants = "bcdfghjklmnpqrstvwxyz"
    frequency = {}

    for char in str:
        if char in consonants:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency    
# Example usage:
    


str = 'Fantastic 4!'
print(constant_frequencies(str))

# Palindrome Verfication
# function takes a string as input and returns True if the string is a palindrome, False otherwise
# palindrome = a word that reads the same backwards as forwards
# must only consider alphabetiical characters, ignore case sensitivity & spaces
# turn into one giant string, remove all non-alphabetic characters, and convert to lowercase
def is_palindrome(string):
    # remove non-alphabetic characters and convert to lowercase
    cleaned = ''.join([c.lower() for c in string if c.isalpha()])
    return cleaned == cleaned[::-1]


print(is_palindrome("race a car"))


