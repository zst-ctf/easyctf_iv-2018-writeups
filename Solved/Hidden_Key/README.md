# Hidden Key
Cryptography - 250 points

## Challenge 
> Written by arxenix

>Ugh, another RSA problem? Help me decrypt this message please

> [file](hiddenkey.txt).

## Hint
> i left an extra key in my back pocket


## Solution

#### Formula
![formula]

[formula]: http://slideplayer.com/slide/8615820/26/images/21/RSA+Scheme+(I)*+For+large+2+primes+p,q.jpg

http://slideplayer.com/slide/8615820/26/images/21/RSA+Scheme+(I)*+For+large+2+primes+p,q.jpg

	e = m^e % n
	m = c^d % n

	ed = k * phi + 1 
	ed = 1 (mod phi)
	ed % phi = 1

#### Calculation

	We are given 2d + phi(n)
		Let 2d + phi(n) = X

	Hence,
		0.5X = d + 0.5phi
		0.5Xe = ed + 0.5e*phi
		0.5Xe % phi = ed % phi + 0.5e*phi % phi
		0.5Xe % phi = 1 + 0

	By inspection...
		0.5Xe % phi = 1
		   de % phi = 1
		0.5X = d

> python3 solve.py 

## Flag
`easyctf{awb14vym13jcli5si6}`