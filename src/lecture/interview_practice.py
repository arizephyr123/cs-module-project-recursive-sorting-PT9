# Ex. 1
# Given the radius of a circle, calculate it's area and and format
# the result to three decimal places

# A = pi * r^2
# use exact value of pi 
import math # math.pi
# format output as string 
def area_circle(radius):
    # do math to calc area
    area = math.pi * radius**2
    result  = f"{area:.2f}"

print(area_circle(3))   # 28.274






# Ex. 2
# We'll say that a positive int divides itself if every digit in the 
# number divides into the number evenly. So for example 128 divides 
# itself since 1, 2, and 8 all divide into 128 evenly. 
# And we'll say that 0 does not divide into anything evenly, so no 
# number with a 0 digit divides itself. 
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]


# only positive numbers? -> yes
# return bool? -> yes
# implement error handling -> not for now, stretch
def divides_self(num):
    # copy num
    digits_left = num
    # loop through all digits in num
    while digits_left > 0:
        # num % 10 to get the digit on RHS
        digit = num % 10
        print(digit)
        # if that result is 0, return false
        if digit == 0 or 
        # if num % result is NOT 0, return false
        # // 10 to chop off the digit on the RHS

    # if all digits divide evenly, return True



print(divides_self(128)) # → True
print(divides_self(12)) # → True
print(divides_self(120)) # → False



# Ex. 3
# The Knapsack Problem
# https://en.wikipedia.org/wiki/Knapsack_problem

# want to maximize value while staying under
# the weight limit

# no volumn constraint
# each item only exits once (no duplicates)

def naive_knapsack(weight_limit, items):
    items.sort(key= lambda x: x.value, reverse=True)

    sack =[]
    curr_weight = 0
    i = 0
    # while there is room in the sack
    # while curr_weight < weight_limit:
    for i in range(len(items)):
        # put the next most valuable item in it IF there is room 
        if curr_weight + items[i].weight <= weight_limit:               sack.append(items[i])

    return sack

    