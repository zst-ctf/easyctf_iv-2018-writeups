#!/usr/bin/env python3
import string

N = int(input())
text = input()

def rot(s):
    # lowercase letters and spaces
    rotated = "bcdefghijklmnopqrstuvwxyza "
    standard = "abcdefghijklmnopqrstuvwxyz "
    return s.translate(str.maketrans(rotated, standard))

for i in range(N):
    text = rot(text)

print(text)
