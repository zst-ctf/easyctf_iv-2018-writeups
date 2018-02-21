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

# https://stackoverflow.com/a/28261391

# use a binary number (represented as string) as a mask
def mask(lst, m):
    # pad number to create a valid selection mask 
    # according to definition in the solution laid out 
    m = m.zfill(len(lst))
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))

def subset_sum(lst, target):
    # there are 2^n binary numbers with length of the original list
    for i in range(2**len(lst)):
        # create the pick corresponsing to current number
        pick = mask(lst, bin(i)[2:])
        if sum(pick) == target:
            yield pick

if __name__ == "__main__":

    result = list(subset_sum(integers, target_sum))
    # solve([1,2,3,4,5], [], 0, 7)
    #solve(integers, [], 0, target_sum)
    #print(subsetsum(integers, target_sum))
    print(len(result))
    #print(subset_sum(integers, target_sum))
    

