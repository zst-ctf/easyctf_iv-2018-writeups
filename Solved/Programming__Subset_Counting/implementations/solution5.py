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

output = []
# https://stackoverflow.com/questions/16046880/i-have-a-list-of-numbers-and-a-certain-sum-and-i-need-to-calculate-the-possible
def subset_sum_recursive(numbers,target,partial):
    s = sum(partial)

    #check if the partial sum is equals to target
    if s == target: 
        global output
        output.append(target)
        #"sum(%s)=%s"%(partial,target)
    if s >= target:
        return # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum_recursive(remaining,target,partial + [n]) 

def subset_sum(numbers,target):
    #we need an intermediate function to start the recursion.
    #the recursion start with an empty list as partial solution.
    subset_sum_recursive(numbers,target,list())


subset_sum(integers, S)
print(len(output))
