# Souper Strong Primes
Cryptography - 200 points

## Challenge 
> Written by soup

> Technically I used strong primes. But are they really strong in this case? They are big, but there might still be an issue here. 

> [n.txt](n.txt)

> [e.txt](e.txt) 

> [c.txt](c.txt)

## Hint
> I chose "strong" primes, according to wikipedia. But are there strong primes that aren't cryptographically secure for RSA?

## Solution

References:
- https://github.com/HackThisCode/CTF-Writeups/tree/master/2017/Boston%20Key%20Party/RSA%20Buffets
- https://github.com/lanjelot/ctfs/blob/master/NOTES-ctfs

---

#### Fermat's factorisation

Looking at all possible exploits, it could be that the chosen primes are close primes.

I used [this RSA tool](https://github.com/rk700/attackrsa) which implemented the Fermat factorisation attack.

	git clone https://github.com/rk700/attackrsa

And it successfully factorised within seconds.

However, when decrypting using `c^d % n` or `pow(c, d, n)`, it was incredibly slow.

#### Chinese Remainder Theorem

["Chinese Remainder Theorem (CRT) can be used to speed up the calculations for the RSA algorithm"](https://www.di-mgt.com.au/crt_rsa.html).

I adapted this code for [decryption using CRT](https://github.com/lanjelot/ctfs/blob/master/scripts/crypto/rsa/decrypt-rsa-crt.py).

#### Decrypting

With this, putting it all into one script: [`attack.py`](attack.py)

The script completes in about 10 min on my tbMBP2017 base model.

	
	Souper_Strong_Primes $ time python attack.py
	Cracked
	Found private key...
	Decrypting...
	Decrypting...1
	Decrypting...2
	Decrypting...3
	Decrypting...4
	('m =', '0xa444fca4d33ba72c651a0f0527121b64368f2c329537de2f4f16e40aa39ed4c4f178b306bfb772797358936a55c56c1a69fc8bc74da57cafbfd47c4b49e316a00624e1e86f4ec577c01e618425111c4ea1469509f93e32e10716e3904a8b6b0a1d16cd53227a623674f724e45f8d3029814b0b4c2921e469a9ac450633d')
	Decoding...
	Plain text is:

	DO?M3?r?Q??Rq!?Ch??)S}???n@?9?LO?0k?w'?5?6?\V???ȼt?W???GĴ?1jbN???W|?BQ??iP???.qn9?????l?2'?#gOrNE?????F???Pc

	real	9m59.657s
	user	9m46.967s
	sys	0m4.108s

Hmmm? That's weird...

If we try again but print `m` in ***base-10***, we see this

	110010101100001011100110111100101100011011101000110011001111011010100110111010001110010001100000110111001100111010111110111000001110010011010010110110100110011011100110101111101101110001100000111010001011111011100110011000001011111011100110111010001110010001100000011000000110000011011100110011101111101L

Wow, looks like they hid the binary encoding in a base-10 integer...

Add one leading zero and convert it to ASCII

## Flag
`easyctf{Str0ng_prim3s_n0t_s0_str000ng}`
