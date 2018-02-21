#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode

n = 9247606623523847772698953161616455664821867183571218056970099751301682205123115716089486799837447397925308887976775994817175994945760278197527909621793469
e = 27587468384672288862881213094354358587433516035212531881921186101712498639965289973292625430363076074737388345935775494312333025500409503290686394032069
c = 7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120

print('n =', n)
print('e =', e)
print('c =', c)

###############################################################
# Do RSA Wiener Attack
###############################################################

'''
References:
    https://crypto.stackexchange.com/questions/777/in-rsa-do-i-calculate-d-from-e-or-e-from-d
    https://github.com/pablocelayes/rsa-wiener-attack

Formula:
    m = c^d % n
'''
import binascii

# Add git directory to path, so we can import easily
import sys
sys.path.insert(0, './rsa-wiener-attack')

# import the hack!
from RSAwienerHacker import hack_RSA
d = hack_RSA(e, n)

# decrypt
priv_key = RSA.construct((n, e, d))
m = priv_key.decrypt(c)
# pow(c, d) % n
# m = pow(c, d, n)

# https://stackoverflow.com/questions/4368676/is-there-a-way-to-pad-to-an-even-number-of-digits
def hex_pair(x):
    return ('0' * (len(x) % 2)) + x

m_hex = '{:x}'.format(m)
m_hex = hex_pair(m_hex)
msg = binascii.unhexlify(m_hex)
print(msg)
