# Keyed Xor
Cryptography - 100 points

## Challenge 
> Written by sso999

> A flag has been encrypted using keyed xor. Can you decrypt it?

> [File](102bcaa49609327736d8ebae118a7d1dd6285a9527dcb18bd690a592d648a408_keyed_xor.txt).

> The key was created by taking two words from this [wordlist.](1cdfad12bcae77ef64defecc1f5f030639e517c4e2ccac33b7ca6a1e059aafe9_words.txt)

## Solution
Since we know the flag starts with 'easyctf{' (8 chars), let's try to get the first word

	>>> xor(ciphertext, 'easyctf{')
	'spectatoq~u{k}u}wd}pvhb\x7fbusq}fv}|}m\x7fpzs\x7f{w\x7fr|vgfxyf}js\x7fn\x7fqpft}d}vzoogktxfh|'

8 chars gives us 'spectato'
Hence, the first word is either 'spectator' or 'spectators' as inside the wordlist.

---

Thus we can bruteforce it with a few rules... It gives us 3 results...

	> 6347success
	key: spectatorsveneration
	text: easyctf{flpgflagflagflagsutglafcwylgggzjmfihkcurokcagbktnylqdygegzhyvldfml}
	-----

	> 9830success
	key: spectatorsgeneration
	text: easyctf{flagflagflagflagsutglawcwylgggzjmfihkcurokragbktnylqdygegzhyvlufml}
	-----

	> 10782success
	key: spectatorstoleration
	text: easyctf{flrmdlagflagflagsutgladiuylgggzjmfihkcurokakebktnylqdygegzhyvlflol}
	-----

The flag appears to be the 2nd one

## Flag
`easyctf{flagflagflagflagsutglawcwylgggzjmfihkcurokragbktnylqdygegzhyvlufml}`
