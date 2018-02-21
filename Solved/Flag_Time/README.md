# Flag Time
Miscellaneous - 80 points

## Challenge 
> Written by neptunia

> This problem is so easy, it can be solved in a matter of seconds. Connect to `c1.easyctf.com:12482`.

## Hint
> time for u to get an ez flag

## Solution

When entering in the header of the flag, it takes a few seconds to respond.

If you notice, it takes 1 second per correct character. ("matter of seconds")

Hence we can bruteforce the payload character by character by counting the seconds


	$ python3 solve.py 
	Starting bruteforce
	9 easyctf{e
	10 easyctf{ez
	11 easyctf{ez_
	12 easyctf{ez_t
	13 easyctf{ez_t1
	14 easyctf{ez_t1m
	15 easyctf{ez_t1m1
	16 easyctf{ez_t1m1n
	17 easyctf{ez_t1m1ng
	18 easyctf{ez_t1m1ng_
	19 easyctf{ez_t1m1ng_4
	20 easyctf{ez_t1m1ng_4t
	21 easyctf{ez_t1m1ng_4tt
	22 easyctf{ez_t1m1ng_4tta
	23 easyctf{ez_t1m1ng_4ttac
	24 easyctf{ez_t1m1ng_4ttack
	25 easyctf{ez_t1m1ng_4ttack!
	26 easyctf{ez_t1m1ng_4ttack!}

## Flag
`easyctf{ez_t1m1ng_4ttack!}`