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

# https://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number/3421173
def f(v, i, S, memo):
  if i >= len(v): return 1 if S == 0 else 0
  if (i, S) not in memo:  # <-- Check if value has not been calculated.
    count = f(v, i + 1, S, memo)
    count += f(v, i + 1, S - v[i], memo)
    memo[(i, S)] = count  # <-- Memoize calculated result.
  return memo[(i, S)]     # <-- Return memoized value.

def g(v, S, memo):
  subset = []
  for i, x in enumerate(v):
    # Check if there is still a solution if we include v[i]
    if f(v, i + 1, S - x, memo) > 0:
      subset.append(x)
      S -= x
  return subset


memo = dict()
result = f(integers, 0, target_sum, memo)

#if result != 0:
#	print(g(integers, target_sum, memo))
print(result)
