# AES
Cryptography - 160 points

## Challenge 
> Written by sso999

>There's an AES challenge running at `c1.easyctf.com 12487`

> [(source).](aes_redacted.py)

	Input 256 different plaintexts such that:
		 - Each is a binary string
		 - Each has length 256
		 - Input can not be all 0's or all 1's
		 - Let Pi denote the ith plaintext input. Then P0 ^ P1 ^ ... ^ P255 = encrypt(key, P0) ^ encrypt(key, P1) ^ ... ^ encrypt(key, P255)

## Analysis

First 2048 bits produced by encrypt() is always the same... We are controlling the last 256 bits

	def pad(m):
	    p = BLOCK_SIZE - len(m) % BLOCK_SIZE
	    return m + p * bytes([p])

This function pads `p` number of bytes on the right. The value of the byte is `bytes([p])`.
Hence by reading the last byte value, we know how many chars is the padding to unpad it.

Now we can easily write a decrypt function

	def decrypt(key, bintext, mode=AES.MODE_CBC):
	    IV = key

	    ciphertext = bin_to_ascii(bintext)[len(IV):] # remove IV from front

	    aes = AES.new(key, mode, IV)
	    decrypted = aes.decrypt(ciphertext)

	    p = decrypted[-1] # last byte will be equal to p
	    decrypted_unpadded = decrypted[:-p] # remove padding

	    return hexlify(decrypted_unpadded).decode()


https://anh.cs.luc.edu/331/code/aes.py

However, we need to control the input such that the output is predictable...

## Flag
`?`