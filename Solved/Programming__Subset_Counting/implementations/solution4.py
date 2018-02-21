#!/usr/bin/env python3

# The first line contains two integers N and S.
first_line = input().split(' ')
N = int(first_line[0])
S = int(first_line[1])

# The second line contains N space-separated integers a_1, a_2, ..., a_N.
integers = input().split(' ')
integers = list(filter(None, integers)) # remove empty
integers = list(map(int, integers))
assert len(integers) == N, len(integers)

target_sum = S

# https://stackoverflow.com/questions/18305843/find-all-subsets-that-sum-to-a-particular-value
def total_subsets_matching_sum(numbers, sum):
    array = [1] + [0] * (sum)
    for current_number in numbers:
        for num in range(sum - current_number, -1, -1):
            if array[num]:
                array[num + current_number] += array[num]
    return array[sum]

print(total_subsets_matching_sum(integers, target_sum))
