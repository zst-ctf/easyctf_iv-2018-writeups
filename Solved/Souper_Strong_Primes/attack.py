#!/usr/bin/env python
import sys
sys.path.append('./attackrsa')
from attackrsa import Fermat
import gmpy

n = int(open('n.txt', 'r').read())
e = int(open('e.txt', 'r').read())

# Factorise
fermat = Fermat.Fermat(n)
fermat.e = e
if not fermat.crack():
    print("Failed")
    exit(2)
else:
    print("Cracked")


# Get private key
d = fermat.getPrivKey()
p = fermat.p
q = fermat.q
assert (p * q == n)

print("Found private key...")
# print("d is %s" % hex(d))
# print("p is %s" % hex(p))
# print("q is %s" % hex(q))


# Decrypt
c = int(open('c.txt', 'r').read())
print("Decrypting...0")

# https://github.com/lanjelot/ctfs/blob/master/scripts/crypto/rsa/decrypt-rsa-crt.py
dp = gmpy.invert(e, (p-1))
dq = gmpy.invert(e, (q-1))
qinv = gmpy.invert(q, p)

print("Decrypting...1")
m1 = pow(c, dp, p)

print("Decrypting...2")
m2 = pow(c, dq, q)

print("Decrypting...3")
h = (qinv * (m1 - m2)) % p

print("Decrypting...4")
m = m2 + h * q

'''
print("m = %s" % hex(m))

# Decode to plaintext
print("Decoding...")

hex_string = hex(m)[2:]
if len(hex_string) % 2 != 0:
    hex_string = '0' + hex_string
    # fix odd-length string

msg = hex_string.decode('hex')
print("Plain text is:")
print(msg)
'''
# Print in base 10 instead
print("m = %s" % (m,))
