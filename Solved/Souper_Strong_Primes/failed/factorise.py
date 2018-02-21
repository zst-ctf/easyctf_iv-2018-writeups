#!/usr/bin/env python3
import gmpy2

n = gmpy2.mpz(int(open('n.txt', 'r').read()))
e = int(open('e.txt', 'r').read())

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

# i = isqrt(n)
i = gmpy2.isqrt(n)

# assert (i*i == n)

print(n - (i * (n / i)))

p, q = 0, 0

count=0
print("Calculating...")
while True:
  if n - (i * (n / i)) == 0:
    p = i
    q = n//i
    break
  i += 1
  count+=1
  #print('\r', count, end='')

print('Iteration: ', count)
print("Solved...")

p = int(p)
q = int(q)
assert(i != p)
assert(p * q == n)

print('p =', int(p))
print('')
print('q =', int(q))
print("Done...")