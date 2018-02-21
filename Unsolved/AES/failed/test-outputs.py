#!/usr/bin/env python3

from Crypto import Random
from Crypto.Random import random
from Crypto.Cipher import AES
from binascii import *

BLOCK_SIZE = 16

def pad(m):
    p = BLOCK_SIZE - len(m) % BLOCK_SIZE
    return m + p * bytes([p])

def encrypt(key, message, mode=AES.MODE_CBC):
    IV = key    # totally a good idea
    aes = AES.new(key, mode, IV)
    return hexlify(IV + aes.encrypt(pad(message))).decode()

def bin_to_ascii(bin_text):
    input_dec = int(bin_text.encode(), 2)
    t = hex(input_dec).lstrip("0x").rstrip("l")
    if len(t) & 1:
        t = unhexlify("0" + t)
    else:
        t = unhexlify(t)
    return t

def decrypt(key, bintext, length=-1, mode=AES.MODE_CBC):
    IV = key
    assert len(IV) == 16

    ciphertext = bin_to_ascii(bintext)
    assert IV == ciphertext[:len(IV)]

    ciphertext = ciphertext[len(IV):]  # remove IV from front

    aes = AES.new(key, mode, IV)
    decrypted = aes.decrypt(ciphertext)
    #print('decrypted', decrypted)

    if (length == -1):
        p = decrypted[-1]  # last byte will be equal to p
    else:
        p = length
    decrypted_unpadded = decrypted[:-p]  # remove padding

    #print('ciphertext', ciphertext)
    #print('decrypted', decrypted)
    #print('decrypted_unpadded', decrypted_unpadded)
    return hexlify(decrypted_unpadded).decode()

def get_first_block(key):
    # Create AES decryption
    aes = AES.new(key, mode=AES.MODE_ECB)
    decrypted = aes.decrypt(b"\x00" * 16)

    # Get plaintext first block
    plaintext = bytes()
    for a, b in zip(key, decrypted):
        plaintext += bytes([a ^ b])

    # Return plaintext
    return plaintext


key = Random.get_random_bytes(16)
key = b'\x93mE\x81[rU\xe6\xa7z\x94\x034xz"'

def enc_text(plaintext):
    e1 = int(encrypt(key, plaintext), 16)
    d1 = int(decrypt(key, bin(e1)[2:], length=len(plaintext)), 16)
    print('e1 =', hex(e1))
    print('last_block =', hex(e1)[64+2:])
    print('d1 =', hex(d1))
    ex = int(encrypt(key, bin(d1)[2:].encode()), 16)
    print('ex =', hex(ex))
    print()

def enc_recursive(plaintext, iterations):
    enc = plaintext
    for i in range(iterations):
        enc = encrypt(key, enc.encode()[-16:])
    return hexlify(enc.encode()).decode()

print(enc_recursive('\x00'*16, 10))

#enc_text(b'\x00'*16)
'''
enc_text(key)
enc_text(b'\x00'*16)
enc_text(b'\xFF'*16)
enc_text(key + b'\x01'*16)
enc_text(key + b'\x02'*16)
'''
#decrypted = int(decrypt(key, bin(0x00000000000000000000000000000000ecde1567ae0f408473c02294a8580602)[2:]), 16)
#print(decrypted )

'''
aes = AES.new(key, AES.MODE_CBC, key)
print(hexlify(aes.encrypt(('\x00'*16))))
print(hexlify(key))
'''
quit()

'''

'''



enc = int(encrypt(key, b'\x00'*255 + b'\x01'), 16)
dec0 = int(decrypt(key, bin(enc)[2:]), 16)

for i in range(128):
    decrypted = int(decrypt(key, bin(1<<(i) ^ enc)[2:]), 16)
    encrypted = int(decrypt(key, bin(1<<(i) ^ enc)[2:]), 16)
    print(i, hex(decrypted), hex(encrypted ^ enc), hex(decrypted ^ dec0))

xored = 0
for n in range(128):
    i = n+1
    decrypted = int(decrypt(key, bin(i)[2:]), 16)
    xored ^= decrypted

for n in range(128):
    i = n+1
    xored ^= i

print(xored )
quit()


# p1 == encrypt(p129)
# encrypt(p1) == encrypt(encrypt(p129))
# decrypt(p1) == p129


compare = 0
for numb in range(1, 2**16):

    binary = bin(numb)[2:]
    plaintext = bin_to_ascii(binary)
    enc = int(encrypt(key, plaintext), 16)
    if (numb == 1):
        compare = enc
        xored = 0
    else:
        xored = compare ^ enc
    #decrypted = int(decrypt(key, bin(enc)[2:]), 16)
    #assert (numb == decrypted)
    print(f"{hex(numb)[2:].ljust(4)} | {hex(enc)[34:]} | {hex(xored)}")

