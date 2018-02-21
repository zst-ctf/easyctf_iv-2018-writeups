# RSA_v
Cryptography - 200 points

## Challenge 
> Bob is extremely paranoid, so he decided that just one RSA encryption is not enough. Before sending his message to Alice, he forced her to create 5 public keys so he could encrypt his message 5 times! Show him that he still is not secure... [rsa.txt](rsa.txt).

## Solution

#### Analysing the keys

The text is encrypted multiple times using the same `n` but different `e`

Take a look at: [Is it safer to encrypt twice with RSA? - StackExchange](https://crypto.stackexchange.com/questions/5382/is-it-safer-to-encrypt-twice-with-rsa)

It is said that for 2 exponents: `c = (m^e1)^e2 (mod n)`

Hence, our `e` in this case is to multiply all 5 exponents together.

	e = 11 * 41 * 67623079903 * 5161910578063 * 175238643578591220695210061216092361657427152135258210375005373467710731238260448371371798471959129039441888531548193154205671

And we have our new `e` to work with

	e = 27587468384672288862881213094354358587433516035212531881921186101712498639965289973292625430363076074737388345935775494312333025500409503290686394032069

#### Wiener attack

[Looking at some lists of exploits to do](https://github.com/eazebu/RSAExploits#exploits)...

We notice our `e` is huge. (Reference: [PlaidCTF CTF 2015 Curious](https://github.com/ctfs/write-ups-2015/tree/master/plaidctf-2015/crypto/curious))

When `e` is large, `d` is small.
Hence, Wiener's attack can be used when `d` is small.

> python3 solve.py

## Flag
`easyctf{keblftftzibatdsqmqotemmty}`