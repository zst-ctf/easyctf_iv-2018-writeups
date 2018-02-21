# Programming: Teaching Old Tricks New Dogs
Programming - 40 points

## Challenge 
> Written by michael

> You can decode a Caesar cipher, but can you write a program to decode a Caesar cipher?

> Your program will be given 2 lines of input, and your program needs to output the original message.

> First line contains `N`, an integer representing how much the key was shifted by. `1 <= N <= 26`
Second line contains the ciphertext, a string consisting of lowercase letters and spaces.
For example:

	6
	o rubk kgyeizl

> You should print

	i love easyctf

## Solution

Similar to solutions for custom base64 charset in python, we can use `str.translate`

> python3 [solution.py](solution.py)
