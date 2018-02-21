#!/usr/bin/env python3
import base64

with open('encrypted_lines.txt') as file:
    lines = file.readlines()

for line in lines:
    try:
        print(base64.b64decode(line).decode('ascii'))
        continue
    except:
        pass
    print(line)
