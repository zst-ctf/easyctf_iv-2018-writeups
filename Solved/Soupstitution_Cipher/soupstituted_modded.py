#!/usr/bin/env python3

from binascii import unhexlify as unhexlify
from operator import attrgetter as attrgetter

ME_FLAGE = '<censored>'

'''
>>> SoUP(1234)
4321
'''
def reverse_int(numb):
    x = 0
    while numb != 0:
        x = (x * 10) + (numb % 10)
        numb //= 10
    return x


def str2int(str):
    x = 0
    for ch in str:
        x *= 10
        x += ord(ch) - ord('0')
    return x

def main():
    # get first 7 digits
    user_input = input()[:7] 
    print(user_input)
    if not attrgetter('isdigit')(user_input)():
        print("that's not a number lol")
        return

    # reverse the base-10 integer
    soup = reverse_int(str2int(user_input)) 

    # convert to base-16 integer, then pad zero at the left
    SouP = attrgetter('zfill')(hex(soup)[2:])(8)[-8:]
    
    # compare if text == soup
    #if unhexlify(SouP) == attrgetter('encode')('s0up')():
    if unhexlify(SouP) == b's0up':
        print("oh yay it's a flag!", ME_FLAGE)
    else:
        print('oh noes rip u')

if __name__ == '__main__':
    main()

