# Adder
Reverse Engineering - 80 points

## Challenge 
> Written by soup

> This program adds numbers. Find the flag! [adder](adder)

## Hint
> Adds numbers.

## Solution

Open in Hopper

	0000000000400b9c         addl       %edx, %eax
	0000000000400b9e         cmpl       $0x539, %eax
	0000000000400ba3         jne        loc_400bcc

Here it is seen that it compares the added number to 0x539 = 1337
	
	$ ./adder 
	Enter three numbers!
	1337
	0
	0
	easyctf{y0u_added_thr33_nums!}


## Flag
`easyctf{y0u_added_thr33_nums!}`