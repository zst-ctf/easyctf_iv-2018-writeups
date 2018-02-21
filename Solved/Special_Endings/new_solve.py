#!/usr/bin/env python3
from base64 import b64decode, b64encode
import string

table = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


def hidden_binary(a, b):
    if ((not a) or (not b) or
       (not a.endswith('=')) or (not b.endswith('='))):
        return ''

    # 2 bits for a =-padded base64 string
    # 4 bits for a ==-padded one.
    bits = a.count('=') * 2
    a = a.rstrip('=')[-1]
    b = b.rstrip('=')[-1]

    diff = abs(table.index(a) - table.index(b))
    binary = bin(diff)[2:].zfill(bits)
    return binary

with open("encrypted_lines.txt") as file:
    lines = file.read()

binary = ""
for line in lines.splitlines():
    clean = b64encode(b64decode(line)).decode()
    binary += hidden_binary(line, clean)

print(binary)

# Print binary to ASCII
for i in range(0, len(binary), 8):
    print(chr(int(binary[i:i+8], 2)), end='')
print()
