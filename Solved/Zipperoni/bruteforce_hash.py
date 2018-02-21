#!/usr/bin/env python3
import hashlib
import sys
import string

def change_str(s, ch, index):
    s = list(s)
    s[index] = ch
    return ''.join(s)


# get next combination
def increment(pattern_now, index=0):
    if (index > len(pattern_now)):
        return None

    ch = pattern_now[index]
    charset = ''
    if ch != '_':
        if ch.isdigit():
            charset = string.digits
        elif ch.islower():
            charset = string.ascii_lowercase
        elif ch.isupper():
            charset = string.ascii_uppercase

        next_pos = charset.index(ch) + 1
        max_pos = len(charset)

        if (next_pos >= max_pos):
            pattern_now = change_str(pattern_now, charset[0], index)
            pattern_now = increment(pattern_now, index+1)
        else:
            pattern_now = change_str(pattern_now, charset[next_pos], index)
    else:
        pattern_now = increment(pattern_now, index+1)

    return pattern_now


# yield all possible combinations
def generate_permutations(pattern):
    while True:
        yield pattern
        pattern = increment(pattern)
        if pattern == None:
            break

if __name__ == '__main__':
    pattern = open('pattern.txt').read().strip()
    target_hash = open('hash.txt').read().strip()
    bruteforce_char = '0'

    print("Bruteforcing:", target_hash)
    print("Pattern:", pattern)

    # For each of the possibilities, run it through SHA1
    # and check if it is equal to our target.
    # Break out and print once it is correct
    for each in generate_permutations(pattern):
        sha1hex = hashlib.sha1(each.encode()).hexdigest()
        print('\r', each, sha1hex, end='')
        if sha1hex == target_hash:
            with open('password.txt', 'w') as f:
                f.write(each)
            print("\n\n\nSUCCESS:", each)
            quit()
