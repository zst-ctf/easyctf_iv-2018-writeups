# xor
Cryptography - 50 points

## Challenge 
> Written by sso999

> A flag has been encrypted using single-byte xor. Can you decrypt it? [File](xor.txt).

## Solution
Bruteforce XOR single-key
	
Reference: https://stackoverflow.com/questions/41819489/single-byte-xor-cipher-python

	$ python3
	>>> ciphertext = 'Z^LF\KYDLHNJQWO^[H[ZUSP[PZF[TKZ^ZB'
	>>> import binascii
	>>> strings = (''.join(chr(ord(num) ^ key) for num in ciphertext) for key in range(256))
	>>> result = filter(lambda s: 'easyctf' in s.lower(), strings)
	>>> list(result)
	['EASYCTF[SWQUNHPADWDEJLODOEYDKTEAE]', 'easyctf{swqunhpadwdejlodoeydkteae}']


## Flag
`easyctf{swqunhpadwdejlodoeydkteae}`