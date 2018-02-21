# Liar
Reverse Engineering - 70 points

## Challenge 
> Written by michael

> Sometimes, developers put their source into their code with `-g`. Sometimes, they put another source into their code with `-g`.

>[executable](d692f7a8a8626a021ff89ce1227c9d51c7c59184d3934c1a73f3a0a84043588f_getflag)

>[source](c0a63b9876c7c3f3fb6df61d6131f24fb75ca7625426709932a0029d21d1d84c_getflag.c)


## Solution

Analysis after looking through disassembly in Hopper

1. it takes in a digit using scanf
2. runs through some cipher
3. prints only if the resulting output starts with 'easyctf'

	
	// checks for string starting with the hex '65617379637466' (easyctf)

	if (((
		((*(int8_t *)g & 0xff) == 0x65) &&
	    ((*(int8_t *)0x2011a1 & 0xff) == 0x61)) && 
	    ((*(int8_t *)0x2011a2 & 0xff) == 0x73)) &&
	    ((*(int8_t *)0x2011a3 & 0xff) == 0x79)) {
	    
	    if ((*(int8_t *)0x2011a4 & 0xff) == 0x63) {
            if ((*(int8_t *)0x2011a5 & 0xff) == 0x74) {
                if ((*(int8_t *)0x2011a6 & 0xff) == 0x66) {
                        rax = 0x0;
                        rax = printf("the flag is %s\n", g);
                }
            }
	    }
	}

Hence, we can bruteforce the unknown digit since it will only print with the correct input.

	for i in {1..100}; do echo $i | ./getflag; done
	the flag is easyctf{still_wasn't_too_bad,_right?}

## Flag
`easyctf{still_wasn't_too_bad,_right?}`