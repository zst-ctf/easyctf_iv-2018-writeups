from itertools import cycle
import base64
import string

with open('102bcaa49609327736d8ebae118a7d1dd6285a9527dcb18bd690a592d648a408_keyed_xor.txt') as cipherfile:
    ciphertext = cipherfile.read()

with open('1cdfad12bcae77ef64defecc1f5f030639e517c4e2ccac33b7ca6a1e059aafe9_words.txt') as wordfile:
    wordlist = wordfile.read().splitlines()


def xor(data, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
    return xored

permitted_chars = string.ascii_letters + '{}'


def main():
    for word1 in ['spectator', 'spectators']:
        for i, word2 in enumerate(wordlist):
            key = word1 + word2
            text = xor(ciphertext, key)
            if text.count('}') == 1 and \
               text.count('{') == 1 and \
               text.endswith('}') and \
               all(t in permitted_chars for t in text):

                print('success')
                print('key:', key)
                print('text:', text)
                print('-----\n')

            print('\r>', i, end='')

if __name__ == '__main__':
    main()
