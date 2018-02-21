# format
Binary Exploitation - 160 points

## Challenge 
> Go to [`/problems/format`](./files) on the shell server and tell me what is in `flag.txt`.

## Solution

Program seeds at current seconds since Unix epoch

	srand(time(0));

Make a C program to create the same random number and feed it into `./format`. (Do it within the same second and it works)

	$ gcc payload.c -o payload
	$ ~/payload | ./format 
	Enter your name: Your name is: name

	Enter your secret password (in hex)
	easyctf{p3sky_f0rm4t_s7uff}

## Flag
`easyctf{p3sky_f0rm4t_s7uff}`