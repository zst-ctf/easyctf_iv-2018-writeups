#!/usr/bin/env python3
# https://stackoverflow.com/questions/19558769/python-greedy-algorithm

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

# sort by rating
# https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
hackers = sorted(hackers, key=lambda x: x[0], reverse=True)

####################################
# Dynamic programming (Knapsack problem)
####################################
# https://github.com/kaushikthedeveloper/GeeksforGeeks-python/blob/master/Scripts/0-1%20Knapsack%20Problem%20(%20DP%20).py
def knapsack(v: list, w: list, max_weight: int):
    rows = len(v) + 1
    cols = max_weight + 1

    # adding dummy values as later on we consider these values as indexed from 1 for convinence
    v = [0] + v[:]
    w = [0] + w[:]

    # row : values , #col : weights
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    # 0th row and 0th column have value 0

    # values
    for i in range(1, rows):
        # weights
        for j in range(1, cols):
            # if this weight exceeds max_weight at that point
            if j - w[i] < 0:
                dp_array[i][j] = dp_array[i - 1][j]

            # max of -> last ele taken | this ele taken + max of previous values possible
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], v[i] + dp_array[i - 1][j - w[i]])

    # return dp_array[rows][cols]  : will have the max value possible for given wieghts

    values_chosen = []
    i = rows - 1
    j = cols - 1

    # Get the items to be picked
    while i > 0 and j > 0:

        # ith element is added
        if dp_array[i][j] != dp_array[i - 1][j]:
            # add the value
            values_chosen.append(v[i])
            # decrease the weight possible (j)
            j = j - w[i]
            # go to previous row
            i = i - 1

        else:
            i = i - 1

    return dp_array[rows - 1][cols - 1], values_chosen


####################################
# pass input to function
####################################
weights = list(i[1] for i in hackers)
ratings = list(i[0] for i in hackers)
max_weight = W

max_rating, ratings_chosen = knapsack(ratings, weights, max_weight)
print(max_rating)
