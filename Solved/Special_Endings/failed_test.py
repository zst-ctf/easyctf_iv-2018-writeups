#! /usr/bin/env python3
from base64 import b64decode, b64encode
from binascii import hexlify, unhexlify
import string

table = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open("encrypted_lines.txt") as file:
    data = file.read()

flag = ""
for line in data.split("\n"):
    string = b64decode(line).decode()
    encoding = b64encode(string.encode()).decode()

    for i, (a, b) in enumerate(zip(chunks(line, 4), chunks(encoding, 4))):
        if a != b:# or (i+1)*4 >= len(line):
            binaries = ""
            for c in a:
                if c != "=":
                    index = table.index(c)
                    binary = bin(index)[2:].zfill(6)
                    binaries += binary

            binaries[-8:]
            print(a, b, chr(int(binaries[-7:].zfill(8), 2)))

            
            while len(binaries) > 8:
                char = int(binaries[:8], 2)
                #print(binaries, bin(char), chr(char), char)
                binaries = binaries[8:]
            '''
            while len(binaries) > 6:
                binaries = binaries[6:]
            '''

            #binaries = binaries.zfill(4)
            #binaries = binaries.ljust(6, '0')

            #print(a, b)
            #print(a, b, binaries, hex(int(binaries, 2)))

            flag += binaries
        
for part in chunks(flag, 8):
    print(table[int(part, 2)], part)
    #print(chr(int(part, 2)), part)