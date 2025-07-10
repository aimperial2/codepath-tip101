# Practice Session 1 & 2

# 1.1: def hello_world():

# 1.2: def todays_mood():
#     mood = "😎"
#     print("Today's mood: " + mood)
# todays_mood()

# 1.3: Lunch Menu
# def print_menu(menu):
#     print("Lunch today is: " + menu)

# menu = input("What are you feeling: ")
# print_menu(menu)

# def difference(a, b):
#     return a - b


# 1.4: Sum of two integers
# def sum(a, b):
#     return a + b

# a = 20
# b =5

# total = sum(a, b)
# print(str(total))

#1.5: Product of Two Integers

# def product(a, b):
#     return a * b

# a = int(input("A: "))
# b = int(input("B: "))

# product = product(a, b)
# print(product)

#1.6: Classify Age

# def classify_age(age):
#     if age < 18:
#        return "child"
#     else: 
#         return "adult"

# output = classify_age(5)
# print(output)

# 1.7: Time?
# def what_time_is_it(hour):

#     if hour == 2:
#         return "taco time 🌮"
#     elif hour == 12:
#         return "peanut butter jelly time 🥪"
#     else: 
#         return "nap time 😴"
    
# time = what_time_is_it(1)
# print(time)  
       
    
# 1.8: BlackJack

# def blackjack(score):
    
#     if score == 21:
#         print("Blackjack!")
#     elif score > 21:
#         print("Bust!")
#     elif score >= 17:
#         print("Nice Hand!")
#     else:
#         print("Hit me!")

# blackjack(24)
# blackjack(18)
# blackjack(22)
# blackjack(5)

# 1.9: First Item

# def get_first(lst):

#     if len(lst) == 0:
#        return None
#     else:
#         return lst[0]


# lst= [3,1,6,7,5]
# first = get_first(lst)

# print(first)

# 1.10: Last Item
# def get_last(lst):
#     if len(lst) == 0:
#         return None
#     else:
#         return lst[-1]


# lst= [3,1,6,7,5]
# last = get_last(lst)
# print(last)

# 1.11: Counter
# def counter(stop):
    
#     for i in range(1, stop + 1):
#         print(i)

# counter(6)

#1.12: Sum of 1-10

# def sum_ten():
#     total = 0
#     for num in range (1, 11):
#         total += num
    
#     return total

# sum10 = sum_ten()
# print(sum10)

#1.13: Total Sum
# def sum_positive_range(stop):
#     total = 0

    
# x = 15
# y = 20

# if x > y and y < 30:
#     print("A")
# elif x < y and x < 10:
#     print("B")
# elif x > 15 and x < y:
#     print("C")
# else:

#     print("D")

# final_ans = 0
# for num in range(1,6):
#     final_ans += num

# result = final_ans * 2
# print(result)

# def mystery_function(lst1, lst2):
#     for num in lst2:
#         lst1.append(num)
#     return lst1
# output = mystery_function([1,2,3,4],[5,6,7,8])
# print(output)

# def count_negatives(lst):
#     count = 0
#     for num in lst:
#         if num < 0:
#             count += 1
#     return count

# lst = [1, -2, -3, -5, -1]
# total = count_negatives(lst)
# print(total)


#1.14: Total Sum in Range

#1.15: Negative Numbers 


# a = 6
# b =7
# diff = difference(a, b)
# print("diff = " + str(diff))

# def concatenate_list(nums):
#     ans = nums + nums
#     return ans

# nums = [1, 2, 3, 4]

