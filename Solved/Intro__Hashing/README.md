# Intro: Hashing
Miscellaneous - 20 points

## Challenge 
> Written by gengkev

>Cryptographic hashes are pretty cool! Take the SHA-512 hash of [this file](74183a3cfd8b4fb83a8180fc4dae4cbeac96b7ae9ac9ec1a8a10ef2a6d00e9ae_image.png), and submit it as your flag.

## Hint
> Try searching the web to find out what SHA-512 is.

## Solution

	 $ shasum -a 512 *.png
	 $ openssl dgst -sha512 *.png

## Flag
Flag is the SHA-512 sum in hex
