#!/usr/bin/env python3
import itertools

####################################
# RETRIEVE THE INPUT
####################################

# The first line contains two integers N and W
first_line = input().split(' ')
N = int(first_line[0])
W = int(first_line[1])

hackers = []
# The following N lines each contain two integers r_i and w_i
# representing the skill and weight of the ith hacker
for i in range(N):
    line = input().split(' ')
    r_i = int(line[0])
    w_i = int(line[1])
    hackers.append((r_i, w_i))

hackers = sorted(hackers, reverse=True)

####################################
# Form iterations of all inputs
####################################
# https://stackoverflow.com/questions/34517540/find-all-combinations-of-a-list-of-numbers-with-a-given-sum
combinations = [seq for i in range(len(hackers), 0, -1)
                    for seq in itertools.combinations(hackers, i)]



####################################
# Find best weight to rating combination
####################################
highest_r = 0
for item in combinations:
    # sum_w = sum(map(lambda x: x[1], item))
    sum_w = sum(w[1] for w in item)
    if sum_w <= W:
        # total_rating = sum(map(lambda x: x[0], item))
        total_rating = sum(r[0] for r in item)
        if total_rating > highest_r:
            highest_r = total_rating

print(highest_r)


'''
possibilities = []
for i, item in enumerate(combinations):
    weights = map(lambda x: x[1], item)
    if sum(weights) <= W:
        possibilities.append(item)

highest_r = 0
for i, item in enumerate(possibilities):
    ratings = map(lambda x: x[0], item)
    total_rating = sum(ratings)
    if total_rating > highest_r:
        highest_r = total_rating

print(highest_r)
'''
