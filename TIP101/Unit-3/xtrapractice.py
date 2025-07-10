# Note: I need more practice for Unit 3 since session 1 of this week was embarassing lol

# Methods : .lower()
# lower() returns a string as a lowercase string
# no parameters

s = "Hello World!"
lowercase  = s.lower()
print(lowercase)

hi = "HELLO WORLD"
lowercase2 = hi.lower()
print(lowercase2)

# Example: Valid Palindrome
# Given a string s, return true if it is a palindrome, ignoring case and non-alphanumeric characters.
# EXAMPLE CASES:
#  Input: "Racecar"
# Output: True
# Input: "hello"
# Output: False
# Input: "A man a plan a canal Panama"
# Output: False (because of spaces - only consider letters)
# Input: "race a car"
# Output: False
# Input: "Madam"
# Output: True

# does not accept spaces,punctuations,  must be able to read the word forward and backwards
# use lower() to have it readable
# 
def is_palindrome(s):

    if ' ' in s:    # checks for punctuation
        return False
    
    cleaned = ""
    for char in s:
        if char.isalpha():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

print(is_palindrome("A man a plan a canal Panama"))

print(is_palindrome("Racecar"))

# Split Method - .split()
# splits string into a list along with whitespace or specified separator

s = "Do you ever feel, like a plastic bag"
divorce = s.split()
print(divorce)

s = "Do-you*ever*feel,-like-a*plastic*bag"
separation = s.split("*")
huh = s.split("-")
print(separation)
print(huh)


# Join Method - s.join(x)
# turns iterable x into a string using s as a separator
# parameter is x: iterable that joins together into a string

# Example 1: Join items in a list separated by space
lst = ['Never', 'gonna', 'run', 'around', 'and', 'desert', 'you']
joined = ' '.join(lst)
print(joined) # Prints 'Never gonna run around and desert you'

# Example 2: Join items in a list separated by dash
lst = ['Never', 'gonna', 'make', 'you', 'cry']
joined = '-'.join(lst)
print(joined) # Prints 'Never-gonna-make-you-cry'


# function is wordPattern
# takes input 'pattern' boolean return true or false
# check if there is one to one mapping
# a or b maps to one exact word: dog with a, and cat with b
# letter -> word && word -> letter
# words must match the pattern

# because the string is whole, we SPLIT string
# we end up with a list

# char to word: a: dog, b: cat
# word to char: dog, a  cat, b
# ask interviewer/understand: pattern is always going to be characters

def wordPattern(pattern, s):
    words = s.split(" ")
    if len(words) != len(pattern):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        # Check char -> word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word  # Add new mapping
        
        # Check word -> char mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char  # Add new mapping
    
    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
# fish would not be valid as now a = dog, fish which is NOT 1:1 but 1:2 
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))


