# hexedit
Reverse Engineering - 50 points

## Challenge 
> Written by r3ndom

> Can you find the flag in [this file?](be60d833b5f96108d7cede754286a78e230871bd02b2c1939b5c1b2d7cd09a64_hexedit)

## Solution

As the name implies

	$ xxd *hexedit | grep 'easyctf' -B 1 -A 1
	00001030: 0000 0000 0000 0000 0000 0000 0000 0000  ................
	00001040: 6561 7379 6374 667b 3962 6665 3938 6239  easyctf{9bfe98b9
	00001050: 7d00 4743 433a 2028 5562 756e 7475 2034  }.GCC: (Ubuntu 4

## Flag
`easyctf{9bfe98b9}`