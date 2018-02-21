from soupstituted import *
import itertools
import base64


# create list of unicode chars
digit_list = []
codepoint_list = []
for codepoint in range(2**16):
    c = chr(codepoint)
    if c.isdigit():
        digit_list.append(c)
        codepoint_list.append(codepoint)
 
print(codepoint_list)
# print(len(digit_list))

test = 2365552391
while test > 0:
    if (test in codepoint_list):
        print(test)
        quit()
    test //= 10

print('Done')
'''
def getint(string):
    soup = SoUP(SOup(string))
    return soup

for p in itertools.permutations(digit_list, 7):
    string = ''.join(p)
    result = getint(string) - 2365552391
    print('\r', end='')
    print(p, '\t', result, end='')
    if (result >= 0):
        print(result)
        print(string)
        print(base64.b16encode(string.encode()))
        quit()
'''

'''
# reverse so largest codepoint to smallest
#digit_list = digit_list[::-1]

for p in permutations(digit_list):

perms = [''.join(p) ]



prepend = ''
while len(prepend) < 7:
    for i, ch in enumerate(digit_list):
        payload = prepend + ch
        result = getint(payload.ljust(7, '0'))
        print(payload.ljust(7, '0'))
        if (result - 2365552391 > 0):
            print("Char:", ch)
            print("Codepoint:", ch)
            prepend += ch
            break
    prepend += digit_list[-1] #else add largest

payload = prepend
result = getint(payload)
print(result - 2365552391)
'''