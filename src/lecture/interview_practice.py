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
'''
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
'''


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

import itertools
# knapsack problem - brute force
# brute fore is like guess and check
def knapsack_brute_force(weight_limit, items):
    all_combos = []
    for i in range(1, len(items)+1):
        # generate all combos using itertools.combinations
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            all_combos.append(combo)

    max_value = -1
    best_combo = None
    for combo in all_combos:
        value = 0 # of the entire combo
        weight = 0 # of the entire combo
        for item in combo:
            value += item.value
            weight += item.weight
        if weight <= weight_limit: # could fit in knapsack
            if value < max_value:
                max_value = value
                best_combo = combo


# Stream lined solution
def knapsack_brute_force_better(weight_limit, items):
    max_value = -1
    best_combo = None
    for i in range(1, len(items)+1):
        # generate all combos using itertools.combinations
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            # check the weight & value
            value = 0 # of the entire combo
            weight = 0 # of the entire combo
            for item in combo:
                value += item.value
                weight += item.weight
            if weight <= weight_limit: # could fit in knapsack
                if value < max_value:
                    max_value = value
                    best_combo = combo


# knapsack- Greedy solution
# PROS: much faster then brute_force, much smarter than naive solution
# CONS: may not get optimal result- will give good, but not best result
def knapsack_greedy(weight_limit, items):
    for i in items:
        i.efficiency = i.value / i.weight

    items.sort(keys=lambda x: x.efficiency, reverse=True)

    sack = []
    weight = 0
    for i in items:
        weight += i.weight
        if weight > weight_limit:
            return sack
        else:
            sack.append(i)


# Fibonacci
# following makes same recursive call calcs multiple times
def fib(n):
    # base case
    if n == 1 or n == 0:
        return 1
    # recursive case
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(15))
print(fib(30))
print(fib(35))

'''
Memoization will optimize functions that need to compute values several times for a single access. Caching will optimize functions that are called several times with the same parameters. In other words, Memoization will optimize the first access whether caching will only optimize recurrent accesses.
'''
# caching is just saving data for later
# specifying place like in 
def fib_cache(n, cache={}):
    # base case
    if n == 1 or n == 0:
        return 1
    # recursive case 
    # elif n in cache: # alt to next line
    elif n in cache.keys(): 
        return cache[n]
    else:
        value = fib_cache(n-1) + fib_cache(n-2)
        cache[n] = value
        return value

print('================')
print(fib_cache(5))
print(fib_cache(15))
print(fib_cache(30))
print(fib_cache(35))
print(fib_cache(40))