#!/usr/bin/env python3

from Crypto import Random
from Crypto.Random import random
from Crypto.Cipher import AES
from binascii import *

flag = "<redacted>"

BLOCK_SIZE = 16

# Pad m using PKCS#7 
'''
pad with n bytes of the ASCII(n) on the right
n = 1 to 16
'''
def pad(m):
    p = BLOCK_SIZE - len(m) % BLOCK_SIZE
    print('len', len(m), 'pad', p)
    return m + p * bytes([p])

# AES encrypt
def encrypt(key, message, mode=AES.MODE_CBC):
    IV = key    # totally a good idea
    aes = AES.new(key, mode, IV)
    #print("PADDED", pad(message))
    #print("NO-PAD", (message))
    return hexlify(IV + aes.encrypt(pad(message))).decode()

def encrypt2(key, message, mode=AES.MODE_CBC):
    IV = key    # totally a good idea
    aes = AES.new(key, mode, IV)
    return aes.encrypt(pad(message))

def decrypt2(key, message, msg_len=256, mode=AES.MODE_CBC):
    IV = key
    assert len(IV) == 16

    aes = AES.new(key, mode, IV)
    decrypted = aes.decrypt(message)

    p = BLOCK_SIZE - msg_len % BLOCK_SIZE
    decrypted_unpadded = decrypted[:-p]
    return hexlify(decrypted_unpadded).decode()

def bin_to_ascii(bin_text):
    input_dec = int(bin_text.encode(), 2)
    t = hex(input_dec).lstrip("0x").rstrip("l")
    if len(t) & 1:
        t = unhexlify("0" + t)
    else:
        t = unhexlify(t)
    return t


def decrypt(key, bintext, mode=AES.MODE_CBC):
    IV = key
    assert len(IV) == 16

    ciphertext = bin_to_ascii(bintext)[len(IV):]  # remove IV from front

    aes = AES.new(key, mode, IV)
    decrypted = aes.decrypt(ciphertext)

    p = decrypted[-1]  # last byte will be equal to p
    decrypted_unpadded = decrypted[:-p]  # remove padding

    print('ciphertext', ciphertext)
    print('decrypted', decrypted)
    print('decrypted_unpadded', decrypted_unpadded)
    return hexlify(decrypted_unpadded).decode()

key = Random.get_random_bytes(16)
print("The key for this session is: {}".format(key))
print("Input 256 different plaintexts such that:")
print("\t - Each is a binary string")
print("\t - Each has length 256")
print("\t - Input can not be all 0's or all 1's")
print("\t - Let Pi denote the ith plaintext input. Then P0 ^ P1 ^ ... ^ P255 = encrypt(key, P0) ^ encrypt(key, P1) ^ ... ^ encrypt(key, P255)")

xor_1 = 0
xor_2 = 0

#print('e1 =', bin(int(encrypt(key, ('0'*254+'00').encode()), 16)))
#print('e1 =', bin(int(encrypt(key, ('0'*254+'01').encode()), 16)))
#print('e2 =', bin(int(encrypt(key, ('0'*254+'10').encode()), 16)))


plaintext = bin_to_ascii('0'*253+'001')
e1 = int(encrypt(key, plaintext), 16)
d1 = int(decrypt(key, bin(e1)[2:]), 16)
print('e1 =', hex(e1)[2:])
print('d1 =', hex(d1)[2:])
print()
plaintext = bin_to_ascii('0'*253+'010')
e2 = int(encrypt(key, plaintext), 16)
d2 = int(decrypt(key, bin(e2)[2:]), 16)
print('e2 =', hex(e2)[2:])
print('d2 =', bin(d2)[2:])
print()
plaintext = bin_to_ascii('0'*253+'011')
e3 = int(encrypt(key, plaintext), 16)
d3 = int(decrypt(key, bin(e3)[2:]), 16)
print('e3 =', hex(e3)[2:])
print('d3 =', bin(d3)[2:])
print()
print('e1-e2 =', hex(e1-e2))
print('e2-e3 =', hex(e2-e3))
print('e1-e3 =', hex(e1-e3))
print()

d0 = int(decrypt(key, '1'*112), 16)
print('d0 =', hex(e1-e3))
print()


#e2 = encrypt2(key, ('0'*254+'01').encode())
#d2 = decrypt2(key, e2)
# print('d2 =', (d2))

quit()
#d2 = bin(int(decrypt(key, ('0'*254+'01').encode())[:-1]+"0", 16))

#print('d2 =', d2[:256])

inputs = set()
for _ in range(2):
    i = input("Input plaintext {}:\t".format(_))
    
    if i in inputs or len(i) != 256 or not set(i) == set('01'):
        print("Input error")
        xor_1 = 0
        xor_2 = 1
        break

    inputs.add(i)
    
    input_dec = int(i, 2)
    xor_1 ^= input_dec
    print('input_dec', hex(input_dec))
    
    t = hex(input_dec).lstrip("0x").rstrip("l")
    if len(t) & 1:
        t = unhexlify("0" + t)
    else:
        t = unhexlify(t)
        
    xor_2 ^= int(encrypt(key, t), 16)
    print('encrypt(key, t)', (encrypt(key, t)))
    print()

if xor_1 == xor_2:
    print(flag)
else:
    print('xor_1:', bin(xor_1))
    print('xor_2:', bin(xor_2))
    print()
    print('xor_1:', hex(xor_1))
    print('xor_2:', hex(xor_2))
    print("Try again")

