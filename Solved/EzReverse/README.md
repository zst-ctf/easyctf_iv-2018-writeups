# EzReverse
Reverse Engineering - 140 points

## Challenge 
> Written by soup

> Take a look at [executable](87ece32cf212ca63756402d7c103af5c1ca9fd8437247fd30dd27ad8c03fb802_executable). Objdump the executable and read some assembly!

## Hint
> Time to read a bit of assembly! Did you know that characters are actually just integers? Take a look at an ASCII table for reference.


## Solution

Look at the decompiled code in hopper.

Simplifying it...

	int main(int arg0, int argv) {
	    first_arg = argv + 0x8

        var_20 = first_arg[0] & 0xff + 0x1;
        var_1C = first_arg[1] & 0xff + 0x2;
        var_18 = first_arg[2] & 0xff + 0x3;
        var_14 = first_arg[3] & 0xff + 0x4;
        var_10 = first_arg[4] & 0xff + 0x5;

        if ( 
	        	(var_14 == 0x6f) &&  // first_arg[3] == 0x6B
	        	(var_18 == var_14 + 0xe) && // first_arg[2] == 0x7A
	        	(var_20 == var_10 - 0xa) // first_arg[0] == first_arg[4] - 6
        	) {
                if (var_1C == 0x35) { // first_arg[1] == 0x33
                        if (var_10 == var_14 + 0x3) { // first_arg[4] == first_arg[3] + 2 == 0x6D
                        	 // first_arg[0] == first_arg[4] - 6 == 0x67
                                rax = 0x0;
                                rax = printf("Now here is your flag: ");
                                rax = print_5(&var_20);
                                rax = 0x1;
                        }
                }
        }

	    return rax;
	}

I simplified it a lot and derived the input argument needed (`first_arg[]`)

Hence, these are the ASCII codes needed: 0x67, 0x33, 0x7A, 0x6B, 0x6D

	$ python
	>>> x = [0x67, 0x33, 0x7A, 0x6B, 0x6D]
	>>> ''.join(map(lambda x: chr(x), x))
	'g3zkm'

	$ ./executable g3zkm
	Now here is your flag: 10453125111114

## Flag
`10453125111114`