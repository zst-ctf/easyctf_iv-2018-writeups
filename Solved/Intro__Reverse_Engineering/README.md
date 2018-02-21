# Intro: Reverse Engineering
Intro - 30 points

## Challenge 
> What does this [Python program](mystery.py) do? And more specifically, what input would give this output?

> `6528c39d4b4f03c38a5703c3b90710c39bc2ad45c293c2a3c2b17fc3a0c28343c3bc5c4110c3a3c2bf`

## Hint
> Try plugging in some values and working through it yourself.

## Solution

Analysis of program:
- XOR cipher
- Key of XOR is cyclic (`key[i % len(key)]`)
- Key at each index is multiplied with index (`(i * ord(key[i % len(key)])`)

Hence, this is just XOR cipher with a fixed key, do not need to worry about the key. Apply XOR cipher again.

	$ python3
	
	>>> import mystery
	>>> inputText = bytes.fromhex('6528c39d4b4f03c38a5703c3b90710c39bc2ad45c293c2a3c2b17fc3a0c28343c3bc5c4110c3a3c2bf')

	>>> output = mystery.mystery(inputText.decode("utf-8"))
	>>> output.decode()
	'656173796374667b636861725f62795f636861725f6430306131357d'

	>>> bytes.fromhex(output.decode())
	b'easyctf{char_by_char_d00a15}'

## Flag
`easyctf{char_by_char_d00a15}`