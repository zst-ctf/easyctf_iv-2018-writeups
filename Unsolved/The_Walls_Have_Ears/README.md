# The Walls Have Ears
Networking - 325 points

***[CHALLENGE WAS WITHDRAWN BY ORGANISERS]***

## Challenge 
> Written by michael

> I'm trying to get the flag from `c1.easyctf.com:12488`, but it's asking me for a password I don't know..

> Fortunately, I found this service on the shell server called `/problems/flagclient` that can help me get it! But it's not being very nice to me:( See if you can do better.

> Some useful information:

> - Player key: `244346084`
- It's sending over interface `eth0`
- Please don't brute-force anything

## Hint
> ?

## Analysis

#### Analyse source
    user72122@shell:/problems/flagclient$ ls
    flagclient  flagclient.c  Makefile  password.txt

    user72122@shell:/problems/flagclient$ cat password.txt
    cat: password.txt: Permission denied

    user72122@shell:/problems/flagclient$ cat flagclient.c

***(See [flagclient.c](flagclient.c) for output)***


    void generate_key(char *password, int seed, char *client_key) {
        int i = 0;
        for (char *c = password; *c; ++c, ++i) {
            unsigned char b = (seed >> (8 * (i % 4))) & (char)0xff;
            client_key[i] = *c ^ b;
        }
        client_key[i] = 0;
    }

    244346084 = 0xE906CE4

Value of `b`:

    i=0 -> 0xE4
    i=1 -> 0x6C
    i=2 -> 0x90
    i=3 -> 0x0E
    i=4 -> go to i=0


Test:

    user72122@shell:/problems/flagclient$ ./flagclient
    Tell me your player key, and I'll get your flag for you!
    Enter your key: 244346084

    Ok, we've generated a key for you.
    The last 4 characters are: 6b c5 11 9a

    We'll automatically retrieve the flag now...Done!

    Here you g.. Oh wait, you haven't paid the Usage Fee.
    Please pay the fee first.


    user72122@shell:/problems/flagclient$ du -s -B1 password.txt
    4096 password.txt                                                                                           

---

    pass: 6b c5 11 9a
    key:  e4 6c 90 0e
    outp: 8f a9 81 94

## Flag
***[CHALLENGE WAS WITHDRAWN BY ORGANISERS]***