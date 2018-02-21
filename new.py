#!/usr/bin/env python3
import sys
import os

argv = sys.argv
argv.pop(0)

if len(argv) > 3:
    print("Usage: ./new.py challenge_name category points")
    quit()

challenge = argv[0].strip()
category = argv[1].strip()
points = argv[2].strip()

assert points.isdigit() == True

folder = ''.join(c if c.isalnum() else '_' for c in challenge).rstrip('_')
folder_readme = folder + "/README.md"
if not os.path.exists(folder):
    os.makedirs(folder)

if not os.path.exists(folder_readme):
    with open("TEMPLATE.md", 'r') as f:
        template = f.read()

    with open(folder + "/README.md", 'w') as f2:
        template = template.replace("CHALLENGE", challenge)
        template = template.replace("CATEGORY", category)
        template = template.replace("POINTS", points)
        f2.write(template)

    with open("README.md", 'a') as f3:
        f3.write(f'[{challenge}](./Solved/{folder}) | {category} | {points} | \n')
else:
    print('Already created')