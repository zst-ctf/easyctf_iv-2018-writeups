#!/usr/bin/env python3

import sys
sys.path.append('./roca-crack/roca-crack')
import keygen
from keygen import *

from functools import reduce
from math import log
from operator import mul
from os import remove
from sys import version_info
from subprocess import check_output

from Crypto.Util.number import getRandomNBitInteger, isPrime
from Crypto.PublicKey import RSA

keysize = 512
assert(e == 65537)

keysize = 1024
N= 132976364789897921342543549711912647694669521920153802982254224725736923458173837255174296819060662269554125350083091285935957540127356604900645893136598839320400831526785060891741096714368740740782188060018589435475785977831257944434032793861699344254315626556027928061047163734435294404321083598799153242551
p= 10963843906295654580762950966589120750613759547438115472159730074622587030995931502682829404396587964653809339116932474831706299935690191214092865019785223
q= 12128626230581436867741417180019798437736056762839322961683042454208508334710589835986128027809048012672618694016108930635808014843088659507102422034429137
prime_count = keygen._prime_count_for_keysize(keysize)
primes = keygen._first_n_primes(prime_count)
M = reduce(mul, primes)  # the primorial M in the paper
e_pow_a = N % M
a = log(e_pow_a, e)
print('a=', a)

'''
N = int(open('n.txt').read())
for prime_count in range(2, 1000):
    primes = keygen._first_n_primes(prime_count)
    M = reduce(mul, primes) 
    e_pow_a = N % M
    a = log(e_pow_a, e)
    assert(pow(e, a) == e_pow_a, pow(e, a))
    if pow(e, int(a)) == e_pow_a:
        print('For n =', prime_count)
        print('    a =', a)
        print('    M =', M)
    print(prime_count)
'''

'''
prime_count = keygen._prime_count_for_keysize(keysize)
primes = keygen._first_n_primes(prime_count)
M = reduce(mul, primes)  # the primorial M in the paper

N = int(open('n.txt').read())

e_pow_a = N % M
a = log(e_pow_a, e)
print('a=', a)

M_bits = int(log(M, 2)) + 1
k_bits = (keysize // 2) - M_bits
a_bits = {
    39: 62, 71: 134, 126: 255, 225: 434
}[prime_count]  # Table 1 - Naive BF # attempts gives order of group

'''
