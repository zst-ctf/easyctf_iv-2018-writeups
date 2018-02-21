# Not OTP
Cryptography - 100 points

## Challenge 
> Written by neptunia

> It seems we've intercepted 2 strings that were both encrypted with what looks like OTP! Is it possible to decrypt them? file

## Hint
> I think there's something about cribs in there...

## Solution

### Technique
OTP uses XOR, which is vulnerable to *crib dragging*.

Tools:
- https://github.com/1f604/personal-projects/blob/master/decryption/cribsearch.py
- https://github.com/crowell/crib-dragging
- https://github.com/SpiderLabs/cribdrag

Using the latter:

    $ git clone https://github.com/SpiderLabs/cribdrag
    $ cd cribdrag
    
    $ ./xorstrings.py 38445d4e5311544249005351535f005d5d0c575b5e4f481155504e495740145f4c505c5c0e196044454817564d4e12515a5f4f12465c4a45431245430050154b4d4d415c560c4f54144440415f595845494c125953575513454e11525e484550424941595b5a4b 3343464b415550424b415551454b00405b4553135e5f00455f540c535750464954154a5852505a4b00455f5458004b5f430c575b58550c4e5444545e0056405d5f53101055404155145d5f0053565f59524c54574f46416c5854416e525e11506f485206554e51

    $ ./cribdrag.py 0b071b0512440400024106001614001d06490448001048540a04421a00105216184516045c493a0f450d4802154e590e195318491e09460b1756111d00065516121e514c034c0e0100191f410c0f071c1b00460e1c11147f1d1a503c0c1654002d01135f0e141a

### Trial and error

With reference to the [contents in Wikipedia article on known-plaintext attack (cribs)](https://en.wikipedia.org/wiki/Known-plaintext_attack)...

---

    91: "_cr1b_dr4gz}"
    Enter the correct position, 'none' for no match, or 'end' to quit: 91
    Is this crib part of the message or key? Please enter 'message' or 'key': key
    Your message is currently:
    0   _______________this is the secret string
    40   that you will never guess! flag is easy
    80  ctf{otp_ttp_cr1b_dr4gz}
    Your key is currently:
    0   _______________in which babies sleep. Th
    40  ey can also refer to a sample of plainte
    80  xt used in codebreaking
    Please enter your crib: 

---

    Enter the correct position, 'none' for no match, or 'end' to quit: end
    Your message is: _______________this is the secret string that you will never guess! flag is easyctf{otp_ttp_cr1b_dr4gz}
    Your key is: _______________in which babies sleep. They can also refer to a sample of plaintext used in codebreaking


## Flag
`easyctf{otp_ttp_cr1b_dr4gz}`