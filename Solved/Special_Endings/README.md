# Special Endings
Forensics - 350 points

## Challenge 
> She taught us so much... 

>[tribute](encrypted_lines.txt)

## Hint
> RFC 4648


## Solution

When decoding, we get a normal looking text file of quotes by an author.

But if we were to re-encode into base64 strings, we realise some endings are different.

Here are some examples of the last 4 chars which differ:

	original	re-encoded 
	Lm==		Lg==
	Lp==		Lg==
	Lm==		Lg==
	ZC7=		ZC4=
	Lm==		Lg==
	dy7=		dy4=
	bh==		bg==

This challenge is the exact same as [DEFCON oCTF 2016 - ultra_encryption](https://github.com/ctfs/write-ups-2016/tree/master/open-ctf-2016/steganography/ultra-encryption-100).

Running their script, we get the flag

	$ python solve.py 
	ill_miss_you

Just for completeness, I rewrote the script in Python 3.

	$ python new_solve.py 
	ill_miss_you

## Flag
`ill_miss_you`