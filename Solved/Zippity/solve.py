#!/usr/bin/env python3
import socket
import re

s = socket.socket()
s.connect(('c1.easyctf.com', 12483))

database = []
with open('Gaz_zcta_national.txt', 'r') as file:
    for line in file.read().splitlines():
        database.append(line.split('\t'))


def find_answer(zip, question):
    for entry in database:
        if entry[0] != zip:
            continue
        print(">>> Found zip", zip)

        if 'population' in question:
            return entry[1].strip()

        if 'housing' in question:
            return entry[2].strip()

        if 'land area' in question:
            return entry[3].strip()

        if 'water area' in question:
            return entry[4].strip()

        if 'latitude' in question:
            return entry[7].strip()

        if 'longitude' in question:
            return entry[8].strip()

    print('>>> Cannot parse question:', question)


while True:
    data = s.recv(4096).decode().strip()
    if not data:
        continue

    print("Received:", data)
    if 'What is' in data:
        match = re.search(r'zip code (.....)', data)
        zip = match.group(1)
        payload = find_answer(zip, data) + '\n'
        s.send(payload.encode())
    if 'easyctf{' in data:
        quit()
