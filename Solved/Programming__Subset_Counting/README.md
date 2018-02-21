# Programming: Subset Counting
Programming - 55 points

## Challenge 
> Written by blockingthesky

> Given a set of numbers, print out how many non-empty subsets sum to a given integer.

#### Input Format
> The first line contains two integers `N` and `S`. The second line contains N space-separated integers `a_1, a_2, ..., a_N`.

	1 <= N <= 20

	-100 <= S <= 100

	-1000 <= a_i <= 1000

> #### Output Format
> A single integer, the number of non-empty subsets which sum to `S`. Two subsets are different if an element appears in one and does not appear in the other. Note that `a_1` is distinct from `a_2`, even if their values are identical.

>#### Sample Input

	6 5
	2 4 1 1 1 2

> #### Sample Ouput

	8

## Solution

The classic [subset sum problem](https://en.m.wikipedia.org/wiki/Subset_sum_problem).

I tried many implementations from various websites. I have concluded that this produces the most complete solution and also utilises dynamic programming techniques (memoisation)

- https://stackoverflow.com/a/3421173

It is adapted as seen in `solution3.py`

However, this gives "Wrong Answer" upon submission...

#### Rectifying the error

From `test2.txt`, we can see that `solution2.py` (utilising bruteforce of all combinations) and `solution3.py` (memoisation), both overcount the answer by an extra 1. This is weird since the answer from bruteforce tallies with that using memoisation

...

We notice that `test2.txt` has a target of zero.

From the challenge, they want "non-empty subsets sum".

Hence, if the target sum is zero, the function takes into account an empty list `[]` which will also produces zero sum.

Dirty fix is to remove that over-count
	
	if result != 0 and target_sum == 0:
		result -= 1

Answer is now correct!
