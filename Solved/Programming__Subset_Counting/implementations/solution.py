#!/usr/bin/env python3

# The first line contains two integers N and S.
first_line = input().split(' ')
N = int(first_line[0])
S = int(first_line[1])

#  The second line contains N space-separated integers a_1, a_2, ..., a_N.
integers = input().split(' ')
integers = list(filter(None, integers)) # remove empty
integers = list(map(int, integers))
assert len(integers) == N, len(integers)

# Code adapted from: http://www.edufyme.com/code/?id=c0c7c76d30bd3dcaefc96f40275bdc0a
output = []
target_sum = S

def ssum(list, sum):
  current = ""
  ssum_h(list, len(list), current, sum)

def ssum_h(list, n, subset, sum):
  if sum == 0:
    output.append(subset)
    # print subset
    return
    
  if n == 0:
    return
    
  if list[n-1] <= sum:
    ssum_h(list, n-1, subset, sum)
    ssum_h(list, n-1, subset + str(list[n-1]) + " ", sum-list[n-1])
  else:
    ssum_h(list, n-1, subset, sum)

    
if __name__ == "__main__":
    ssum(integers, target_sum)
    print(len(output))
    

